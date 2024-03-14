import Modele

class Creep():
    def __init__(self, modele, vague, id):
#Les points de vie et la vitesse dépendent du niveau donc initialiser dans le Modèle
#La couleur, la liste de poison et le statut peuvent être initialisé tout de suite.
        self.modele = modele
        self.enVie = True
        self.id = id
        self.couleur = "red3"
        self.dommage = 0
        self.pointsDeVie = 20 * vague
        self.vitesse = 2 * vague
        self.listePoison = []
        self.troncon = 0
        self.posX, self.posY = self.modele.chemin[self.troncon][0]
        self.cibleX, self.cibleY = self.modele.chemin[self.troncon][1]

    def hit_creep(self):
        pass

    def deplacer(self): #marche pour troncon 0
        for creep in self.modele.creeps_actifs:
            print("creep pos x et y:", self.posX, self.posY)
            # ?? creep.pos == self.cible
            creep.pos = self.posX, self.posY
            self.cible = self.cibleX, self.cibleY
            if creep.pos == self.cible: # si cible atteinte, changer troncon & assigner nouvelle cible
                self.troncon += 1
                self.cible = self.modele.chemin[self.troncon][1]   # 0: [(165, 0),   (165, 495)]

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