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



    def startChrono(self):
        self.chronoStarted = True
        if self.chrono >= 0:
            self.parent.vue.afficherChrono(self.chrono)
            self.parent.vue.root.after(1000, self.startChrono)
            self.chrono -= 1
        else:
            self.chronoStarted = False
            self.parent.vue.root.after_cancel(self.startChrono)