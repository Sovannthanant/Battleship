# ---------------------------------------- TESTS DU BATTLESHIP ----------------------------------------

import pytest     # importer de la librairie pour effectuer les test

import Battleship #importer le fichier Battleship pour pouvoir utiliser ces fonctions
import Battleship_Fonctions #importer le fichier Battleship_Fonctions pour utiliser ces fonction aussi

"""

"""

from Battleship_Fonctions import (
    afficher_grille_bateaux_j1,
    afficher_grille_bateaux_j2,
    afficher_grille_tirs_j1,
    afficher_grille_tirs_j2,
    message_hors_grille,
)

def _formater_grille(grille):
    """Cette fonction return la grille dans un chaine de caractère
    arg:
    grille: prend les 4 grilles comme paramètres
    et a chaque fois que l'on appel notre fonction, on assigne l'un des quatres paramètre qu'il va utiliser



"""
    return "\n".join(" ".join(ligne) for ligne in grille) + "\n"


# -------------------- Test 1 : afficher_grille_bateaux_j1 --------------------

def test_afficher_grille_bateaux_j1():
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

    sortie_attendue = _formater_grille(Battleship.grille_bateaux_j1)

    resultat = afficher_grille_bateaux_j1()

    assert resultat == sortie_attendue


# -------------------- Test 2 : afficher_grille_tirs_j1 --------------------


def test_afficher_grille_tirs_j1():
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

    sortie_attendue = _formater_grille(Battleship.grille_tirs_j1)   #on prepare la sortie atendu( notre objet)

    resultat = afficher_grille_tirs_j1()       # appel de la fonction que l'on veut tester


    assert resultat == sortie_attendue         #vérifie si la valeur retourné par la fonction est exacte


# -------------------- Test 3 : afficher_grille_bateaux_j2 --------------------
# FONCTION QUI VA ME SERVIR DE DEMO
def test_afficher_grille_bateaux_j2():
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

    objet=_formater_grille(Battleship.grille_bateaux_j2)
    resultat=afficher_grille_bateaux_j2()
    assert objet==resultat

"""
    sortie_attendue = _formater_grille(Battleship.grille_bateaux_j2)

    resultat = afficher_grille_bateaux_j2()

    assert resultat == sortie_attendue
"""

# -------------------- Test 4 : afficher_grille_tirs_j2 --------------------
#FONCTION QUI VA ME SERVIR DE DEMO
def test_afficher_grille_tirs_j2():
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

    sortie_attendue = _formater_grille(Battleship.grille_tirs_j2)

    resultat = afficher_grille_tirs_j2()

    assert resultat == sortie_attendue


# -------------------- Test message_hors_grille --------------------

def test_message_hors_grille():
    verifie_message="LE DÉPLACEMENT VA HORS DE LA GRILLE. ⚠️\n"
    assert message_hors_grille() == verifie_message


# -------------------- Tests de placement_tirs --------------------
#Testons plusieurs cas avec la fonction  avec la fonction (test_placement_tirs)
@pytest.mark.parametrize("etat_initial, message_attendu, marqueur_attendu", [                           #/organisation/la clé du programme /
    ("~~", "TIR MANQUÉ", "}{"),
    ("To", "TIR TOUCHÉ", "()"),
    ("C1", "TIR TOUCHÉ", "()"),
    ("C2", "TIR TOUCHÉ", "()"),
    ("Cu", "TIR TOUCHÉ", "()"),
    ("PA", "TIR TOUCHÉ", "()"),
])
def test_placement_tirs(etat_initial, message_attendu, marqueur_attendu):
     #Initialisation

    grille_tirs = [["~", "~"], ["~", "~~"]] #on créer deux grilles minimales ici (2*2)
    grille_bateaux = [["~", "~"], ["~", etat_initial]]

    resultat = Battleship_Fonctions.placement_tirs(
        grille_tirs, grille_bateaux, colonne=1, ligne=1
    )

    assert message_attendu in resultat
    assert grille_tirs[1][1] == marqueur_attendu
    assert grille_bateaux[1][1] == marqueur_attendu
