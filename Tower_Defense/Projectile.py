import helper
import math

class Projectile:
    def __init__(self, tour, creep):
        self.parent = tour
        self.departX = tour.x
        self.departY = tour.y
        self.cible = creep
        self.cibleX = creep.posX # ajusté dans cibler creep
        self.cibleY = creep.posY
        self.vitesse = 40
        self.taille = 10
        self.dommage = 10
        self.niveau = tour.amelioration
        self.couleur = "azure4" # a la base niv 1
        self.zone_impact = 10
        self.angle = helper.Helper.calcAngle(self.departX, self.departY, self.cibleX, self.cibleY)

        if self.niveau == 2: # balle rapide
            self.couleur = "MediumPurple4"
            self.vitesse = 70
            self.dommage = 10
            self.taille = 10
            self.cooldown = 2

        elif self.niveau == 3: # grenade : taille grande, vitesse lente,
            self.couleur = "tomato"
            self.vitesse = 80
            self.dommage = 15
            self.taille = 10
            self.cooldown = 50

    def cibler_creep(self):
        # self.cibleX =
        # self.cibleY =
        pass



    def creep_hit(self):
        self.cible.pointsDeVie -= self.dommage
        if self.cible.pointsDeVie <= 0:
            self.cible.EnVie = False
            self.parent.modele.suppression_creeps(self.cible.id)
        print(self.cible.pointsDeVie)

    def jouer_coup(self):
        self.deplacer()
        self.verifier_impact()
        pass

    def deplacer(self):
        self.departX, self.departY = helper.Helper.getAngledPoint(self.angle,self.vitesse,self.departX,self.departY)


    def verifier_impact(self):
        if self.distance_pts(self.departX, self.departY, self.cibleX, self.cibleY) <= self.zone_impact:
            self.creep_hit()

    def distance_pts(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


