
#---------------------------------------- BATTLESHIP ----------------------------------------🚢💥
#MON PSEUDO-CODE POUR UN JEU DE BATTLESHIP FONCTIONNEL.
#1. Créer le tableau du premier joueur et du deuxième joueur.
#   - Grille des bateaux et des grilles de tir des deux joueurs.
#   - Fonctions qui permettent de pourvoir les afficher en tant que grille.
#2. Créer les dimensions des cinq différents navires :
#   - Un Torpilleur, dimension de 1x2 cases.
#   - Deux Croiseurs, dimensions de 1x3 cases.
#   - Un Cuirassé, dimension de 1x4 cases.
#   - Un Porte-Avion, dimension de 1x5 cases.
#3. Faire Demander aux deux joueurs de placer leurs bateaux dans leurs grilles :
#   - Appuyer les touches W,A,S,D déplace le bateau, R tourne et E le place.
#       - Si le joueur déplace un bateau hors de la grille, un message est affiché et le mouvement annulé.
#       - Quand le joueur tourne le bateau (ex. torpilleur 1x2 à 2x1) ajuster les cases pour sens vertical.
#       - Lorsque le bateau est placé, le prochain bateau est affiché.
#   - Cette fonction se répète jusqu'à tous les bateaux soient placés, ensuite répéter pour le joueur 2.
#4. Commencer la partie avec le premier joueur, demander qu'il entre une coordonnée sur sa grille de tir :
#   - Si le joueur touche un bateau ennemi:
#       - Marquer une explosion sur grille de tir du joueur 1 et sur la grille bateaux du joueur 2.
#   - Si le joueur fait un tir nul et touche rien :
#       - Marquer un tir nul sur la grille de tir du joueur 1 et sur la grille bateaux du joueur 2.
#
#   - Tour de l'autre joueur.
#   - S'arrête quand tous les bateaux d'un joueur sont détruit, la partie se termine.
#5. Quand la partie est terminé, un message de victoire pour le joueur gagnant est affiché.
#   - Afficher un message de victoire pour le joueur gagnant est affiché.
#   - Demandez aux joueurs s'ils veulent rejouer une partie :
#       - Si oui, recommencez le programme depuis le début.
#       - Si non, terminer le programme.

#==================== NOTES IMPORTANTES DE L'ENSEIGNANTE ==================== ⚠️⚠️⚠️
#   - ✅ Plus de Commentaires tout au long du programme.
#   - ✅ Des Documentations pour les fonctions qui ne sont pas expliquées (fonctions def).
#   - ✅ Faire attention au Pseudo code (Si, Sinon, Demander, Afficher et autre). Ils devraient être plus détaillés et
#   découper par fonctions.
#   - Commencer à déplacer certaines fonctions dans un autre fichier pour les utiliser comme modules, hors du principal.
#   - Prévoir et faire des plans de test sous forme de tableau, les fichiers de types .md avec l'utilisation de Pytest.
#   - ✅ Il faut avancer plus vite, il reste beaucoup de travails à faire encore.


#-------------------- 1. Créer le tableau du premier joueur et du deuxième joueur --------------------
#Quand le joueur 1 tir dans sa grille_tir_j1, les tirs sont marqué sur cette grille et le joueur 2 reçoie les tirs du
#joueur 1 dans sa grille_bateaux_j2. C'est la même chose si le joueur 2 tir sur le joueur 1.
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
def afficher_grille_bateaux_j1():
    """Fonction qui permet d'afficher la grille des bateaux du joueur 1."""
    print("I=====I BATEAUX DU JOUEUR 1 I=====I")
    for ligne in grille_bateaux_j1:
        print(*ligne)

def afficher_grille_tirs_j1():
    """Fonction qui permet d'afficher la grille des tirs du joueur 1."""
    print("I=======I TIR DU JOUEUR 1 I=======I")
    for ligne in grille_tirs_j1:
        print(*ligne)

def afficher_grille_bateaux_j2():
    """Fonction qui permet d'afficher la grille des bateaux du joueur 2."""
    print("I=====I BATEAUX DU JOUEUR 2 I=====I")
    for ligne in grille_bateaux_j2:
        print(*ligne)

def afficher_grille_tirs_j2():
    """Fonction qui permet d'afficher la grille des tirs du joueur 2"""
    print("I=======I TIR DU JOUEUR 2 I=======I")
    for ligne in grille_tirs_j2:
        print(*ligne)

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

#-------------------- 3. Faire Demander aux joueurs de placer leurs bateaux --------------------

def message_hors_grille():
    """Une petite fonction qui sert à afficher un message lorsqu'un déplacement va à l'extérieur de la grille. """
    print("LE DÉPLACEMENT VA HORS DE LA GRILLE. ⚠️")

def placement_bateaux(joueur):
    """Fonction qui permet de choisir où placer des bateaux la grille en utilisant W,A,S,D pour se déplacer, R
    pour faire une rotation et E pour placer le bateau. Une fois placer, le prochain bateau apparait pour son
    placement. Quand les bateaux sont placés, c'est au tour de l'autre joueur de placer, puis la partie débute.
    FONCTION FAITE PAR VANN SOVANNTHANANT."""
    # J'ai réalisé qu'on peut envoyer des variables dans les paramètres des fonctions définies avec ce lien :
    # https://www.w3schools.com/python/gloss_python_function_arguments.asp
    if joueur == "j1":
        grille_bateaux = grille_bateaux_j1
    elif joueur == "j2":
        grille_bateaux = grille_bateaux_j2

    nombre_bateaux = 0
    while nombre_bateaux < 5:
        nombre_bateaux += 1
        horizontal = True

    # Pour la fonction ".get", je me suis inspiré de cette vidéo : https://www.youtube.com/watch?v=MZZSMaEAC2g
        bateau = ordre_placement.get(nombre_bateaux)
    # Les bateaux commencent au centre de la grille, à la coordonnée E5 et le nombre_bateaux augmente jusqu'à 5.
        ligne = 5
        colonne = 5
    # Pour i in range (longueur des valeurs des clés dans ordre_placement (ex. 5 : ["PA","PA","PA","PA","PA")).
        for i in range(len(bateau)):
            grille_bateaux_j1[ligne][colonne +i] = bateau[i]
        if joueur == "j1":
            afficher_grille_bateaux_j1()
        elif joueur == "j2":
            afficher_grille_bateaux_j2()

        while True:
            reponse = str.upper(input("Appuyer W,A,S,D pour déplacer, R pour tourner et E pour placer: "))
    # Avant le déplacement du bateau, les cases bateau sont effacées pour éviter d'avoir une copie du bateau.
            if horizontal:
                for i in range(len(bateau)):
                    grille_bateaux[ligne][colonne +i] = "~~"
            elif not horizontal:
                for i in range(len(bateau)):
                    grille_bateaux[ligne +i][colonne] = "~~"

    # Les touches "W" et "S" permettent des déplacements vertical, donc les bateaux se déplacent sur ligne.
            if reponse == "W":
                if ligne > 1:
                    ligne -= 1
                elif ligne == 1:
                    message_hors_grille()
            elif reponse == "S":
                if ligne < 10 and (not ligne + len(bateau) -1 >= 10):
                    ligne += 1
                elif ligne == 10 or (ligne + len(bateau) - 1>= 10):
                    message_hors_grille()
    # Les touches "A" et "D" permettent des déplacements horizontal, les bateaux se déplacent sur colonne.
            elif reponse == "A":
                if colonne > 1:
                    colonne -= 1
                elif colonne == 1:
                    message_hors_grille()
            elif reponse == "D":
                if colonne + len(bateau) -1 < 10 or (colonne < 10 and not horizontal):
                    colonne += 1
                elif colonne + len(bateau) -1 == 10:
                    message_hors_grille()
    # La touche "R" alterne entre horizontal et not horizontal, et "E" sert à conclure le placement.
            if reponse == "R":
                if ligne < 10:
                    horizontal = not horizontal
                elif ligne == 10:
                    message_hors_grille()
            elif reponse == "E":
                if horizontal:
                    for i in range(len(bateau)):
                        grille_bateaux[ligne][colonne +i] = bateau[i]
                elif not horizontal:
                    for i in range(len(bateau)):
                        grille_bateaux[ligne +i][colonne] = bateau[i]
                break

    # Pour éviter de répéter afficher_grille_bateaux_j1(j2) après chaque touches, je l'ai mis à la fin.
            if horizontal:
                for i in range(len(bateau)):
                    grille_bateaux[ligne][colonne +i] = bateau[i]
            elif not horizontal:
                try:
                    for i in range(len(bateau)):
                        grille_bateaux[ligne +i][colonne] = bateau[i]
                except IndexError:
                    message_hors_grille()

            if joueur == "j1":
                afficher_grille_bateaux_j1()
            elif joueur == "j2":
                afficher_grille_bateaux_j2()

#-------------------- 4. Commencer la partie, demander aux joueurs entrer une coordonnée --------------------

def placement_tirs(grille_tirs, grille_bateaux, colonne, ligne):
    """Petite Fonction fonctionnant avec la fonction tirs_sur_grilles, évite de répéter le remplissage de cases."""
    # Cette fonction n'est pas terminée et en phase de testé
    if grille_bateaux[ligne][colonne] == "~~":
        grille_tirs[ligne][colonne] = "}{"
        grille_bateaux[ligne][colonne] = "}{"
        print("TIR MANQUÉ 🌊")
    elif (grille_bateaux[ligne][colonne] == "To" or
          grille_bateaux[ligne][colonne] == "C1" or
          grille_bateaux[ligne][colonne] == "C2" or
          grille_bateaux[ligne][colonne] == "Cu" or
          grille_bateaux[ligne][colonne] == "PA"):
        grille_tirs[ligne][colonne] = "()"
        grille_bateaux[ligne][colonne] = "()"
        print("TIR TOUCHÉ 💥")

def message_tirs_sur_tirs():
    """petite fonction pour pouvoir modifier la réponse quand un tir et tirer sur un tir (évite de modifier 12x)."""
    print("VOUS AVEZ DÉJÀ TIRER ICI, RÉESSAYER. ⚠️")

def demande_coordonnee(joueur):
    """Fonction qui permet de tirer sur la grille de tirs des joueurs, en entrant une coordonnée (exemple J,10).
    Si le joueur touche un bateau ennemi : Marque une explosion sur la grille de tir j1 et sur grille bateaux j2.
    Si le joueur fait un tir nul et rate : Marque un tir nul sur la grille de tir du j1 et sur grille bateaux j1.
    Une fois le tir fait, c'est le tour de l'autre joueur et s'arrête quand tous les bateaux sont détruits.
    FONCTION FAITE PAR LAMARANA SOW."""
    if joueur == "Joueur1":
        grille_tirs = grille_tirs_j1
    elif joueur == "Joueur2":
        grille_tirs = grille_tirs_j2
    # J'ai inversé ici, parce qu'un tir dans grille_tirs doit apparaitre dans la grille_bateaux opposée adverse.
    if joueur == "Joueur1":
        grille_bateaux = grille_bateaux_j2
    elif joueur == "Joueur2":
        grille_bateaux = grille_bateaux_j1

    # J'ai utilisé un dictionnaire, car c'est plus efficace que d'utiliser des fonctions "if" pour chaque lettre.
    lettre_colonne = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}
    while True:
        reponse = input(f"{joueur}, veuillez entrez une coordonnée pour tirer sur la grille (exemple J,10): ")
        try:
    # La réponse du joueur est séparée pour identifier la ligne et la colonne du tir. J'ai trouvé ".split" ici :
    # https://www.w3schools.com/python/ref_string_split.asp La coordonnée est une liste à deux éléments.
            if str and "," in reponse:
                coordonnee = reponse.split(",")
                print(coordonnee)
                ligne = int(coordonnee[1])
                if 1 <= ligne <=10:
                    colonne = str.upper(coordonnee[0])
                    if colonne in lettre_colonne.keys():
                        colonne = int(lettre_colonne[colonne])
                        # Si le tir a été placé sur une cse de tir "}{" ou "()":
                        #   - Affichez un message d'erreur et redemander la coordonnée.
                        if (grille_bateaux[ligne][colonne] == "}{" or
                            grille_bateaux[ligne][colonne] == "()"):
                            message_tirs_sur_tirs()
                        else:
                            placement_tirs(grille_tirs, grille_bateaux, colonne, ligne)
                            break
                    else:
                        print("Veuillez écrire une lettre de A à J pour tirer dans la grille. ⚠️")
                else:
                    print("Veuillez écrire un chiffre de 1 à 10 pour tirer dans la grille. ⚠️")
        except KeyError or ValueError or IndexError:
            print("Veuillez écrire une lettre de A à J, une virgule et un chiffre de 1 à 10. ⚠️")

    # Affichez les grilles de tirs pour que les joueurs comprennent où ils ont tirés.
    if joueur == "Joueur1":
        afficher_grille_tirs_j1()
    elif joueur == "Joueur2":
        afficher_grille_tirs_j2()

#-------------------- 5. Quand la partie est terminé, un message de victoire est affiché. --------------------

print("I====I PHASE DES PLACEMENT  I====I")
placement_bateaux("j1")
#placement_bateaux("j2")

print("I=======I PHASE DES TIRS I=======I")
while True:
    #demande_coordonnee("Joueur1")
    demande_coordonnee("Joueur2")


"""
"To" in grille_bateaux_j1 or "To" in grille_bateaux_j2 or
"C1" in grille_bateaux_j1 or "C1" in grille_bateaux_j2 or
"C2" in grille_bateaux_j1 or "C2" in grille_bateaux_j2 or
"Cu" in grille_bateaux_j1 or "Cu" in grille_bateaux_j2 or
"PA" in grille_bateaux_j1 or "PA" in grille_bateaux_j2
"""

#ERREUR REMARQUER
#Dans la fonction def placement_bateau :
#   - Quand un bateau passe au dessus un autre bateau, les cases de l'ancien bateau se fait remplacer par une vague et
#   se fait effacer. Il faut trouver une façon de sauvegarder : peut-être faire une copie avant le prochain placement
#   Ou bloquer le mouvement ou permettre de passer au dessus en gardant l'élément du bateau en dessous.

#Dans la fonction def demande_coordonnée :
#   - Ne s'arrête pas encore lorsque que les bateaux sont tous détruits.