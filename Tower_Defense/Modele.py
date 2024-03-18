import os.path
import random

import time
#import Creeps as Creeps
from Creep import Creep
from datetime import datetime
from Tour import *

class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.chronoStarted = False
        self.enVie = True
        self.chrono = 2 # a remettre a 10
        self.argent = 200
        self.nbVies = 20
        self.vague = 0
        #Chemin fait en ligne au lieu de rectangle
        self.chemin = {
            0: [(165, 0),   (165, 495)],
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




    # Méthode Création des Creeps pour le niveau
    def creer_niveau(self):
        self.vague += 1
        for i in range(self.nbCreeps):
            c = Creep(self, self.vague, i)
            self.creeps_inactifs.append(c)


    def spawn_creep(self): #pop de creep inactif et append dans creep actif
        if len(self.creeps_inactifs) > 0:

            self.creeps_actifs.append(self.creeps_inactifs.pop())
            # self.parent.vue.afficher_creeps()
        self.parent.vue.root.after(1000, self.spawn_creep)

    def deplacer_creeps(self):
        for creep in self.creeps_actifs:
            if (creep.posX, creep.posY) == (creep.cibleDebut, creep.cibleFin):
                # Changer de tronçon si possible
                if creep.troncon < len(self.modele.chemin) - 1:
                    creep.troncon += 1
                   # si on change de troncon
                    creep.cibleDebut, creep.cibleFin = self.modele.chemin[creep.troncon][1]  # Mettre à jour la cible du creep
                    # on est arriver a la fin

            # Déplacer le creep vers sa cible
            if creep.troncon == 0:
                creep.posY += 10
            elif creep.troncon == 1:
                creep.posX += 10
            elif creep.troncon == 2:
                creep.posY -= 10
            elif creep.troncon == 3:
                creep.posX += 10
            elif creep.troncon == 4:
                creep.posY += 10
            elif creep.troncon == 5:
                creep.posX -= 10
            elif creep.troncon == 6:
                creep.posY += 10
            elif creep.troncon == 7:
                creep.posX += 10



#Méthode pour supprimer les creeps
    def suppression_creeps(self, ID):
        for creeps in self.creeps_actifs:
            if ID == creeps.id:
                self.creeps_actifs.remove(creeps)


    def verifier_collision_tours(self):
        for tour in self.tours:
            for creep in self.creeps_actifs:
                tour.verifier_collision_creep(creep)

    def creer_tours(self, type, niveau, coordos, ID):       #coordos = x & y
        # appelé par le deposement d'une tour sur le canvas dans Vue
        #unpack les coordos:
        x, y = coordos
        t = Tour(self, type, x, y, niveau, ID)
        self.tours.append(t)













