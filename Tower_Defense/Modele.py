import os.path
import random

import time
#import Creeps as Creeps
from Creeps import Creeps
from datetime import datetime

from TourProjectile import *
from TourEclair import *
from TourPoison import *


class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.chronoStarted = False
        self.enVie = True
        self.chrono = 10
        self.argent = 200
        self.nbVies = 20
        self.vague = 1
        # self.dict_rect = {      #coordonnées troncons coin haut gauche & bas droite
        #     'start1': (160, 0), 'end1': (240, 640), # end avec start meme coordo?
        #     'start2': (240, 560), 'end2': (480, 640),
        #     'start3': (400, 120), 'end3': (480, 560),
        #     'start4': (480, 120), 'end4': (1160, 200),
        #     'start5': (1080, 200), 'end5': (1160, 400),
        #     'start6': (720, 320), 'end6': (1080, 400),
        #     'start7': (720, 400), 'end7': (800, 640),
        #     'start8': (800, 560), 'end8': (1120, 640),
        # }
        self.dict_rect = {
              'start1': (132, 0), 'end1': (198, 528),
                'start2': (198, 462), 'end2': (396, 528),
                'start3': (330, 99), 'end3': (396, 462),
                'start4': (396, 99), 'end4': (957, 165),
                'start5': (891, 165), 'end5': (957, 330),
                'start6': (594, 264), 'end6': (891, 330),
                'start7': (594, 330), 'end7': (660, 528),
                'start8': (660, 462), 'end8': (924, 528),
        }

        self.troncon_couleur = "sienna3"
        self.chateau_couleur = "DarkOrchid4"
        # self.dict_pos_chateau = {
        #     'coinG': (1080, 480),
        #     'coinD': (1200, 480),
        #     'blocHG': (1120, 520),
        #     'blocHD': (1160, 520),
        #     'blocMG': (1120, 560),
        #     'blocMD': (1160, 560),
        #     'blocBG': (1120, 600),
        #     'blocBD': (1160, 600),
        #     'finG': (1120, 520),
        #     'finD': (1240, 520),
        #     'finHG': (1160, 560),
        #     'finHD': (1200, 560),
        #     'finMG': (1160, 600),
        #     'finMD': (1200, 600),
        #     'finBG': (1160, 640),
        #     'finBD': (1200, 640)
        #         }


        self.nbCreeps = 20
        self.creeps_inactifs = []
        self.creeps_actifs = []
        self.tours = []
        self.creer_creeps()


    def commencer_niveau(self):
        pass

    # Méthode Création des Creeps pour le niveau
    def creer_creeps(self):
        for i in range(self.nbCreeps):
            v = self.vague *5 #************calcul arbitraire de vitesse, À TESTER******************
            HP = self.vague * 20 #************calcul arbitraire de point de Vie, À TESTER******************
            if i == 10:
                HP = 69
            c = Creeps(self, HP, v, i)
            self.creeps_inactifs.append(c)

#Méthode pour supprimer les creeps
    def suppression_creeps(self, ID):
        for creeps in self.creeps_actifs:
            if ID == creeps.id:
                self.creeps_actifs.remove(creeps)


    def verifier_collision_tours(self):
        for tour in self.tours:
            tour.verifier_collision_creep()

    def creer_tours(self):












