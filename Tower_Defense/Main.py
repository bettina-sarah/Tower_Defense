import Modele as mod
import Vue as vue


class Controleur():
    def __init__(self):
        self.modele = mod.Modele(self)
        self.vue = vue.Vue(self, self.modele)
        self.vue.root.after(1000, self.commencer_partie)
        self.vue.root.after(2000, self.modele.spawn_creep)
        self.vue.root.mainloop()



    def commencer_partie(self):
        if self.vue:
            if self.modele.enVie:  # while infini sinon rien pour l'arreter
                self.modele.creer_niveau() #cree la vague et creeps inactifs
                if not self.modele.chronoStarted:
                    self.start_chrono()
                    self.changer_vague()
                self.animer_jeu()

        else:  # si pas en vie
            self.start_new_game()

    def start_chrono(self):
        self.modele.chronoStarted = True
        if self.modele.chrono >= 0:
            self.vue.afficherChrono(self.modele.chrono)
            self.modele.chrono -= 1
            self.vue.root.after(1000, self.start_chrono)
        else:
            self.modele.chronoStarted = False
            self.modele.chrono = 10

    def changer_vague(self):
        self.vue.afficher_vague()





    def animer_jeu(self):
        #vue affiche creeps
        if self.modele.enVie:
            if not self.modele.chronoStarted:
                self.modele.deplacer_creeps()
                self.vue.afficher_creeps()
                self.modele.verifier_collision_tours()
                self.update_vie()

            self.vue.root.after(50, self.animer_jeu)
        else:
            self.game_over()

    def creer_tours(self, type, niveau, coordos):
        self.modele.creer_tours(type,niveau, coordos)

    def game_over(self):
        self.vue.gameOver()


    def start_new_game(self):
        # demande au user si new game ou non Y/N
        pass

    def update_vie(self):
        self.vue.update_vie()



if __name__ == "__main__":
    c = Controleur()
