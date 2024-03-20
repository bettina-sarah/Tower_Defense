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
        self.vitesse = (20 * vague)/1.8
        self.listePoison = []
        self.troncon = 0
        self.posX, self.posY = self.modele.chemin[self.troncon][0]
        self.cibleDebut, self.cibleFin = self.modele.chemin[self.troncon][0], self.modele.chemin[self.troncon][1]


    def jouer_coup(self):
        if self.troncon < len(self.modele.chemin) - 1:
            # Vérifier si le creep est arrivé à la cible actuelle
            if (self.posX, self.posY) == self.cibleFin:
                self.troncon += 1  # Passer au tronçon suivant
                self.cibleDebut, self.cibleFin = self.modele.chemin[self.troncon][0], self.modele.chemin[self.troncon][1]

        # Déterminer la direction du déplacement
        dx = self.cibleFin[0] - self.posX
        dy = self.cibleFin[1] - self.posY

        # Déplacer le creep dans la direction appropriée
        if dx > 0:
            self.posX += min(dx, self.vitesse)
        elif dx < 0:
            self.posX += max(dx, -self.vitesse)

        if dy > 0:
            self.posY += min(dy, self.vitesse)
        elif dy < 0:
            self.posY += max(dy, -self.vitesse)

        if self.troncon == len(self.modele.chemin) - 1 and (self.posX, self.posY) == self.cibleFin:
            self.modele.hit_chateau(self)

    def hit_creep(self):
        pass


    def check_en_vie(self):
        pass
