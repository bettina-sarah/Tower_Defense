from Eclair import *
from Poison import *
from Projectile import *
import time

class Tour:
    def __init__(self, modele, type, x, y, niveau):
        self.modele = modele
        self.type = type
        self.delais_tir = 0
        self.delais_tir_max = 100
        self.x = x
        self.y = y
        self.amelioration = niveau # 1 2 ou 3
        #self.id_tour = 1
        self.ID = len(self.modele.tours)
        self.ammo = []  # gere acide lent, acide rapide, acide forte
        self.cible = None #Liste des creeps dans le range

        if self.type == "Projectile":
            self.couleur = "dark violet"
            self.rayon = 100

            self.cout = 100 * self.amelioration

            self.taille = 100
        elif self.type == "Eclair":
            self.couleur = "DarkGoldenrod2"
            self.rayon = 120

            self.cout = 120 * self.amelioration

            self.taille = 120
        elif self.type == "Poison":
            self.couleur = "lime green"
            self.rayon = 150

            self.taille = 150

    def jouer_prochain_coup(self):
        pass
        # si projectile ou poison et si je suis pret a tirer.
    def verifier_collision_creep(self, creep):

            self.cout = 150 * self.amelioration
            self.taille = 150




    def tirer(self, type, niveau, creep):
        #Verifie le type et niveau de la tour en question et créer un projectile
        if type == 'Eclair' and niveau == 1 and len(self.ammo) > 0 :
            #Création Éclair
            e = self.create_Eclair(niveau)
            #rajout dans la liste des projectiles
            self.ammo.append(e)
            #PROBLEME : DOIT SEULEMENT VISÉ UN CREEP A LA FOIS
            e.cibler_creep(creep)
            print("shoot " + str(creep.id))



    #Amélioration_tours transférer dans modele
    # def amelioration_tours(self):
    #     # Méthode pour améliorer le niveau de la tour
    #     if self.niveau < 3:
    #         self.niveau += 1

    def create_Eclair(self, niveau):
        return Eclair(self.modele, self.x, self.y)

    def jouer_coup(self):
        if self.delais_tir == 0:
            creep_cible = self.trouver_cible()
            if creep_cible:
                if self.type == "Projectile":
                    if self.amelioration == 1:
                        p = Projectile(self, creep_cible)
                        self.ammo.append(p)
                        self.delais_tir = self.delais_tir_max
                elif self.type == "Eclair":
                    if self.amelioration == 1:
                        e = Eclair(self, creep_cible)
                        self.ammo.append(e)
                        self.delais_tir = self.delais_tir_max
                elif self.type == "Poison":
                    if self.amelioration == 1:
                        ps = Poison(self, creep_cible)
                        self.ammo.append(ps)
                        creep_cible.listePoison.append(ps)
                        self.delais_tir = self.delais_tir_max
                    #AJOUTER LES AUTRES AMÉLIORATION POUR AUTRE PROJECTILES
                #VÉRIFIER AUTRE TYPES
        else:
            self.delais_tir -= 1
        #AVERTIR PROJECTILE COURANT
        for i in self.ammo:
            i.jouer_coup()

    def trouver_cible(self):
        # Vous devez d'abord obtenir la liste des creeps du modèle pour vérifier la portée
        for creep in self.modele.creeps_actifs:
            if self.rayon >= self.modele.distance_pts(creep.posX, creep.posY, self.x, self.y):
                return creep  # Retourner le creep s'il est dans la portée

        return None  # Retourner None si aucun creep n'est dans la portée

