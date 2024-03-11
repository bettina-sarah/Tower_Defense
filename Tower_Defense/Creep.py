import Modele

class Creep():
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
        self.posX = None
        self.posY = None
        self.cibleX = None
        self.cibleY = None
        self.troncon = None

    def afficher_Creeps(self):
        pass

    def hit_creep(self):
        pass

    def deplacer(self):
        for creep in self.modele.creeps_actifs:
            if creep.pos == self.cible:
                self.troncon += 1
                self.cible = self.modele.chemin[self.troncon]
            if creep.troncon == 0:
                    creep.posY += 1
            elif creep.troncon == 1:
                    creep.posX += 1
            elif creep.troncon == 2:
                    creep.posY -= 1
            elif creep.troncon == 3:
                    creep.posX += 1
            elif creep.troncon == 4:
                    creep.posY += 1
            elif creep.troncon == 5:
                    creep.posX -= 1
            elif creep.troncon == 6:
                    creep.posY += 1
            elif creep.troncon == 7:
                    creep.posX += 1






    def check_en_vie(self):
        pass

    def hit_chateau(self):
        pass