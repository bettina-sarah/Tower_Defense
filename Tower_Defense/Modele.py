import os.path
import random
import math

import time
# import Creeps as Creeps
from Creep import Creep
from datetime import datetime
from Tour import *


class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.chronoMax = 60
        self.chrono = 0
        self.enVie = True
        # self.chrono = 2  # a remettre a 10
        self.argent = 500
        self.nbVies = 2000
        self.vague = 0
        # Chemin fait en ligne au lieu de rectangle
        self.chemin = {
            0: [(165, 0), (165, 495)],
            1: [(165, 495), (363, 495)],
            2: [(363, 495), (363, 132)],
            3: [(363, 132), (924, 132)],
            4: [(924, 132), (924, 297)],
            5: [(924, 297), (627, 297)],
            6: [(627, 297), (627, 495)],
            7: [(627, 495), (924, 495)],
        }
        self.troncon_couleur = "sienna3"
        self.chateau_couleur = "DarkOrchid4"
        self.cout_tours = {
            "Projectile_1": 100,
            "Projectile_2": 150,
            "Projectile_3": 200,
            "Eclair_1": 120,
            "Eclair_2": 180,
            "Eclair_3": 240,
            "Poison_1": 150,
            "Poison_2": 190,
            "Poison_3": 230,
        }
        self.nbCreeps = 20 #PROBLEME LES 2 PREMIERS CREEPS SONT CRÉES EN MEME TEMPS
        self.creeps_inactifs = []
        self.creeps_actifs = []
        self.tours = []
        self.variable_test = 5
        self.delai_spawn_time = 0
        self.delai_spawn_time_max = 10


    def jouer_prochain_coup(self):
        # tester si on a un niveau en cours
        if self.creeps_actifs or self.creeps_inactifs:
            if self.creeps_inactifs and self.delai_spawn_time < 1:
                self.spawn_creep()
                self.delai_spawn_time = self.delai_spawn_time_max
            else:
                self.delai_spawn_time -= 1
        else:
            if self.chrono < 1:
                self.chrono = self.chronoMax
            else:
                self.chrono -= 1
                if self.chrono == 0:
                    self.creer_niveau()
        for i in self.creeps_actifs:
            i.jouer_coup()

        for i in self.tours:
            i.jouer_prochain_coup()


    def reinitialiser_modele(self):
        self.chronoStarted = False
        self.enVie = True
        self.chrono = 2
        self.nbVies = 20
        self.nbCreeps = 20  # PROBLEME LES 2 PREMIERS CREEPS SONT CRÉES EN MEME TEMPS
        self.creeps_inactifs = []
        self.creeps_actifs = []

    # Méthode Création des Creeps pour le niveau
    def creer_niveau(self):
        self.vague += 1
        for i in range(self.nbCreeps):
            c = Creep(self, self.vague, i)
            self.creeps_inactifs.append(c)

    def spawn_creep(self):  # pop de creep inactif et append dans creep actif
        if len(self.creeps_inactifs) > 0:
            self.creeps_actifs.append(self.creeps_inactifs.pop())
            # self.parent.vue.afficher_creeps()
        # self.parent.vue.root.after(1500, self.spawn_creep)


    # Méthode pour supprimer les creeps
    def suppression_creeps(self, ID):

        # Passe a travers les creeps actifs
        for creeps in self.creeps_actifs:

            # Prends le bon creep en utilisant le ID
            if ID == creeps.id:
                # Supprime
                self.creeps_actifs.remove(creeps)


    def verifier_collision_tours(self):
        if len(self.tours) > 0:
            for tour in self.tours:
                for creep in self.creeps_actifs:
                    tour.jouer_coup( )

    def creer_tours(self, x, y, niveau, type):  # coordos = x & y
        # appelé par le deposement d'une tour sur le canvas dans Vue
        # unpack les coordos:
        cle_cout_tour = type + "_" + str(niveau)
        t = Tour(self, type, x, y, niveau)
        self.tours.append(t)
        self.argent -= self.cout_tours[cle_cout_tour]
        self.parent.tour_a_creer(t)

        print("Tour ajout")

    def hit_chateau(self, creep):
        self.suppression_creeps(creep.id)
        self.nbVies -= 1

        print(self.nbVies)
        # changer la vie dans la vue?

    def amelioration_tours(self, id):
        # Méthode pour améliorer le niveau de la tour
        for tour in self.tours:
            if tour == id:
                if tour.niveau <= 3:
                    tour.niveau += 1

    def distance_pts(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
