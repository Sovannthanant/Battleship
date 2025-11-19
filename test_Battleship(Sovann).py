
#---------------------------------------- TESTS DES FONCTIONS DU BATTLESHIP ----------------------------------------⚙🛠
import pytest
#-------------------- Fonctions d'affichage --------------------
from Battleship_Fonctions import (afficher_grille_bateaux_j1, afficher_grille_bateaux_j2,
                                  afficher_grille_tirs_j1, afficher_grille_tirs_j2)

#---------- Act
#---------- Arrange
#---------- Assert
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

#---------- Act
#---------- Arrange
#---------- Assert
def test_message_hors_grille():
    verification = print("LE DÉPLACEMENT VA HORS DE LA GRILLE.")
    assert message_hors_grille() == verification

# J'ai tenter d'utiliser @pytest.mark.markdown, ça n'a pas marcher.
"""@pytest.mark.markdown("input,resultat_attendu"[
    ("w",ligne -= 1),
    ("S",ligne += 1),
    ("A",colonne -= 1),
    ("D",colonne += 1),
    ("r",horizontal = not horizontal),
])
def test_placement_bateaux():
    verification = placement_bateaux(input)
    assert resultat_attendu == verification"""


#-------------------- Fonctions de tirs --------------------
from Battleship_Fonctions import placement_tirs, message_tirs_sur_tirs, demande_coordonnee

#---------- Act
#---------- Arrange
#---------- Assert
# @pytest.mark.markdown, n'a pas fonctionner non plus.
"""@pytest.mark.markdown("case,resultat_attendu"[
    ("~~","TIR MANQUÉ"),
    ("To","TIR TOUCHÉ"),
    ("C1","TIR TOUCHÉ"),
    ("C2","TIR TOUCHÉ"),
    ("Cu","TIR TOUCHÉ"),
    ("PA","TIR TOUCHÉ"),
])
def test_placement_tirs():
    verification = placement_tirs(input)
    assert resultat_attendu = verification"""

def test_message_tirs_sur_tirs():
    verification = print("VOUS AVEZ DÉJÀ TIRER ICI, RÉESSAYER.")
    assert message_tirs_sur_tirs() == verification

# Je ne sais pas comment utiliser @pytest.mark.markdown.
"""@pytest.mark.markdown("input,resultat_attendu"[
    ("E,5",placement_tirs),
    ("E,12",print("Veuillez entrez un chiffre de 1 à 10 pour tirer dans la grille."),
    ("K,5",print("Veuillez entrez une lettre de A à J pour tirer dans la grille."),
    ("BA,11",print("Écrivez un lettre de A à J, une virgule et et un chiffre de 1 à 10. ⚠️"),
])
def test_demande_coordonne():
    verification == demande_coordonnee(input)
    assert resultat_attendu == verification
"""