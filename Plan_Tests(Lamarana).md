# Plan de tests – Projet Battleship 

Ce document présente **mon plan de tests unitaires** pour quelques fonctions de mon projet *Battleship*, en utilisant la méthode **AAA (Arrange / Act / Assert)** vue en cours.

---

## 1. Fonction `placement_tirs(grille_tirs, grille_bateaux, colonne, ligne)`

### Rôle de la fonction

Cette fonction sert à gérer le résultat d’un tir dans le jeu.  
En gros, selon ce qu’il y a dans la case visée, elle met à jour :

- la **grille de tirs** du joueur (là où il voit ses tirs),
- la **grille de bateaux** de l’adversaire.

Deux cas principaux :

- Si la case visée est de l’eau (`"~~"`), c’est un tir raté :  
  → on met le symbole `"}{"` dans les deux grilles  
  → et on affiche `"TIR MANQUÉ 🌊"` dans la console.

- Si la case visée correspond à une partie d’un bateau (`"To"`, `"C1"`, `"C2"`, `"Cu"`, `"PA"`), c’est un tir réussi :  
  → on met le symbole `"()"` dans les deux grilles  
  → et on affiche `"TIR TOUCHÉ 💥"` dans la console.

### Ce que je veux vérifier avec les tests

Pour cette fonction, je veux vérifier plusieurs choses :

- que les paramètres `grille_tirs` et `grille_bateaux` sont bien des listes de listes ;
- que la **bonne case** est bien modifiée dans les deux grilles après l’appel à la fonction ;
- que le bon **symbole** est utilisé :
  - `"}{"` pour un tir dans l’eau ;
  - `"()"` pour un tir sur un bateau ;
- que le **message affiché** dans la console correspond au bon cas :
  - `"TIR MANQUÉ"` pour un tir dans l’eau ;
  - `"TIR TOUCHÉ"` pour un tir sur un bateau.

### Tableau du plan de tests

| Cas # | Description                          | État initial de `grille_bateaux[ligne][colonne]` | Données d’entrée (ligne, colonne) | Résultat attendu dans `grille_tirs` | Résultat attendu dans `grille_bateaux` | Message console attendu  | Vérifications (assert) principales                                                                 |
|------:|--------------------------------------|--------------------------------------------------|------------------------------------|-------------------------------------|----------------------------------------|---------------------------|-------------------------------------------------------------------------------------------------------------------|
| 1     | Tir dans l’eau (tir manqué)         | `"~~"`                                           | ligne = 1, colonne = 1            | `grille_tirs[1][1] == '}{'`         | `grille_bateaux[1][1] == '}{'`         | contient `"TIR MANQUÉ"`  | `assert grille_tirs[1][1] == '}{'` ; `assert grille_bateaux[1][1] == '}{'` ; `assert "TIR MANQUÉ" in captured.out` |
| 2     | Tir sur un Torpilleur               | `"To"`                                           | ligne = 1, colonne = 1            | `grille_tirs[1][1] == '()'`         | `grille_bateaux[1][1] == '()'`         | contient `"TIR TOUCHÉ"`  | `assert grille_tirs[1][1] == '()'` ; `assert grille_bateaux[1][1] == '()'` ; `assert "TIR TOUCHÉ" in captured.out` |
| 3     | Tir sur un Croiseur 1               | `"C1"`                                           | ligne = 1, colonne = 1            | `grille_tirs[1][1] == '()'`         | `grille_bateaux[1][1] == '()'`         | contient `"TIR TOUCHÉ"`  | pareil que le cas 2, mais avec `"C1"` comme état initial                                                           |
| 4     | Tir sur un Croiseur 2               | `"C2"`                                           | ligne = 1, colonne = 1            | `grille_tirs[1][1] == '()'`         | `grille_bateaux[1][1] == '()'`         | contient `"TIR TOUCHÉ"`  | pareil que le cas 2                                                                                                |
| 5     | Tir sur un Cuirassé                 | `"Cu"`                                           | ligne = 1, colonne = 1            | `grille_tirs[1][1] == '()'`         | `grille_bateaux[1][1] == '()'`         | contient `"TIR TOUCHÉ"`  | pareil que le cas 2                                                                                                |
| 6     | Tir sur un Porte-Avion              | `"PA"`                                           | ligne = 1, colonne = 1            | `grille_tirs[1][1] == '()'`         | `grille_bateaux[1][1] == '()'`         | contient `"TIR TOUCHÉ"`  | pareil que le cas 2                                                                                                |

### Lien avec mes tests pytest

Ces cas de tests sont ensuite utilisés dans un test unitaire paramétré avec `pytest`, par exemple :

```python
@pytest.mark.parametrize("etat_initial, message_attendu, marqueur_attendu", [
    ("~~", "TIR MANQUÉ", "}{"),
    ("To", "TIR TOUCHÉ", "()"),
    ("C1", "TIR TOUCHÉ", "()"),
    ("C2", "TIR TOUCHÉ", "()"),
    ("Cu", "TIR TOUCHÉ", "()"),
    ("PA", "TIR TOUCHÉ", "()"),
])
def test_placement_tirs(capsys, etat_initial, message_attendu, marqueur_attendu):
    # Arrange : je prépare une petite grille de test
    grille_tirs = [["~", "~"], ["~", "~~"]]
    grille_bateaux = [["~", "~"], ["~", etat_initial]]

    # Act : j'appelle la fonction que je veux tester
    bf.placement_tirs(grille_tirs, grille_bateaux, colonne=1, ligne=1)
    captured = capsys.readouterr()

    # Assert : je vérifie que le symbole et le message sont corrects
    assert message_attendu in captured.out
    assert grille_tirs[1][1] == marqueur_attendu
    assert grille_bateaux[1][1] == marqueur_attendu
