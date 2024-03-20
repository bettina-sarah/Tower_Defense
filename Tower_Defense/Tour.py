from Eclair import *
from Poison import *
from Projectile import *

class Tour:
    def __init__(self, modele, type, x, y, niveau):
        self.modele = modele
        self.type = type
        self.x = x
        self.y = y
        self.niveau = niveau # 1 2 ou 3
        #self.id_tour = 1
        self.ID = len(self.modele.tours)
        self.projectiles = []  # gere acide lent, acide rapide, acide forte

        if self.type == "Projectile":
            self.couleur = "dark violet"
            self.rayon = 100
            self.cout = 100 * self.niveau
            self.taille = 100
        elif self.type == "Eclair":
            self.couleur = "DarkGoldenrod2"
            self.rayon = 120
            self.cout = 120 * self.niveau
            self.taille = 120
        elif self.type == "Poison":
            self.couleur = "lime green"
            self.rayon = 150
            self.cout = 150 * self.niveau
            self.taille = 150


    def verifier_collision_creep(self, creep):
        # if self.rayon ==
        #if self.niveau = 2 ou 3 .. faire un laser
        # niveau 2: red2
        # niveau 3: red4

         #Si la distance entre le creep et la Tour est plus petit que le rayon, la Tour tire
         if self.rayon >= self.modele.distance_pts(creep.posX, creep.posY, self.x, self.y):
            #print("shoot") #Test pour voir si la fonction marche
            self.tirer(self.type, self.niveau, creep)
            print("shoot") #TEST




    def tirer(self, type, niveau, creep):
        #Verifie le type et niveau de la tour en question et créer un projectile
        if type == 'Eclair' and niveau == 1:
            #Création Éclair
            e = self.create_Eclair(niveau)
            #rajout dans la liste des projectiles
            self.projectiles.append(e)
            #PROBLEME : DOIT SEULEMENT VISÉ UN CREEP A LA FOIS
            e.cibler_creep(creep)

            pass




    #Amélioration_tours transférer dans modele
    # def amelioration_tours(self):
    #     # Méthode pour améliorer le niveau de la tour
    #     if self.niveau < 3:
    #         self.niveau += 1

    def create_Eclair(self, niveau):

        return Eclair(self.modele, self.x, self.y)






    #def create_projectile(self, target_x, target_y):
         # Créer un projectile en fonction du type de la tour
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