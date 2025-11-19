# Plan de test pour les fonctions de Battleship.py
 
## 1.---------- Fonctions d'affichage ----------
Il n'y a pas beaucoup de vérifications à faire pour les fonctions d'affichages.\
Elles impriment des listes sous forme de grille pour faire des tableaux.
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


## 2.---------- Fonctions de placement ----------
### message_hors_grille()
| Valeur expecter                        | Valeur sortie                          | Bon ou non|
|----------------------------------------|----------------------------------------|-----------|
| "LE DÉPLACEMENT VA HORS DE LA GRILLE." | "LE DÉPLACEMENT VA HORS DE LA GRILLE." | Bon       |
### placement_bateaux(joueur)
| Valeur entrée | Valeur expecter                      | Valeur sortie                | Bon ou non |
|---------------|--------------------------------------|------------------------------|------------|
| w             | Déplacement du bateau vers le haut   | Déplacement vers le haut     | Bon        |
| S             | Déplacement du bateau vers le bas    | Déplacement vers le bas      | Bon        |
| A             | Déplacement du bateau vers la gauche | Déplacement vers la gauche   | Bon        |
| D             | Déplacement du bateau vers la droite | Déplacement vers la droite   | Bon        |
| R             | Rotation du bateau                   | Rotation du tableau          | Bon        |
| E             | Placement et prochain bateau         | Placement et prochain bateau | Bon        |
| 2             | Redemande la question                | Redemande la question        | Bon        |
| =             | Redemande la question                | Redemande la question        | Bon        |
Le déplacement d'un bateau sur un autre, efface celui qui est en dessous.
Les bateaux peut toujours allez en dessous de la grille quand not horizontal.

## 3.---------- Fonctions de tirs ----------
### placement_tirs(grille_tirs, grille_bateaux, colonne, ligne)
| Valeur entrée                 | Valeur expecter                      | Valeur sortie               | Bon ou non |
|-------------------------------|--------------------------------------|-----------------------------|------------|
| Case "~~"                     | Remplacer la case avec "}{"          | Remplacer la case avec "}{" | Bon        |
| Case "To","C1","C2","Cu","PA" | Remplacer la case avec "()"          | Remplacer la case avec "()" | Bon        |
| Cases "}{" ou "()"            | Redemande une coordonnée             | Redemande une coordonnée    | Bon        |
### message_tirs_sur_tirs()
| Valeur expecter                        | Valeur sortie                          | Bon ou non|
|----------------------------------------|----------------------------------------|-----------|
| "VOUS AVEZ DÉJÀ TIRER ICI, RÉESSAYER." | "VOUS AVEZ DÉJÀ TIRER ICI, RÉESSAYER." | Bon       |
### demande_coordonnee(joueur)
| Valeur entrée | Valeur expecter                                                       | Valeur sortie                                                        | Bon ou non |
|---------------|-----------------------------------------------------------------------|----------------------------------------------------------------------|------------|
| E,5           | placement_tirs()                                                      | placement_tirs()                                                     | Bon        |
| E,11          | "Veuillez entrez un chiffre de 1 à 10 pour tirer dans la grille."     | "Veuillez entrez un chiffre de 1 à 10 pour tirer dans la grille."    | Bon        |
| K,5           | "Veuillez entrez une lettre de A à J pour tirer dans la grille."      | "Veuillez entrez une lettre de A à J pour tirer dans la grille."     | Bon        |
| BA,11         | "Écrivez un lettre de A à J, une virgule et et un chiffre de 1 à 10." | "Écrivez un lettre de A à J, une virgule et et un chiffre de 1 à 10."| Bon        |


## 4.---------- Boucle de partie ----------
Il n'y a pas de fonction définie, c'est simplement une boucle while. Lorsque\
on entre la reponse OUI, elle recommence sinon termine le programme.