import Modele as mod
import Vue as vue


class Controleur():
    def __init__(self):
        self.modele = mod.Modele(self)
        self.vue = vue.Vue(self, self.modele)
        self.vue.root.after(1000, self.animer_jeu)
        # self.vue.root.after(2000, self.modele.spawn_creep)
        self.vue.root.mainloop()



    # def commencer_partie(self):
    #     if self.vue:
    #         if self.modele.enVie:
    #             # self.modele.creer_niveau() #cree la vague et creeps inactifs
    #             self.modele.jouer_prochain_coup()
    #             if not self.modele.chronoStarted:
    #                 self.start_chrono()
    #                 self.changer_vague()
    #             self.animer_jeu()
    #
    #     else:  # si pas en vie
    #         self.start_new_game()

    # def start_chrono(self):
    #     self.modele.chronoStarted = True
    #     if self.modele.chrono >= 0:
    #         self.vue.afficherChrono(self.modele.chrono)
    #         self.modele.chrono -= 1
    #         self.vue.root.after(1000, self.start_chrono)
    #     else:
    #         self.modele.chronoStarted = False
    #         self.modele.chrono = 10

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
        # self.vue.root.after_cancel(self.commencer_partie)
        # self.vue.root.after_cancel(self.modele.spawn_creep)
        self.vue.clear_game_over()
        self.modele.reinitialiser_modele()
        self.commencer_partie()
        # self.vue.root.after(1000, self.commencer_partie)
        # self.vue.root.after(2000, self.modele.spawn_creep)

    def update_vie(self):
        self.vue.update_vie()

    def update_argent(self):
        self.vue.update_argent()


if __name__ == "__main__":
    c = Controleur()
