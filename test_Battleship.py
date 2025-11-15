
#---------------------------------------- TESTS DES FONCTIONS DU BATTLESHIP ----------------------------------------⚙🛠
import pytest
#-------------------- Fonctions d'affichage --------------------
from Battleship_Fonctions import (afficher_grille_bateaux_j1, afficher_grille_bateaux_j2,
                                  afficher_grille_tirs_j1, afficher_grille_tirs_j2)
#---------- Act, Arrange, Assert
def test_afficher_grille_bateaux_j1():
    verification = afficher_grille_bateaux_j1()
    assert afficher_grille_bateaux_j1() == verification

def test_afficher_grille_tirs_j1():
    verification = afficher_grille_tirs_j1()
    assert afficher_grille_tirs_j1() == verification

def test_afficher_grille_bateaux_j2():
    verification = afficher_grille_bateaux_j2()
    assert afficher_grille_bateaux_j2() == verification

def test_afficher_grille_tirs_j2():
    verification = afficher_grille_tirs_j2()
    assert afficher_grille_tirs_j2() == verification

#-------------------- Fonctions de placement --------------------
from Battleship_Fonctions import message_hors_grille, placement_bateaux

def test_message_hors_grille():
    verification = print("LE DÉPLACEMENT VA HORS DE LA GRILLE. ⚠️")
    assert message_hors_grille() == verification

