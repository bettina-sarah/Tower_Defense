import Modele as mod
import Vue as vue


class Controleur():
    def __init__(self):
        self.modele = mod.Modele(self)
        self.vue = vue.Vue(self, self.modele)
        self.vue.root.mainloop()

    def commencer_partie(self):
        if self.modele.enVie:  # while infini sinon rien pour l'arreter
            if not self.modele.chronoStarted:
                print("commencer partie - chrono")
                self.start_chrono()
            #self.animer_jeu()

        else:  # si pas en vie
            self.start_new_game()

    def start_chrono(self):
        self.modele.chronoStarted = True
        if self.modele.chrono >= 0:
            self.vue.afficherChrono(self.modele.chrono)
            print("mode start chrono & chrono value", self.modele.chrono)
            self.modele.chrono -= 1
            self.vue.root.after(1000, self.start_chrono)

        else:
            self.modele.chronoStarted = False
            self.modele.chrono = 10
            # self.vue.root.after_cancel(self.startChrono)
            # chronostarted devient false... donc startchrono est pas rappelé




    def animer_jeu(self):
        #creer creeps & deplacement
        #vue affiche creeps
        if self.modele.enVie:
            self.vue.root.after(50, self.animer_jeu)
        else:
            #gameover() ou new game ...
            pass




    def start_new_game(self):
        # demande au user si new game ou non Y/N
        pass


if __name__ == "__main__":
    c = Controleur()
