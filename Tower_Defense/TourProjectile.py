from Projectile import *

class TourProjectile:
    def __init__(self, x, y, modele, niveau, couleur="dark violet"):
        self.modele = modele
        self.x = x
        self.y = y
        self.niveau = niveau # 1 2 ou 3
        self.couleur = couleur
        self.rayon = 100
        self.dommage = 10 * self.niveau
        self.cout = 100 * self.niveau
        self.projectiles = []  # gere balle lente, balle rapide, grenade


    def verifier_collision_creep(self):
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