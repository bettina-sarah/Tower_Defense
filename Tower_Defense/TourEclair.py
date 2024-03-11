from Eclair import *

class TourEclair:
    def __init__(self, x, y, modele, niveau, couleur="DarkGoldenrod2"):
        self.modele = modele
        self.x = x
        self.y = y
        self.niveau = niveau # 1 2 ou 3
        self.couleur = couleur
        self.rayon = 120 #rayon diff de projectile
        self.dommage = 12 * self.niveau
        self.cout = 180 * self.niveau
        self.projectiles = []  # gere acide lent, acide rapide, acide forte


    def verifier_collision_creep(self):
        #if self.niveau = 2 ou 3 .. faire un laser
        # niveau 2: red2
        # niveau 3: red4
        pass

    def tirer(self):
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