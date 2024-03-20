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
        self.variable_test = 5




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
            # Si le creep n'a pas atteint la fin du chemin
            if creep.troncon < len(self.chemin) - 1:
                # Vérifier si le creep est arrivé à la cible actuelle
                if (creep.posX, creep.posY) == creep.cibleFin:
                    creep.troncon += 1  # Passer au tronçon suivant
                    creep.cibleDebut, creep.cibleFin = self.chemin[creep.troncon][0], self.chemin[creep.troncon][1]

            # Déterminer la direction du déplacement
            dx = creep.cibleFin[0] - creep.posX
            dy = creep.cibleFin[1] - creep.posY

            # Déplacer le creep dans la direction appropriée
            if dx > 0:
                creep.posX += min(dx, creep.vitesse)
            elif dx < 0:
                creep.posX += max(dx, -creep.vitesse)

            if dy > 0:
                creep.posY += min(dy, creep.vitesse)
            elif dy < 0:
                creep.posY += max(dy, -creep.vitesse)

            if creep.troncon == len(self.chemin) - 1 and (creep.posX, creep.posY) == creep.cibleFin:
                self.suppression_creeps(creep.id)
                self.nbVies -= 1
                print(self.nbVies)

    #Méthode pour supprimer les creeps
    def suppression_creeps(self, ID):
        for creeps in self.creeps_actifs:
            if ID == creeps.id:
                self.creeps_actifs.remove(creeps)


    def verifier_collision_tours(self):
        for tour in self.tours:
            for creep in self.creeps_actifs:
                tour.verifier_collision_creep(creep)

    def creer_tours(self, type, niveau, coordos):       #coordos = x & y
        # appelé par le deposement d'une tour sur le canvas dans Vue
        #unpack les coordos:
        x, y = coordos
        t = Tour(self, type, x, y, niveau)
        self.tours.append(t)













