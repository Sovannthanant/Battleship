
#----------------------------------------BATTLESHIP----------------------------------------🚢💥
#Mon Pseudo-Code pour un jeu de Battleship fonctionnel.
#1. Créer le tableau du premier joueur et deuxième joueur.
#   -Grille des bateau du premier joueur et son grille de tir.
#   -Grille des bateau du deuxieme joueur et son grille de tir.
#2. Créer les dimensions des cinq différents navires:
#   -Un Tourpilleur, dimension de 1x2 espaces.
#   -Deux Croiseur, dimensions de 1x3 espaces.
#   -Un Cuirassé, dimension de 1x4 espaces.
#   -Un Porte-Avion, dimension de 1x5 cases.
#3. Faire Demander aux deux joueurs de placer les bateau dans la grille:
#   -Offrir le choix au joueur s'il veut tourner la pièce dans l'angle des x ou y.
#   -Si le joueur place la pièce et celle-ci dépasse la grille, redemander de placer.
#   -Sinon Continuer à placer les autres pièces.
#4. Commencer la partie avec le premier joueur, demander qu'il entre une coordonée:
#   -Si le joueur touche un bateau ennemi, marquer une explosion sur la coordonnée.💥
#   -Sinon marquer à la coordonnée une vague. ⬜
#5. Demander le deuxième joueur de jouer et répéter les conditions précédentes.

#1. Créer le tableau du premier joueur et deuxième joueur.
#   -Grille des bateau du premier joueur et grille de tir.
grille_bateau_j1 = [
    ["I=====I BATEAUX DU JOUEUR 1 I=====I"],
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
grille_tir_j1 = [
    ["I=======I TIR DU JOUEUR 1 I=======I"],
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
#   -Grille des bateau du deuxìème joueur et grille de tir.
grille_bateau_j2 = [
    ["I=====I BATEAUX DU JOUEUR 2 I=====I"],
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
grille_tir_j2 = [
    ["I=======I TIR DU JOUEUR 2 I=======I"],
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

#2. Créer les dimensions des cinq différents navires:
#   -Un Tourpilleur, dimension de 1x2 espaces.
tourpilleur_axe_x = ["1","1"]
tourpilleur_placer = False
#   -Deux Croiseur, dimensions de 1x3 espaces.
croiseur1_axe_x = ["1","1","1"]
croiseur2_axe_x = ["1","1","1"]
croiseur1_placer = False
croiseur2_placer = False
#   -Un Cuirassé, dimension de 1x4 espaces.
cuirasse_axe_x = ["1","1","1","1"]
cuirasse_placer = False
#   -Un Porte-Avion, dimension de 1x5 cases.
porte_avion_axe_x = ["1","1","1","1","1"]
porte_avion_placer = False
bateaux_placer = tourpilleur_placer and croiseur1_placer and croiseur2_placer and cuirasse_axe_x and porte_avion_axe_x

#3. Faire Demander aux deux joueurs de placer les bateau dans la grille:
#   -Offrir le choix au joueur s'il veut tourner la pièce dans l'angle des x ou y.

print("Veuillez placer le tourpilleur dans votre grille (pièce de deux cases).")

print("")
for ligne in grille_bateau_j1:
    print(*ligne)

for ligne in grille_tir_j1:
    print(*ligne)