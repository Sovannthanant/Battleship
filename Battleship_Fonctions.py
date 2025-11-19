

#---------------------------------------- FONCTIONS DU BATTLESHIP ----------------------------------------🚢⚙
# En commençant à faire des importations entre les deux fichiers, je suis tombé sur un problème qui arrêtait le
# programme appelé "circular imports". Les importations se fessaient toutes en même temps et ne se comprenaient pas.
# Pour régler ce problème, j'ai placé plusieurs "import" dans les formules définies, ils sont alors exécutés dans un
# ordre. Pour trouver cette solution, j'ai regardé cette vidéo : https://www.youtube.com/watch?v=UnKa_t-M_kM

#-------------------- Fonctions qui permettent de pourvoir les afficher en tant que grille. --------------------
# Celle-ci apporte les listes de listes qui sont entrées dans les fonctions si dessus pour être affichées en tant que
# grille. Ils ne sont pas utilisées dans le fichier principal, mais dans des fonctions définies se trouvant plus bas.


def afficher_grille_bateaux_j1():
    """Fonction qui permet d'afficher la grille des bateaux du joueur 1."""
    print("I=====I BATEAUX DU JOUEUR 1 I=====I")
    from Battleship import grille_bateaux_j1
    for ligne in grille_bateaux_j1:
        print(*ligne)

def afficher_grille_tirs_j1():
    """Fonction qui permet d'afficher la grille des tirs du joueur 1."""
    print("I=======I TIR DU JOUEUR 1 I=======I")
    from Battleship import grille_tirs_j1
    for ligne in grille_tirs_j1:
        print(*ligne)

def afficher_grille_bateaux_j2():
    """Fonction qui permet d'afficher la grille des bateaux du joueur 2."""
    print("I=====I BATEAUX DU JOUEUR 2 I=====I")
    from Battleship import grille_bateaux_j2
    for ligne in grille_bateaux_j2:
        print(*ligne)

def afficher_grille_tirs_j2():
    """Fonction qui permet d'afficher la grille des tirs du joueur 2"""
    print("I=======I TIR DU JOUEUR 2 I=======I")
    from Battleship import grille_tirs_j2
    for ligne in grille_tirs_j2:
        print(*ligne)


#-------------------- 3. Faire Demander aux joueurs de placer leurs bateaux --------------------
# L'importation de grille_bateaux_j1 et de grille_bateaux_j2 permettent leur modification pour contenir les bateaux et
# l'importation de l'ordre de placement permet de placer en ordre: torpilleur > 2 croiseurs > cuirasse > porte-avion.

def message_hors_grille():
    """Une petite fonction qui sert à afficher un message lorsqu'un déplacement va à l'extérieur de la grille, utilisée
    dans la fonction définie placement_bateaux(Joueur)."""
    print("LE DÉPLACEMENT VA HORS DE LA GRILLE. ⚠️")

def message_sur_bateau():
    """Une petite fonction qui sert à afficher un message lorsqu'un déplacement va par dessus un autre bateau, utilisée
    aussi dans la fonction définie placement_bateaux(Joueur)."""
    print("LE DÉPLACEMENT VA SUR UN AUTRE BATEAUX. ⚠️")

def placement_bateaux(joueur):
    """Fonction qui permet de choisir où placer des bateaux la grille en utilisant W,A,S,D pour se déplacer, R
    pour faire une rotation et E pour placer le bateau. Une fois placer, le prochain bateau apparait pour son
    placement. Quand les bateaux sont placés, c'est au tour de l'autre joueur de placer, puis la partie débute.
    FONCTION FAITE PAR VANN SOVANNTHANANT."""
    from Battleship import (grille_bateaux_j1, grille_bateaux_j2, ordre_placement)
    # Cette importation amène un dictionnaire qui contient l'ordre de placement et la liste des cinq bateaux.
    # J'ai réalisé qu'on peut envoyer des variables dans les paramètres des fonctions définies avec ce lien :
    # https://www.w3schools.com/python/gloss_python_function_arguments.asp
    if joueur == "Joueur1":
        grille_bateaux = grille_bateaux_j1
    elif joueur == "Joueur2":
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
            grille_bateaux[ligne][colonne +i] = bateau[i]

        while True:
    # Avant de demander au joueur de placer les bateaux, la grille est affiché pour faciliter la tâche.
            if joueur == "Joueur1":
                afficher_grille_bateaux_j1()
            elif joueur == "Joueur2":
                afficher_grille_bateaux_j2()
            reponse = str.upper(input("Appuyer W,A,S,D pour déplacer, R\npour tourner et E pour placer: "))
    # Avant le déplacement du bateau, les cases bateau sont effacées pour éviter d'avoir une copie du bateau.
            if horizontal:
                for i in range(len(bateau)):
                    grille_bateaux[ligne][colonne +i] = "~~"
            elif not horizontal:
                for i in range(len(bateau)):
                    grille_bateaux[ligne +i][colonne] = "~~"

    # Les touches "W" et "S" permettent des déplacements vertical, donc les bateaux se déplacent sur ligne.
            if reponse == "W":
                if ligne > 1 and grille_bateaux[ligne -1][colonne] not in ("To","C1","C2","Cu","PA"):
                    ligne -= 1
                elif ligne == 1:
                    message_hors_grille()
                elif grille_bateaux[ligne -1][colonne] in ("To","C1","C2","Cu","PA"):
                    message_sur_bateau()
            elif reponse == "S":
                if ligne <10 and grille_bateaux[ligne +1][colonne] not in ("To","C1","C2","Cu","PA"):
                    ligne += 1
                elif ligne == 10 and (not horizontal + len(bateau) <10):
                    message_hors_grille()
                elif grille_bateaux[ligne +1][colonne] in ("To","C1","C2","Cu","PA"):
                    message_sur_bateau()
    # Les touches "A" et "D" permettent des déplacements horizontal, les bateaux se déplacent sur colonne.
            elif reponse == "A":
                if colonne > 1 and grille_bateaux[ligne][colonne -1] not in ("To","C1","C2","Cu","PA"):
                    colonne -= 1
                elif colonne == 1:
                    message_hors_grille()
                elif grille_bateaux[ligne][colonne -1] in ("To","C1","C2","Cu","PA"):
                    message_sur_bateau()
    # Si colonne + len(bateau) -1 < 10 OU colonne <10 et pas horizontal (peut maintenant aller à droite de la grille).
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
                try:
                    if (horizontal and
                        grille_bateaux[ligne +1][colonne] in ("To","C1","C2","Cu","PA") or
                        grille_bateaux[ligne -1][colonne] in ("To","C1","C2","Cu","PA") or
                        grille_bateaux[ligne][colonne +len(bateau)] in ("To","C1","C2","Cu","PA") or
                        grille_bateaux[ligne][colonne -1] in ("To","C1","C2","Cu","PA")):
                            print("Il doit avoir une espace de une case entre les bateaux.")
                            nombre_bateaux -= 1
        # Une condition if expérimental, pour voir si je peux garder une distance d'un case entre les bateaux.
                    elif horizontal:
                        for i in range(len(bateau)):
                            grille_bateaux[ligne][colonne + i] = bateau[i]
                    elif not horizontal:
                        for i in range(len(bateau)):
                            grille_bateaux[ligne +i][colonne] = bateau[i]
                except IndexError:
                    print("Hors d'la liste.")
                    nombre_bateaux -= 1
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

        if joueur == "Joueur1" and nombre_bateaux == 5:
            return grille_bateaux
        elif joueur == "Joueur2" and nombre_bateaux == 5:
            return grille_bateaux

#-------------------- 4. Commencer la partie, demander aux joueurs entrer une coordonnée --------------------
# Les grille_bateaux_j1, grille_bateaux_j2, grille_tirs_j1 et grille_tirs_j2 sont importées pour pouvoir marquer les
# marque de tirs touchés et tirs nuls.

def placement_tirs(grille_tirs, grille_bateaux, colonne, ligne):
    """Petite Fonction fonctionnant avec la fonction tirs_sur_grilles, évite de répéter le remplissage de cases."""
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
    from Battleship import (grille_tirs_j1, grille_tirs_j2, grille_bateaux_j1, grille_bateaux_j2)
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

    if joueur == "Joueur1":
        afficher_grille_tirs_j1()
    elif joueur == "Joueur2":
        afficher_grille_tirs_j2()

    while True:
        reponse = input(f"{joueur}, Entrez une coordonnée pour\ntirer sur la grille (exemple J,10): ")
    # La réponse du joueur est séparée pour identifier la ligne et la colonne du tir. J'ai trouvé ".split" ici :
    # https://www.w3schools.com/python/ref_string_split.asp La coordonnée est une liste à deux éléments.
        if str and "," in reponse:
            coordonnee = reponse.split(",")
            try:
                print(coordonnee)
                ligne = int(coordonnee[1])
                if 1<= ligne <= 10:
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
    # Des messages pour signaler au joueur comment écrire une bonne coordonnée, couvre toutes les erreurs.
                    else:
                        print("Veuillez entrez une lettre de A à J pour tirer dans la grille. ⚠️")
                else:
                    print("Veuillez entrez un chiffre de 1 à 10 pour tirer dans la grille. ⚠️")
            except ValueError or IndexError or TypeError:
                print("Écrivez un lettre de A à J, une virgule et et un chiffre de 1 à 10. ⚠️")
        else:
            print("Écrivez un lettre de A à J, une virgule et et un chiffre de 1 à 10. ⚠️")

    # Affichez les grilles de tirs pour que les joueurs comprennent où ils ont tirés.
    if joueur == "Joueur1":
        afficher_grille_tirs_j1()
    elif joueur == "Joueur2":
        afficher_grille_tirs_j2()


#-------------------- +. Fonctions décoratives, pas nécessaire au fonctionnement.  --------------------
import time
import sys

ecran_accueil = [
    ["I=======I JEU BATTLESHIP  I=======I"],
    ["                                   "],
    ["            _+_  //  //            "],
    ["     =--=/I-I_____I_I---I-I\\=--= "],
    ["\\_°°°°°_°°°°°_____________________/"],
    ["~~ ~~ ~~ ~~ ~~ -- -- -- -- -- -- --"],
]
def affichage_ecran_accueil():
    for ligne in ecran_accueil:
        print(*ligne)

# J'ai appris les ANSI Escape Codes dans ce lien. Je l'ai enlevé des fichiers :
# https://vascosim.medium.com/how-to-print-colored-text-in-python-52f6244e2e30

# J'ai appris à faire des textes clignotants en consultant ce site, j'ai modifié les params :
# https://handhikayp.medium.com/generate-a-blinking-text-with-very-simple-python-4c10750978f5
def texte_clignotant(texte,secondes):
    compteur = 0
    while compteur <= secondes:
        sys.stdout.write(texte)
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write('\r' + ' ' * len(texte)+'\r')
        sys.stdout.flush()
        time.sleep(0.5)
        compteur += 1