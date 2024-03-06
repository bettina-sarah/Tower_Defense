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
        self.pos_chateau = None
        self.nbCreeps = 20
        self.creeps_inactifs = []
        self.creeps_actifs = []

    def commencer_partie(self):
        pass



