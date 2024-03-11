import Modele
from Poison import *

class Creeps():
    def __init__(self, modele, pDV, vitesse, id):
#Les points de vie et la vitesse dépendent du niveau donc initialiser dans le Modèle
#La couleur, la liste de poison et le statut peuvent être initialisé tout de suite.
        self.enVie = True
        self.id = id
        self.couleur = "red3"
        self.dommage = 0
        self.pointsDeVie = pDV
        self.vitesse = vitesse
        self.listePoison = []

    def afficher_Creeps(self):
        pass

    def hit_creep(self):
        pass

    def deplacer(self):
        pass

    def check_en_vie(self):
        pass

    def hit_chateau(self):
        pass