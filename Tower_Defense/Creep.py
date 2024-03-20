import Modele

class Creep():
    def __init__(self, modele, vague, id):
        # Les points de vie et la vitesse dépendent du niveau donc initialiser dans le Modèle
        # La couleur, la liste de poison et le statut peuvent être initialisés tout de suite.
        self.modele = modele
        self.enVie = True
        self.id = id
        self.couleur = "red3"
        self.dommage = 0
        self.pointsDeVie = 20 * vague
        self.vitesse = 10 * vague
        self.listePoison = []
        self.troncon = 0
        self.posX, self.posY = self.modele.chemin[self.troncon][0]
        self.cibleDebut, self.cibleFin = self.modele.chemin[self.troncon][0], self.modele.chemin[self.troncon][1]



    def hit_creep(self):
        pass


    def check_en_vie(self):
        pass
