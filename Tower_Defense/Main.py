import Modele as mod
import Vue as vue


class Controleur():
    def __init__(self):
        self.modele = mod.Modele(self)
        self.vue = vue.Vue(self, self.modele)

        self.vue.root.mainloop()





if (__name__ == "__main__"):
    c = Controleur()