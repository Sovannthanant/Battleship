
#---------------------------------------- BATTLESHIP ----------------------------------------🚢💥
#MON PSEUDO-CODE POUR UN JEU DE BATTLESHIP FONCTIONNEL.
#1. Créer le tableau du premier joueur et du deuxième joueur.
#   - Grille des bateaux et des grilles de tir des deux joueurs.
#   - Fonctions qui permettent de pourvoir les afficher en tant que grille.
#2. Créer les dimensions des cinq différents navires:
#   - Un Torpilleur, dimension de 1x2 cases.
#   - Deux Croiseurs, dimensions de 1x3 cases.
#   - Un Cuirassé, dimension de 1x4 cases.
#   - Un Porte-Avion, dimension de 1x5 cases.
#3. Faire Demander aux deux joueurs de placer leurs bateaux dans leurs grilles:
#   - Appuyer les touches W,A,S,D déplace le bateau, R tourne et E le place.
#       - Si le joueur déplace un bateau hors de la grille, un message est affiché et le mouvement annulé.
#       - Quand le joueur tourne le bateau (ex. torpilleur 1x2 à 2x1) ajuster les cases pour sens vertical.
#       - Lorsque le bateau est placé, le prochain bateau est affiché.
#   - Cette fonction se répète jusqu'à tous les bateaux soient placés, ensuite répéter pour le joueur 2.
#4. Commencer la partie avec le premier joueur, demander qu'il entre une coordonnée sur sa grille de tir:
#   - Si le joueur touche un bateau ennemi:
#       - Marquer une explosion sur grille de tir du joueur 1 et sur la grille bateaux du joueur 2.
#   - Si le joueur fait un tir nul et touche rien:
#       - Marquer un tir nul sur la grille de tir du joueur 1 et sur la grille bateaux du joueur 2.
#   - Tour de l'autre joueur.
#   - S'arrête quand tous les bateaux d'un joueur sont détruit, la partie se termine.
#5. Quand la partie est terminé, un message de victoire pour le joueur gagnant est affiché.
#   - Afficher un message de victoire pour le joueur gagnant est affiché.
#   - Demandez aux joueurs s'ils veulent rejouer une partie :
#       - Si oui, recommencez le programme depuis le début.
#       - Si non, terminer le programme.

#==================== NOTES IMPORTANTES DE L'ENSEIGNANTE ==================== ⚠️⚠️⚠️
#   - Plus de Commentaires tout au long du programme.
#   - Des Documentations pour les fonctions qui ne sont pas expliquées (fonctions def).
#   - Faire attention au Pseudo code (Si, Sinon, Demander, Afficher et autre). Ils devraient être plus détaillés et
#   découper par fonctions.
#   - Commencer à déplacer certaines fonctions dans un autre fichier pour les utiliser comme modules, hors du principal.
#   - Prévoir et faire des plans de test sous forme de tableau, les fichiers de types .md avec l'utilisation de Pytest.
#   - Il faut avancer plus vite, il reste beaucoup de travails à faire encore.


#-------------------- 1. Créer le tableau du premier joueur et du deuxième joueur --------------------
#Quand le joueur 1 tir dans sa grille_tir_j1, les tirs sont marqué sur cette grille et le joueur 2 reçoit les tirs du
#joueur 1 dans sa grille_bateaux_j2. C'est la même chose si le joueur 2 tir sur le joueur 1.
#   - Les grille_bateaux et grille_tir des deux joueurs sont, les quatres, des listes à 2 dimensions.

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
    ["  "," A"," B"," C"," D"," E"," F"," G"," H"," I"," J"],   #10 elements dans une ligne(list).
    ["01","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],   #10 elements dans une colonne(list(list).
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
    ["  "," A"," B"," C"," D"," E"," F"," G"," H"," I"," J"],   #La grille est une liste à deux dimensions.
    ["01","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],   #Des listes à l'intérieur d'une grande liste.
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
def afficher_grille_bateaux_j1():
    """Fonction qui permet d'afficher la grille des bateaux du joueur 1."""
    print("I=====I BATEAUX DU JOUEUR 1 I=====I")
    for ligne in grille_bateaux_j1:
        print(*ligne)
    print("")

def afficher_grille_tir_j1():
    """Fonction qui permet d'afficher la grille des tirs du joueur 1."""
    print("I=======I TIR DU JOUEUR 1 I=======I")
    for ligne in grille_tir_j1:
        print(*ligne)
    print("")

def afficher_grille_bateaux_j2():
    """Fonction qui permet d'afficher la grille des bateaux du joueur 2."""
    print("I=====I BATEAUX DU JOUEUR 2 I=====I")
    for ligne in grille_bateaux_j2:
        print(*ligne)
    print("")

def afficher_grille_tirs_j2():
    """Fonction qui permet d'afficher la grille des tirs du joueur 2"""
    print("I=======I TIR DU JOUEUR 2 I=======I")
    for ligne in grille_tir_j2:
        print(*ligne)
    print("")

#-------------------- 2. Créer les dimensions des cinq différents navires --------------------
#Nous utiliseront cinq bateaux pour notre jeu Battleship, chacun de ces bateaux sont représentés
#par des éléments dans une liste. Le plus il y a d'élément, le plus long est le bateau. Il y a
#un bool pour vérifier quand les bateaux ont été placés, ça servira dans une fonction plus tard.

#   - Un Torpilleur, dimension de 1x2 cases.
liste_torpilleur = ["To","To"]
cases_torpilleur = 1                             #Je ne compte pas l'élément initial, c'est pourquoi
torpilleur_placer = False                       #les cases ont un élément de moins.

#   - Deux Croiseurs, dimension de 1x3 cases.
liste_croiseur1 = ["C1","C1","C1"]
liste_croiseur2 = ["C2","C2","C2"]
cases_croiseur = 2
croiseur1_placer = False
croiseur2_placer = False

#   - Un Cuirassé, dimension de 1x4 cases.
liste_cuirasse = ["Cu","Cu","Cu","Cu"]
cases_cuirasse = 3
cuirasse_placer = False

#   - Un Porte-Avion, dimension de 1x5 cases.
liste_porte_avion = ["PA","PA","PA","PA","PA"]
cases_porte_avion = 4
porte_avion_placer = False

#Dictionare pour les ordres de placement des bateaux.
ordre_placement = {
    1 : liste_torpilleur,
    2 : liste_croiseur1,
    3 : liste_croiseur2,
    4 : liste_cuirasse,
    5 : liste_porte_avion,
}
#Lors que cette variable est activé, le placement des bateaux s'interrompt.
bateaux_placer = torpilleur_placer and croiseur1_placer and croiseur2_placer and cuirasse_placer and porte_avion_placer

#-------------------- 3. Faire Demander aux joueurs de placer leurs bateaux --------------------

def placement_initial():
    """Fonction qui permet de choisir où placer des bateaux la grille en utilisant W,A,S,D pour se déplacer, R
    pour faire une rotation et E pour placer le bateau. Une fois placer, le prochain bateau apparait pour son
    placement. Quand les bateaux sont placés, c'est au tour de l'autre joueur de placer, puis la partie débute."""
    #Les bateaux commencent au centre de la grille, à la coordonnée E5.
    ligne =  5
    colonne = 5
    quantite_bateaux = 0
    grille_bateaux_j1[ligne][colonne] = liste_torpilleur[0]
    grille_bateaux_j1[ligne][colonne+1] = liste_torpilleur[1]
    afficher_grille_bateaux_j1()
    #Le déplacement des bateaux se fait en utilisant les touches W,A,S,D, R pour tourner et E pour placer.
    while quantite_bateaux < 5:
        quantite_bateaux += 1
        while True:
            reponse = str.upper(input("Appuyer W,A,S,D pour déplacer et E pour placer: "))
            if reponse == "W":
                if ligne == 1:
                    print("Hors de la grille")
                    afficher_grille_bateaux_j1()
                elif ligne > 1:
                    grille_bateaux_j1[ligne][colonne] = "~~"
                    grille_bateaux_j1[ligne][colonne + 1] = "~~"
                    ligne -= 1
                    grille_bateaux_j1[ligne][colonne] = liste_torpilleur[0]
                    grille_bateaux_j1[ligne][colonne+1] = liste_torpilleur[1]
                    afficher_grille_bateaux_j1()
            elif reponse == "S":
                if ligne == 10:
                    print("Hors de la grille")
                    afficher_grille_bateaux_j1()
                elif ligne < 10:
                    grille_bateaux_j1[ligne][colonne] = "~~"
                    grille_bateaux_j1[ligne][colonne + 1] = "~~"
                    ligne += 1
                    grille_bateaux_j1[ligne][colonne] = liste_torpilleur[0]
                    grille_bateaux_j1[ligne][colonne + 1] = liste_torpilleur[1]
                    afficher_grille_bateaux_j1()
            elif reponse == "A":
                if colonne == 1:
                    print("Hors de la grille")
                    afficher_grille_bateaux_j1()
                else:
                    grille_bateaux_j1[ligne][colonne] = "~~"
                    grille_bateaux_j1[ligne][colonne + 1] = "~~"
                    colonne -= 1
                    grille_bateaux_j1[ligne][colonne] = liste_torpilleur[0]
                    grille_bateaux_j1[ligne][colonne + 1] = liste_torpilleur[1]
                    afficher_grille_bateaux_j1()
            elif reponse == "D":
                if colonne == 10 -1:
                    print("Hors de la grille")
                    afficher_grille_bateaux_j1()
                else:
                    grille_bateaux_j1[ligne][colonne] = "~~"
                    grille_bateaux_j1[ligne][colonne + 1] = "~~"
                    colonne += 1
                    grille_bateaux_j1[ligne][colonne] = liste_torpilleur[0]
                    grille_bateaux_j1[ligne][colonne + 1] = liste_torpilleur[1]
                    afficher_grille_bateaux_j1()
            elif reponse == "E":
                break
    return grille_bateaux_j1

#---------------------------------------- GROS TEST (VA ÊTRE ENLEVÉ BIENTOT) ----------------------------------------

def placement_initial2():
    """Fonction qui permet de choisir où placer des bateaux la grille en utilisant W,A,S,D pour se déplacer, R
    pour faire une rotation et E pour placer le bateau. Une fois placer, le prochain bateau apparait pour son
    placement. Quand les bateaux sont placés, c'est au tour de l'autre joueur de placer, puis la partie débute."""
    nombre_bateaux = 0          #Le nombre de bateaux dans la grille.
    cases_bateaux = 0           #Le nombre de cases que le bateau.
    ordre_placement.get(0)      #Clé pour trouver valeur(listes) des bateaux.
    while nombre_bateaux < 5:
    # Les bateaux commencent au centre de la grille, à la coordonnée E5.
        nombre_bateaux += 1
        cases_bateaux += 1
        bateau = ordre_placement.get(cases_bateaux)
        ligne = 5
        colonne = 5
        grille_bateaux_j1[ligne][colonne] = bateau[0]
        grille_bateaux_j1[ligne][colonne + 1] = bateau[1]
        afficher_grille_bateaux_j1()
        while True:
    # Le déplacement des bateaux se fait en utilisant les touches W,A,S,D, R pour tourner et E pour placer.
            reponse = str.upper(input("Appuyer W,A,S,D pour déplacer et E pour placer: "))
            if reponse == "R":
                    grille_bateaux_j1[ligne][colonne] = liste_torpilleur[0]
                    grille_bateaux_j1[ligne-1][colonne] = liste_torpilleur[1]
                    afficher_grille_bateaux_j1()
            elif reponse == "W":
                if ligne == 1:
                    print("Hors de la grille")
                    afficher_grille_bateaux_j1()
                elif ligne > 1:
                    grille_bateaux_j1[ligne][colonne] = "~~"
                    grille_bateaux_j1[ligne][colonne + 1] = "~~"
                    ligne -= 1
                    grille_bateaux_j1[ligne][colonne] = liste_torpilleur[0]
                    grille_bateaux_j1[ligne][colonne+1] = liste_torpilleur[1]
                    afficher_grille_bateaux_j1()
            elif reponse == "S":
                if ligne == 10:
                    print("Hors de la grille")
                    afficher_grille_bateaux_j1()
                elif ligne < 10:
                    grille_bateaux_j1[ligne][colonne] = "~~"
                    grille_bateaux_j1[ligne][colonne + 1] = "~~"
                    ligne += 1
                    grille_bateaux_j1[ligne][colonne] = liste_torpilleur[0]
                    grille_bateaux_j1[ligne][colonne + 1] = liste_torpilleur[1]
                    afficher_grille_bateaux_j1()
            elif reponse == "A":
                if colonne == 1:
                    print("Hors de la grille")
                    afficher_grille_bateaux_j1()
                else:
                    grille_bateaux_j1[ligne][colonne] = "~~"
                    grille_bateaux_j1[ligne][colonne + 1] = "~~"
                    colonne -= 1
                    grille_bateaux_j1[ligne][colonne] = liste_torpilleur[0]
                    grille_bateaux_j1[ligne][colonne + 1] = liste_torpilleur[1]
                    afficher_grille_bateaux_j1()
            elif reponse == "D":
                if colonne == 10 -1:
                    print("Hors de la grille")
                    afficher_grille_bateaux_j1()
                else:
                    grille_bateaux_j1[ligne][colonne] = "~~"
                    grille_bateaux_j1[ligne][colonne + 1] = "~~"
                    colonne += 1
                    grille_bateaux_j1[ligne][colonne] = liste_torpilleur[0]
                    grille_bateaux_j1[ligne][colonne + 1] = liste_torpilleur[1]
                    afficher_grille_bateaux_j1()
            elif reponse == "E":
                break
    return grille_bateaux_j1

print(ordre_placement.get(1))
print(f"{ordre_placement.keys}")
print(f"{ordre_placement.values()}")

#placement_initial()
placement_initial2()
input("Appuyer n'importe qu'elle touche pour afficher la grille")
afficher_grille_bateaux_j1()


#LIEN INTERESSANT:
#https://www.geeksforgeeks.org/python/python-using-2d-arrays-lists-the-right-way/
