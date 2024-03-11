from Eclair import *
from Poison import *
from Projectile import *

class Tour:
    def __init__(self, modele, type, x, y, niveau, ID):
        self.modele = modele
        self.type = type
        self.x = x
        self.y = y
        self.niveau = niveau # 1 2 ou 3
        self.ID = ID
        self.projectiles = []  # gere acide lent, acide rapide, acide forte

        if self.type == "TourProjectile":
            self.couleur = "dark violet"
            self.rayon = 100
            self.cout = 100 * self.niveau
            self.taille = 100
        elif self.type == "TourEclair":
            self.couleur = "DarkGoldenrod2"
            self.rayon = 120
            self.cout = 120 * self.niveau
            self.taille = 120
        elif self.type == "TourPoison":
            self.couleur = "lime green"
            self.rayon = 150
            self.cout = 150 * self.niveau
            self.taille = 150


    def verifier_collision_creep(self, creep):
        # if self.rayon ==
        #if self.niveau = 2 ou 3 .. faire un laser
        # niveau 2: red2
        # niveau 3: red4
        pass

    def tirer(self):
        pass

    def amelioration_tours(self):
        pass





    # def create_projectile(self, target_x, target_y):
    #     # Créer un projectile en fonction du type de la tour
    #     return Projectile(self.x, self.y, target_x, target_y, self.damage, self.level, self.type)
    #
    # def upgrade(self):
    #     # Méthode pour améliorer la tour
    #     if self.level < 3:
    #         self.level += 1
    #         # Augmenter les caractéristiques de la tour en fonction du niveau
    #         # (par exemple, augmenter les dégâts, la portée, etc.)
    #         self.damage *= 1.5
    #         self.range *= 1.2
    #         self.upgrade_cost *= 1.5