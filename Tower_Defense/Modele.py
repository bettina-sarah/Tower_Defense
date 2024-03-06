import os.path
import random

import time
from datetime import datetime


class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.chronoStarted = False
        self.enVie = True
        self.chrono = 10
        self.argent = 200
        self.nbVies = 20
        self.vague = 1
        self.dict_rect = {      #coordonnées troncons coin haut gauche & bas droite
            'start1': (160, 0), 'end1': (240, 640), # end avec start meme coordo?
            'start2': (240, 560), 'end2': (480, 640),
            'start3': (400, 120), 'end3': (480, 560),
            'start4': (480, 120), 'end4': (1160, 270),
            'start5': (280, 280), 'end5': (340, 340),
            'start6': (350, 350), 'end6': (410, 410)
        }
        self.troncon_couleur = "sienna3"
        self.chateau_couleur = "DarkOrchid4"
        self.dict_pos_chateau = {
            'coinG': (1080, 480),
            'coinD': (1200, 480),
            'blocHG': (1120, 520),
            'blocHD': (1160, 520),
            'blocMG': (1120, 560),
            'blocMD': (1160, 560),
            'blocBG': (1120, 600),
            'blocBD': (1160, 600),
            'finG': (1120, 520),
            'finD': (1240, 520),
            'finHG': (1160, 560),
            'finHD': (1200, 560),
            'finMG': (1160, 600),
            'finMD': (1200, 600),
            'finBG': (1160, 640),
            'finBD': (1200, 640)
                }
        self.nbCreeps = 20
        self.creeps_inactifs = []
        self.creeps_actifs = []

    def commencer_partie(self):
        pass



