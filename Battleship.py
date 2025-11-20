
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
#-------------------- 1. Créer le tableau du premier joueur et du deuxième joueur --------------------
# Quand le joueur 1 tir dans sa grille_tir_j1, les tirs sont marqué sur cette grille et le joueur 2 reçoie les tirs du
# joueur 1 dans sa grille_bateaux_j2. C'est la même chose si le joueur 2 tir sur le joueur 1.
#   - Les grille_bateaux et grille_tir des deux joueurs sont, les quatre, des listes à 2 dimensions.

grille_bateaux_j1 = [
    ["  "," A"," B"," C"," D"," E"," F"," G"," H"," I"," J"],  # Les colonnes sont de 10 éléments, mais j'en ai
    ["01","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],  # ajouté 1 pour éviter des problèmes de IndexError.
    ["02","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],  # C'était plus compliqué de mettre try et except
    ["03","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],  # plusieurs fois. À la place, j'ai changé la grille.
    ["04","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["05","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],  # Les lignes sont  de 10 éléments.
    ["06","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["07","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["08","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["09","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["10","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
]
grille_tirs_j1 = [
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
    ["  "," A"," B"," C"," D"," E"," F"," G"," H"," I"," J"],   # La grille est une liste à deux dimensions.
    ["01","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],   # Des listes à l'intérieur d'une grande liste.
    ["02","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],   # Grilles crée par VANN SOVANNTHANANT.
    ["03","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["04","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["05","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["06","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["07","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["08","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["09","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
    ["10","~~","~~","~~","~~","~~","~~","~~","~~","~~","~~"],
]


#-------------------- 2. Créer les dimensions des cinq différents navires --------------------
# Nous utiliseront cinq bateaux pour notre jeu Battleship, chacun de ces bateaux sont représentés
# par des éléments dans une liste. Le plus il y a d'élément, le plus long est le bateau. Il y a
# un bool pour vérifier quand les bateaux ont été placés, ça servira dans une fonction plus tard.
# Variables et dictionnaire fait par LAMARANA SOW et VANN SOVANNTHANANT.

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

# Un boolean pour déterminer si la partie est terminée
partie_terminer = False

# Un boolean que si elle est True, c'est le tour du j1.
# Si le boolean est de type False, c'est le tour du j2.
tour_joueur1 = True

# Un Int pour voir s'il reste des bateaux dans des grilles.
compteur_bateaux = 0


#---------------------------------------- LE PROGRAMME PRINCIPAL ----------------------------------------
from Battleship_Fonctions import placement_bateaux, demande_coordonnee, affichage_ecran_accueil, texte_clignotant
#-------------------- 5. Quand la partie est terminé, un message de victoire est affiché. --------------------
# Dans le programme principal, j'ai utilisé beaucoup de fonctions liées aux temps pour afficher les messages à
# un certain intervalle de temps pour faciliter la lecture du programme par l'utilisateur. - VANN SOVANNTHANANT
import time

if __name__ == "__main__":
# La boucle est utilisée pour répéter la partie si les joueurs veulent rejouer.
    while True:
        # L'écran d'acceuil.
        affichage_ecran_accueil()
        input("I=I Appuyer Entrée pour Débuter I=I")
        print("\n"*10)

        # Les placements de bateaux.
        print("I=====I PHASE DES PLACEMENT I=====I")
        print("Les joueurs vont placer les bateaux.\nLes contrôles sont W,A,S,D,R et E.")
        texte_clignotant("...CHARGEMENT GRILLE_BATEAUX_J1...",4)
        print("\n" * 10)
        grille_bateaux_j1 = placement_bateaux("Joueur1")
        texte_clignotant("...CHARGEMENT GRILLE_BATEAUX_J2...", 3)
        print("\n" * 10)
        grille_bateaux_j2 = placement_bateaux("Joueur2")
        print("\n" * 10)

        # Les placements de tirs.
        print("I=======I PHASE DES TIRS I=======I")
        print("Les joueurs vont essayer de tirer\nsur les bateaux ennemis en entrant\ndes coordonnées. (exemple: A,5).")
        texte_clignotant("...CHARGEMENT GRILLE_TIRS(J1,J2)...", 5)
        print("\n" * 10)
        while not partie_terminer:
            # Tour du premier joueur.
            if tour_joueur1 == True:
                demande_coordonnee("Joueur1")
                for ligne in grille_bateaux_j2:
                    if ("To" in ligne or
                        "C1" in ligne or
                        "C2" in ligne or
                        "Cu" in ligne or
                        "PA" in ligne):
                        compteur_bateaux += 1
                    else:
                        compteur_bateaux += 0
            # Vérifie s'il y a des bateaux à l'aide du compteur.
            # S'il n'y a plus bateaux, la partie est terminée.
                if compteur_bateaux > 0:
                    tour_joueur1 = False
                    compteur_bateaux = 0
                elif compteur_bateaux == 0:
                    partie_terminer = True
                    print("Joueur 1, vous avez gagner! ⭐")
            time.sleep(2)
            # Tour du deuxième joueur.
            if tour_joueur1 == False:
                demande_coordonnee("Joueur2")
                for ligne in grille_bateaux_j1:
                    if ("To" in ligne or
                        "C1" in ligne or
                        "C2" in ligne or
                        "Cu" in ligne or
                        "PA" in ligne):
                        compteur_bateaux += 1
                    else:
                        compteur_bateaux += 0
                if compteur_bateaux > 0:
                    tour_joueur1 = True
                    compteur_bateaux = 0
                elif compteur_bateaux == 0:
                    partie_terminer = True
                    print("Joueur 2, vous avez gagner! ⭐")
            time.sleep(2)

        # Demande si les joueurs veulent rejouer.
        print("I======I PARTIE TERMINÉE I======I")
        reponse = str.upper(input(f"Entrez OUI si voulez vous rejouez: "))
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
#     se fait effacer quand en not horizontal.
#TODO: Les bateaux ne doivent pas être coller lors du placement (les bordures ont des problèmes).
#TODO: Les déplacement vers le bas dépasse la grille quand not horizontal.