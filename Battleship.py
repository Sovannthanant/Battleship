
#---------------------------------------- JEU BATTLESHIP SUR LA CONSOLE ----------------------------------------
#---------------------------------------- PSEUDO-CODE POUR BATTLESHIP----------------------------------------
#1. Créer le tableau du premier joueur et du deuxième joueur (Battleship.py).
#   - Grille des bateaux et des grilles de tir des deux joueurs.
#   - Fonctions qui permettent de pourvoir les afficher en tant que grille (Battleship_Fonctions.py).
#2. Créer les dimensions des cinq différents navires (Battleship.py):
#   - Un Torpilleur, dimension de 1x2 cases.
#   - Deux Croiseurs, dimensions de 1x3 cases.
#   - Un Cuirassé, dimension de 1x4 cases.
#   - Un Porte-Avion, dimension de 1x5 cases.
#   - Un dictionnaire pour définir l'ordre de placement.
#3. Faire Demander aux deux joueurs de placer leurs bateaux dans leurs grilles (Battleship_Fonctions.py):
#   - Appuyer les touches W,A,S,D déplace le bateau, R tourne et E le place.
#       - Si le joueur déplace un bateau hors de la grille, un message est affiché et le mouvement annulé.
#       - Quand le joueur tourne le bateau (ex. torpilleur 1x2 à 2x1) ajuster les cases pour sens vertical.
#       - Lorsque le bateau est placé, le prochain bateau est affiché.
#   - Cette fonction se répète jusqu'à tous les bateaux soient placés, ensuite répéter pour le joueur 2.
#4. Commencer la partie avec le premier joueur, demander qu'il entre une coordonnée sur sa grille de tir:
#   - Si le joueur touche un bateau ennemi:
#       - Marquer une explosion sur grille de tir du joueur 1 et sur la grille bateaux du joueur 2.
#   - Si le joueur fait un tir nul et ne touche rien:
#       - Marquer un tir nul sur la grille de tir du joueur 1 et sur la grille bateaux du joueur 2.
#   - Si le joueur fait un tir sur un tir touché ou tir nul:
#       - Redemander au joueur d'entrer une autre coordonnée.
#   - Tour de l'autre joueur.
#   - S'arrête quand tous les bateaux d'un joueur sont détruit, la partie se termine.
#5. Quand la partie est terminé, un message de victoire pour le joueur gagnant est affiché.
#   - Afficher un message de victoire pour le joueur gagnant est affiché.
#   - Demandez aux joueurs s'ils veulent rejouer une partie:
#       - Si oui, recommencez le programme depuis le début.
#       - Sinon, terminer le programme.


#---------------------------------------- ATTRIBUTION DES VARIABLES ----------------------------------------
from copy import copy
#-------------------- 1. Créer le tableau du premier joueur et du deuxième joueur --------------------
# Quand le joueur 1 tir dans sa grille_tir_j1, les tirs sont marqué sur cette grille et le joueur 2 reçoie les tirs du
# joueur 1 dans sa grille_bateaux_j2. C'est la même chose si le joueur 2 tir sur le joueur 1.
#   - Les grille_bateaux et grille_tir des deux joueurs sont, les quatre, des listes à 2 dimensions.

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
grille_tirs_j1 = [
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
grille_tirs_j2 = [
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

gbj1 = copy(grille_bateaux_j1)
gtj1 = copy(grille_tirs_j1)
gbj2 = copy(grille_bateaux_j2)
gtj2 = copy(grille_tirs_j2)

#-------------------- 2. Créer les dimensions des cinq différents navires --------------------
#Nous utiliseront cinq bateaux pour notre jeu Battleship, chacun de ces bateaux sont représentés
#par des éléments dans une liste. Le plus il y a d'élément, le plus long est le bateau. Il y a
#un bool pour vérifier quand les bateaux ont été placés, ça servira dans une fonction plus tard.

#   - Un Torpilleur, dimension de 1x2 cases.
liste_torpilleur = ["To","To"]

#   - Deux Croiseurs, dimension de 1x3 cases.
liste_croiseur1 = ["C1","C1","C1"]
liste_croiseur2 = ["C2","C2","C2"]

#   - Un Cuirassé, dimension de 1x4 cases.
liste_cuirasse = ["Cu","Cu","Cu","Cu"]

#   - Un Porte-Avion, dimension de 1x5 cases.
liste_porte_avion = ["PA","PA","PA","PA","PA"]

# Dictionnaire pour l'ordre de placement des bateaux.
ordre_placement = {
    1 : liste_torpilleur,
    2 : liste_croiseur1,
    3 : liste_croiseur2,
    4 : liste_cuirasse,
    5 : liste_porte_avion,
}

# Une variable pour déterminer si la partie est terminée
partie_terminer = False
tour_joueur1 = 1

#---------------------------------------- LE PROGRAMME PRINCIPAL ----------------------------------------
from Battleship_Fonctions import placement_bateaux, demande_coordonnee, afficher_grille_tirs_j2

#-------------------- 5. Quand la partie est terminé, un message de victoire est affiché. --------------------

if __name__ == "__main__":
# La boucle est utilisée pour répéter la partie si les joueurs veulent rejouer.
    while True:
        grille_bateaux_j1 = gbj1
        grille_tirs_j1  = gtj1
        grille_bateaux_j2 = gbj2
        grille_tirs_j2 = gtj2
        print(grille_bateaux_j1)
        print(gbj1)

        print("I====I PHASE DES PLACEMENT  I====I")
        grille_bateaux_j1 = placement_bateaux("Joueur1")
        grille_bateaux_j2 = placement_bateaux("Joueur2")

        print("I=======I PHASE DES TIRS I=======I")


# Une boucle pour tirer jusqu'à que les bateaux aient coulés.
#

# Cette boucle est là pour laisser les joueurs tirer jusqu'à qu'il n'y a plus de bateaux reste.
        while not partie_terminer:
            if tour_joueur1 == True:
                for ligne in grille_bateaux_j2:
                    for cases in ligne:
                        if ("To" in ligne or
                            "C1" in ligne or
                            "C2" in ligne or
                            "Cu" in ligne or
                            "PA" in ligne):
                            demande_coordonnee("Joueur1")
                            tour_joueur1 = False
# S'il n'y a plus de bateaux dans une des grilles, la partie est terminée et le joueur gagne.
                print("Joueur 1, vous avez gagner!")
                partie_terminer = True
            if tour_joueur1 == False:
                for ligne in grille_bateaux_j1:
                    for cases in ligne:
                        if ("To" in ligne or
                            "C1" in ligne or
                            "C2" in ligne or
                            "Cu" in ligne or
                            "PA" in ligne):
                            demande_coordonnee("Joueur2")
                            tour_joueur1 = True
            print("Joueur 2, vous avez gagner!")
            partie_terminer = True

        print("I======I PARTIE TERMINÉE I======I")
        reponse = str.upper(input(f"Entrez OUI si voulez vous rejouez: "))
# Si la réponse est OUI, le programme revient au début de la boucle et la partie recommence.
        if reponse == "OUI":
            print("")
        else:
            break

#==================== NOTES IMPORTANTES DE L'ENSEIGNANTE ==================== ⚠️⚠️⚠️
#   - ✅ Plus de Commentaires tout au long du programme.
#   - ✅ Des Documentations pour les fonctions qui ne sont pas expliquées (fonctions def).
#   - ✅ Faire attention au Pseudo code (Si, Sinon, Demander, Afficher et autre). Ils devraient être plus détaillés et
#   découper par fonctions.
#   - ✅ Commencer à déplacer certaines fonctions dans un fichier pour les utiliser comme modules, hors du principal.
#   - ✅ Il faut avancer plus vite, il reste beaucoup de travails à faire encore.
#   - Prévoir et faire des plans de test sous forme de tableau, les fichiers de types .md avec l'utilisation de Pytest.

#ERREUR REMARQUER
#TODO: Dans la fonction def placement_bateau :
#   - Quand un bateau passe au dessus un autre bateau, les cases de l'ancien bateau se fait remplacer par une vague et
#     se fait effacer.
#TODO: Dans la fonction def demande_coordonnée :
#   - Ne s'arrête pas encore lorsque que les bateaux sont tous détruits.
#TODO: Vider les tableaux de bateaux quand une partie est recommencer.