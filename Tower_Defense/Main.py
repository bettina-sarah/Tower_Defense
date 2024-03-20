import Modele as mod
import Vue as vue


class Controleur():
    def __init__(self):
        self.modele = mod.Modele(self)
        self.vue = vue.Vue(self, self.modele)
        self.vue.root.after(1000, self.animer_jeu)
        # self.vue.root.after(2000, self.modele.spawn_creep)
        self.vue.root.mainloop()

    def changer_vague(self):
        self.vue.afficher_vague()

    def animer_jeu(self):
        #vue affiche creeps
        self.checkVie()
        if self.modele.enVie:
            self.modele.jouer_prochain_coup()
            self.vue.afficher_jeu()
            self.vue.root.after(50, self.animer_jeu)
        else:
            self.game_over()

    def creer_tours(self, x, y, niveau, type):
        self.modele.creer_tours(x, y, niveau, type)

    def tour_a_creer(self, tour):
        self.vue.creer_tours(tour)

    def checkVie(self):
        if self.modele.nbVies == 0:
            self.modele.enVie = False

    def game_over(self):
        self.vue.game_over()


    def start_new_game(self, event):
        self.vue.clear_game_over()
        self.modele.reinitialiser_modele()
        self.commencer_partie()

    def update_vie(self):
        self.vue.update_vie()

    def update_argent(self):
        self.vue.update_argent()


if __name__ == "__main__":
    c = Controleur()
