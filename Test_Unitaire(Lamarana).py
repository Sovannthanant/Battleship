#------------------ TESTS DU BATTLESHIP ----------------------------------------

import pytest
import Battleship
import Battleship_Fonctions

from Battleship_Fonctions import (
    afficher_grille_bateaux_j1,
    afficher_grille_bateaux_j2,
    afficher_grille_tirs_j1,
    afficher_grille_tirs_j2,
    message_hors_grille,
)

def _formater_grille(grille):
    return "\n".join(" ".join(ligne) for ligne in grille) + "\n"


# -------------------- Test 1 : afficher_grille_bateaux_j1 --------------------

def test_afficher_grille_bateaux_j1(capsys):                #capute le système(fonction)
    Battleship.grille_bateaux_j1 = [
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

    # Appel de la fonction (qui fait print)
    afficher_grille_bateaux_j1()

    captured = capsys.readouterr()                   #méthode de pytest
    resultat = captured.out

    sortie_attendue = (
        "I=====I BATEAUX DU JOUEUR 1 I=====I\n"
        +_formater_grille(Battleship.grille_bateaux_j1)
    )

    assert resultat == sortie_attendue


# -------------------- Test 2 : afficher_grille_tirs_j1 --------------------

def test_afficher_grille_tirs_j1(capsys):
    Battleship.grille_tirs_j1 = [
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

    afficher_grille_tirs_j1()
    captured = capsys.readouterr()                     #capsys.readouterr() capture tout ce qu’une fonction a affiché avec print()

                                                       #afin de pouvoir le tester avec pytest, même si la fonction ne retourne rien.
    resultat = captured.out                            #https://docs.pytest.org/en/stable/how-to/capture-stdout-stderr.html

    sortie_attendue = (
    "I=======I TIR DU JOUEUR 1 I=======I\n"
    + _formater_grille(Battleship.grille_tirs_j1)
    )

    assert resultat == sortie_attendue


# -------------------- Test 3 : afficher_grille_bateaux_j2 --------------------
def test_afficher_grille_bateaux_j2(capsys):
    Battleship.grille_bateaux_j2 = [
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

    afficher_grille_bateaux_j2()
    captured = capsys.readouterr()
    resultat = captured.out

    sortie_attendue = (
        "I=====I BATEAUX DU JOUEUR 2 I=====I\n"
        + _formater_grille(Battleship.grille_bateaux_j2)
    )

    assert resultat == sortie_attendue


# -------------------- Test 4 : afficher_grille_tirs_j2 --------------------

def test_afficher_grille_tirs_j2(capsys):
    Battleship.grille_tirs_j2 = [
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

    afficher_grille_tirs_j2()
    captured = capsys.readouterr()                        #capture la sortie  dans la console puisque la fonction utilise un print()
    resultat = captured.out

    sortie_attendue = (
        "I=======I TIR DU JOUEUR 2 I=======I\n"
        + _formater_grille(Battleship.grille_tirs_j2)
    )

    assert resultat == sortie_attendue


# -------------------- Test message_hors_grille --------------------

def test_message_hors_grille(capsys):
    message_hors_grille()

    captured = capsys.readouterr()
    resultat = captured.out

    assert resultat == "LE DÉPLACEMENT VA HORS DE LA GRILLE. ⚠️\n"


# -------------------- Tests placement_tirs --------------------
 #chaque donnée sera testée une par une par le fonction( test_placement_tirs)
@pytest.mark.parametrize("etat_initial, message_attendu, marqueur_attendu", [                   #Organisation des données
    ("~~", "TIR MANQUÉ", "}{"), #Le seul qui ne sera pas touché(donnée)
    ("To", "TIR TOUCHÉ", "()"), #Torpilleur
    ("C1", "TIR TOUCHÉ", "()"), #Croiseur(1)
    ("C2", "TIR TOUCHÉ", "()"), #Croisseur(2)
    ("Cu", "TIR TOUCHÉ", "()"), #Cuirassé
    ("PA", "TIR TOUCHÉ", "()"), #Porte-avion


])
def test_placement_tirs(etat_initial, message_attendu, marqueur_attendu, capsys):
    #initialissation des grilles pour le test
    grille_tirs = [["~", "~"], ["~", "~~"]]
    grille_bateaux = [["~", "~"], ["~", etat_initial]]
    # Appel de la fonction à tester pour placer un tir
    Battleship_Fonctions.placement_tirs(
        grille_tirs, grille_bateaux, colonne=1, ligne=1
    )

    captured = capsys.readouterr()          #la méthode(# Lit la sortie standard et la sortie d'erreur)
    resultat = captured.out  #Récupère uniquement la sortie standard (ce qui a été print

    assert message_attendu in resultat
    assert grille_tirs[1][1] == marqueur_attendu    # Vérifie que la grille des tirs a été correctement mise à jour
    assert grille_bateaux[1][1] == marqueur_attendu   # Vérifie que la grille des bateaux a été correctement mise à jour
