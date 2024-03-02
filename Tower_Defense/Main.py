import Modele as mod
import Vue as vue


class Controleur():
    def __init__(self):
        self.modele = mod.Modele(self)
        self.vue = vue.Vue(self, self.modele)

        self.vue.root.mainloop()
        self.commencer_partie()

    def commencer_partie(self):
        while self.modele.enVie:
            if (self.modele.chronoStarted == False):
                self.modele.startChrono()





if (__name__ == "__main__"):
    c = Controleur()