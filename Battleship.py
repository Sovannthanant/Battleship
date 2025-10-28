
#----------------------------------------BATTLESHIP----------------------------------------🚢💥
#Mon Pseudo-Code.
#1. Créer le tableau du premier joueur et deuxième joueur.
#2. Créer les dimensions des cinq différents navires:
#   -Un Tourpilleur, dimension de 1x2 espaces.
#   -Deux Croiseur, dimensions de 1x3 espaces.
#   -Un Cuirassé, dimension de 1x4 espaces.
#   -Un Porte-Avion, dimension de 1x5 cases.
#3. Faire Demander aux deux joueurs de placer les bateau dans la grille:
#   -Offrir le choix au joueur s'il veut tourner la pièce dans l'angle des x ou y.
#   -Si le joueur place la pièce et celle-ci dépasse la grille, Redemander de placer.
#   -Sinon Continuer à placer les autres pièces.
#4. Commencer la partie avec le premier joueur, demander qu'il entre une coordonée:
#   -Si le joueur touche un bateau ennemi, marquer une explosion sur la coordonnée.💥
#   -Sinon marquer à la coordonnée une vague. ⬜
#5. Demander le deuxième joueur de jouer et répéter les conditions précédentes.

#1. Créer le tableau du premier joueur et deuxième joueur.
grille_j1 = [
    ["I=========I BATTLESHIPI I=========I"],
    ["  "," A"," B"," C"," D"," E"," F"," G"," H"," I"," J"],
    ["01","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦",],
    ["02","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦",],
    ["03","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦",],
    ["04","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦",],
    ["05","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦",],
    ["06","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦",],
    ["07","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦",],
    ["08","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦",],
    ["09","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦",],
    ["10","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦",],
]

grille_j2 = [
    ["I=========I BATTLESHIPI I=========I"],
    ["  "," A"," B"," C"," D"," E"," F"," G"," H"," I"," J"],
    ["01","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦",],
    ["02","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦",],
    ["03","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦",],
    ["04","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦",],
    ["05","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦",],
    ["06","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦",],
    ["07","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦",],
    ["08","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦",],
    ["09","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦",],
    ["10","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦",],
]

for ligne in grille_j1:
    print(*ligne)
for ligne in grille_j2:
    print(*ligne)