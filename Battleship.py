
#----------------------------------------BATTLESHIP----------------------------------------🚢💥
#Mon Pseudo-Code pour un jeu de Battleship fonctionnel.
#1. Créer le tableau du premier joueur et deuxième joueur.
#   -Grille des bateaux du premier joueur et sa grille de tir.
#   -Grille des bateaux du deuxième joueur et sa grille de tir.
#2. Créer les dimensions des cinq différents navires:
#   -Un Tourpilleur, dimension de 1x2 espaces.
#   -Deux Croiseur, dimensions de 1x3 espaces.
#   -Un Cuirassé, dimension de 1x4 espaces.
#   -Un Porte-Avion, dimension de 1x5 cases.
#3. Faire Demander aux deux joueurs de tourner et placer les bateau dans la grille:
#   -Si le joueur place la pièce et celle-ci dépasse la grille ou est sur un autre bateau redemander de placer.
#   -Sinon Continuer à placer les autres pièces.
#4. Commencer la partie avec le premier joueur, demander qu'il entre une coordonée:
#   -Si le joueur touche un bateau ennemi, marquer une explosion sur la coordonnée.💥
#   -Sinon marquer à la coordonnée une vague. ⬜
#5. Demander le deuxième joueur de jouer et répéter les conditions précédentes.



#--------------------1. Créer le tableau du premier joueur et deuxième joueur.--------------------
#Quand le joueur 1 tir dans sa grille_tir_j1, les tirs sont marqué sur sa grille et le joueur 2
#reçoit les tirs dans sa grille_bateaux_j2.

#   -Grille des bateaux du premier joueur et grille de tir.
grille_bateaux_j1 = [
    ["  "," A"," B"," C"," D"," E"," F"," G"," H"," I"," J"],
    ["01","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["02","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["03","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["04","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["05","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["06","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["07","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["08","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["09","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["10","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
]
grille_tir_j1 = [
    ["  "," A"," B"," C"," D"," E"," F"," G"," H"," I"," J"],
    ["01","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["02","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["03","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["04","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["05","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["06","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["07","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["08","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["09","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["10","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
]
#   -Grille des bateaux du deuxìème joueur et grille de tir.
grille_bateaux_j2 = [
    ["  "," A"," B"," C"," D"," E"," F"," G"," H"," I"," J"],
    ["01","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["02","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["03","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["04","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["05","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["06","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["07","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["08","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["09","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["10","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
]
grille_tir_j2 = [
    ["  "," A"," B"," C"," D"," E"," F"," G"," H"," I"," J"],
    ["01","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["02","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["03","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["04","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["05","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["06","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["07","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["08","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["09","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["10","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
]

def afficher_grille_bateaux_j1():    #grille_bateau_j1 : list
    """Fonction qui permet d'afficher les bateaux du joueur 1."""
    print("I=====I BATEAUX DU JOUEUR 1 I=====I")
    for ligne in grille_bateaux_j1:
        print(*ligne)
    print("")

def afficher_grille_tir_j1():       #grille_tir_j1 : list
    """Fonction qui permet d'afficher les tirs du joueur 1."""
    print("I=======I TIR DU JOUEUR 1 I=======I")
    for ligne in grille_tir_j1:
        print(*ligne)
    print("")

def afficher_grille_bateaux_j2():    #grille_bateau_j2 : list
    """Fonction qui permet d'afficher les bateaux du joueur 2."""
    print("I=====I BATEAUX DU JOUEUR 2 I=====I")
    for ligne in grille_bateaux_j2:
        print(*ligne)
    print("")

def afficher_grille_tirs_j2():      #grille_tir_j2 : list
    """Fonction qui permet d'afficher les tirs du joueur 2"""
    print("I=======I TIR DU JOUEUR 2 I=======I")
    for ligne in grille_tir_j2:
        print(*ligne)
    print("")

#--------------------2. Créer les dimensions des cinq différents navires:--------------------
#   -Un Tourpilleur, dimension de 1x2 cases.
liste_tourpilleur = ["II","II"]
tourpilleur_axe_x = " ".join(map(str,liste_tourpilleur))
tourpilleur_placer = False

#   -Deux Croiseurs, dimensions de 1x3 cases.
croiseur1_axe_x = ["1","1","1"]
croiseur2_axe_x = ["1","1","1"]
croiseur1_placer = False
croiseur2_placer = False

#   -Un Cuirassé, dimension de 1x4 cases.
cuirasse_axe_x = ["1","1","1","1"],
cuirasse_placer = False

#   -Un Porte-Avion, dimension de 1x5 cases.
porte_avion_axe_x = ["1","1","1","1","1"]
porte_avion_placer = False

#Lors que cette variable est activé, le placement des bateaux s'arret.
bateaux_placer = tourpilleur_placer and croiseur1_placer and croiseur2_placer and cuirasse_axe_x and porte_avion_axe_x

#--------------------3. Faire Demander aux deux joueurs de placer les bateau dans la grille:--------------------

#Pour placer les bateaux j'ai pensé que le bateau s'affichera au centre de la grille et le joueur pourra appuyer
#W,A,S,D pour le bouger R pour le tourner et E pour placer.

def placement_initial_j1():
    """Fonction qui permet qui j1 de choisir où placer ses bateaux la grille."""
    placement_initial = "--"
    ligne = 5
    colonne = 5
    grille_bateaux_j1[colonne][ligne] = tourpilleur_axe_x
    ligne2 = 2
    colonne2 = 2
    grille_bateaux_j1[colonne2][ligne2] = tourpilleur_axe_x
    afficher_grille_bateaux_j1()
    return grille_bateaux_j1


placement_initial_j1()
afficher_grille_tir_j1()

#LIEN INTERESSANT:
#https://www.geeksforgeeks.org/python/python-using-2d-arrays-lists-the-right-way/

#Des messages print utiliser plus tard.
#print("Joueur 1, placer le tourpilleur dans\nvotre grille (pièce de deux cases).")
#print("Joueur 1, placer le croisseur_1 dans\nvotre grille (pièce de trois cases).")
#print("Joueur 1, placer le croisseur_2 dans\nvotre grille (pièce de trois cases).")
#print("Joueur 1, placer le cuirasse dans\nvotre grille (pièce de quatre cases).")
#print("Joueur 1, placer le porte_avion dans\nvotre grille (pièce de cinq cases).")

#print("Joueur 2, placer le tourpilleur dans\nvotre grille (pièce de deux cases).")
#print("Joueur 2, placer le croisseur_1 dans\nvotre grille (pièce de trois cases).")
#print("Joueur 2, placer le croisseur_2 dans\nvotre grille (pièce de trois cases).")
#print("Joueur 2, placer le cuirasse dans\nvotre grille (pièce de quatre cases).")
#print("Joueur 2, placer le porte_avion dans\nvotre grille (pièce de cinq cases).")