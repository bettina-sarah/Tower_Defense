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
        self.dict_rect = {      #coordonnées troncons
            'start1': (10, 10), 'end1': (60, 60), # end avec start meme coordo?
            'start2': (70, 70), 'end2': (130, 130),
            'start3': (140, 140), 'end3': (200, 200),
            'start4': (210, 210), 'end4': (270, 270),
            'start5': (280, 280), 'end5': (340, 340),
            'start6': (350, 350), 'end6': (410, 410)
        }
        self.troncon_couleur = "red"
        self.pos_chateau = None
        self.nbCreeps = 20
        self.creeps_inactifs = []
        self.creeps_actifs = []

    def commencer_partie(self):
        pass



