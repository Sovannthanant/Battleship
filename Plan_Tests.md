# Plan de test pour les fonctions de Battleship.py
 
## ---------- Fonctions d'affichage ----------
Il n'y a pas beaucoup de vérifications à faire pour les fonctions d'affichages.
### afficher_grille_bateaux_j1()
| Valeur expecter    | Valeur sortie      | Bon ou non |
|--------------------|--------------------|------------|
| La grille imprimée | La grille imprimée | Bon        |
### afficher_grille_tirs_j1()
| Valeur expecter    | Valeur sortie      | Bon ou non |
|--------------------|--------------------|------------|
| La grille imprimée | La grille imprimée | Bon        |
### afficher_grille_bateaux_j2()
| Valeur expecter    | Valeur sortie      | Bon ou non |
|--------------------|--------------------|------------|
| La grille imprimée | La grille imprimée | Bon        |
### afficher_grille_tirs_j2()
| Valeur expecter    | Valeur sortie      | Bon ou non |
|--------------------|--------------------|------------|
| La grille imprimée | La grille imprimée | Bon        |


## ---------- Fonctions de placement ----------
Une petite fonction : message_hors_ligne() et une grande fonction : placement_bateaux.
### message_hors_grille()
| Valeur expecter                                    | Valeur sortie                                     | Bon ou non|
|----------------------------------------------------|---------------------------------------------------|-----------|
| imprimer "LE DÉPLACEMENT VA HORS DE LA GRILLE. ⚠️" | imprimée "LE DÉPLACEMENT VA HORS DE LA GRILLE. ⚠️"| Bon       |

### placement_bateaux()
| Valeur entrée    | Valeur expecter              | Valeur sortie                | Bon ou non |
|------------------|------------------------------|------------------------------|------------|
| X                | La grille imprimée           | La grille imprimée           | Bon        |