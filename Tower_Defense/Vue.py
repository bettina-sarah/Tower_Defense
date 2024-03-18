import tkinter as tk
from functools import partial

from tkinter import *


class Vue:
    def __init__(self, parent, modele):
        self.parent = parent
        self.modele = modele
        self.root = Tk()
        self.root.geometry("1280x960")  # 32x24 (x40) 24 = hauteur 32 = largeur
        self.fenetre_largeur = 1280
        self.fenetre_hauteur = 960
        # self.create_canvases()
        total_height = 960
        canvas1_height = total_height/4 * 3 # 3/4 du ratio
        self.canvas2_height = total_height/4  # 1/4
        self.placement_tours = False
        self.road_items = []
        self.titre_choix_tours_id = None
        self.boutonTour1_id = None
        self.boutonTour2_id = None
        self.boutonTour3_id = None

        self.create_canvases(canvas1_height, self.canvas2_height)
        self.creer_infos_joueur()
        self.creer_menu_choix_tours()
        self.create_troncons()
        # self.create_events_amelioraton()
        self.create_chateau_canvas()





    def creer_tour(self, event):

            rectangle_x = event.x + 20
            rectangle_y = event.y
            coordos = rectangle_x, rectangle_y

            # Check sil y a un overlap
            overlapping_items = self.canvas1.find_overlapping(rectangle_x, rectangle_y, rectangle_x + 40,
                                                        rectangle_y + 45)
            coordos = event.x, event.y

            # Si pas de overlap, place la tour
            if not any(item in overlapping_items for item in self.road_items) and self.placement_tours == True:
                self.placement_tours = False
                if self.tour_en_cours == "Projectile":
                    self.canvas1.create_rectangle(rectangle_x, rectangle_y, rectangle_x + 40,
                                            rectangle_y + 45, fill="orange", tag="projectile")

                    self.parent.creer_tours("Projectile", 1, coordos)
                    self.canvas1.tag_bind("projectile", "<Button-1>", self.afficher_amelioration)

                elif self.tour_en_cours == "Eclair":
                    self.canvas1.create_rectangle(rectangle_x, rectangle_y, rectangle_x + 40,
                                            rectangle_y + 45, fill="blue", tag="eclair")
                    self.parent.creer_tours("Eclair", 1, coordos)
                    self.canvas1.tag_bind("eclair", "<Button-1>", self.afficher_amelioration)
                elif self.tour_en_cours == "Poison":
                    self.canvas1.create_rectangle(rectangle_x, rectangle_y, rectangle_x + 40,
                                            rectangle_y + 45, fill="green", tag="poison")
                    self.parent.creer_tours("Poison", 1, coordos)
                    self.canvas1.tag_bind("poison", "<Button-1>", self.afficher_amelioration)

            # self.verifier_amelioration()

    def trigger_placement_tours(self, event, tour_en_cours):
        self.placement_tours = not self.placement_tours
        if self.placement_tours:
            self.tour_en_cours = tour_en_cours
            self.canvas1.bind("<Button-1>", self.creer_tour)

    # def verifier_amelioration(self):
    #     tags = self.canvas1.gettags()
    #     if "projectile" in tags:
    #         afficher_amelioration_projectile()
    #     elif "eclair" in tags:
    #         afficher_amelioration_eclair()
    #     elif "poison" in tags:
    #         afficher_amelioration_poison()

    def afficher_amelioration(self, event):
        self.supprimer_menu_choix_tours()
        x = self.fenetre_largeur / 4
        y = self.canvas2_height / 5
        self.titre_amelioration_tours = Label(self.canvas2, text='Amelioration du tour', font=('Helvetica', 11), fg='white',
                                           bg='black')
        self.titre_amelioration_tours_id = self.canvas2.create_window(x * 2, y / 2, anchor="center",
                                                                   window=self.titre_amelioration_tours)

        self.amelioration_quitter_btn = Button(self.canvas2, text="X",font=('Helvetica', 15))
        self.quitter_window_id = self.canvas2.create_window(x * 2.5, y/2, anchor="center", window = self.amelioration_quitter_btn)

        self.amelioration_quitter_btn.bind("<Button-1>", self.supprimer_menu_amelioration)

        # variables a chercher en fonction du tour a ameliorer du MODELE
        label_amelioration_texte = f"\n Cout \n\n + Force: {self.modele.variable_test} \n\n\n + Étendu: {self.modele.variable_test} \n"
        self.label_amelioration = Label(self.canvas2, text=label_amelioration_texte, font=('Helvetica', 11), fg='white',
                                           bg='black')
        self.amelioration_window_id = self.canvas2.create_window(x * 1.5, y*2.5, anchor="center", window = self.label_amelioration)


        self.bouton_ameliorer = Button(self.canvas2, text='AMÉLIORER', font=('Helvetica', 10), bg='white', width=10,
                                  height=5)
        self.bouton_ameliorer_id = self.canvas2.create_window(x * 2, y * 2, anchor="center", window=self.bouton_ameliorer)

        label_tour_actuel_texte = f"\n Tour \n\n  Force: {self.modele.variable_test} \n\n\n  Étendu: {self.modele.variable_test} \n"
        self.label_tour_actuel = Label(self.canvas2, text=label_tour_actuel_texte, font=('Helvetica', 11), fg='white',
                                           bg='black')
        self.tour_actuel_window_id = self.canvas2.create_window(x * 2.5, y * 2.5, anchor="center", window = self.label_tour_actuel)




    def supprimer_menu_amelioration(self, event):
        self.canvas2.delete(self.titre_amelioration_tours_id)
        self.canvas2.delete(self.quitter_window_id)
        self.canvas2.delete(self.amelioration_window_id)
        self.canvas2.delete(self.bouton_ameliorer_id)
        self.canvas2.delete(self.tour_actuel_window_id)

        self.creer_menu_choix_tours()















    def creer_infos_joueur(self):

        x = self.fenetre_largeur / 4
        y = self.canvas2_height / 5

        self.chronoLabel = Label(self.canvas2, text='Chrono',font=('Helvetica', 11), bg='white', width=5)
        self.chrono = Label(self.canvas2, text=str(self.modele.chrono), font=('Helvetica', 11),bg='white', width=5)
        self.canvas2.create_window(x / 2,y * 1 , anchor="center", window=self.chronoLabel)
        self.canvas2.create_window(x / 2, y * 2, anchor="center", window=self.chrono)





        self.vagueLabel = Label(self.canvas2, text='Vague', font=('Helvetica', 11), bg='white', width=5)
        self.vague = Label(self.canvas2, text=str(self.modele.vague), font=('Helvetica', 11), bg='white', width=5)
        self.canvas2.create_window(x / 2, y * 3, anchor="center", window=self.vagueLabel)
        self.canvas2.create_window(x / 2, y * 4, anchor="center", window=self.vague)


        self.nbVieLabel = Label(self.canvas2, text='Vies', font=('Helvetica', 11), bg='white', width=5)
        self.nbVie = Label(self.canvas2, text=str(self.modele.nbVies), font=('Helvetica', 11), bg='white', width=5)
        self.canvas2.create_window(x * 3.5, y * 1, anchor="center", window=self.nbVieLabel)
        self.canvas2.create_window(x * 3.5, y * 2, anchor="center", window=self.nbVie)


        self.argentLabel = Label(self.canvas2, text='Argent', font=('Helvetica', 11), bg='white',
                                 width=5)
        self.argent = Label(self.canvas2, text=str(self.modele.argent), font=('Helvetica', 11), bg='white',
                                 width=5)

        self.canvas2.create_window(x * 3.5, y * 3, anchor="center", window=self.argentLabel)
        self.canvas2.create_window(x * 3.5, y * 4, anchor="center", window=self.argent)

    def creer_menu_choix_tours(self):
        x = self.fenetre_largeur / 4
        y = self.canvas2_height / 5
        self.titre_choix_tours = Label(self.canvas2, text='Choix des tours', font=('Helvetica', 11), fg='white',
                                       bg='black')
        self.titre_choix_tours_id = self.canvas2.create_window(x * 2, y / 2, anchor="center",
                                                               window=self.titre_choix_tours)

        self.boutonTour1 = Button(self.canvas2, text='Tour Projectile', font=('Helvetica', 11), bg='white', width=10,
                                  height=5)
        self.boutonTour1_id = self.canvas2.create_window(x * 1.5, y * 2, anchor="center", window=self.boutonTour1)
        self.boutonTour1.config(bg='orange', fg='black')

        self.boutonTour2 = Button(self.canvas2, text='Tour Eclair', font=('Helvetica', 11), bg='white', width=10,
                                  height=5)
        self.boutonTour2_id = self.canvas2.create_window(x * 2, y * 2, anchor="center", window=self.boutonTour2)
        self.boutonTour2.config(bg='blue', fg='black')

        self.boutonTour3 = Button(self.canvas2, text='Tour Poison', font=('Helvetica', 11), bg='white', width=10,
                                  height=5)
        self.boutonTour3_id = self.canvas2.create_window(x * 2.5, y * 2, anchor="center", window=self.boutonTour3)
        self.boutonTour3.config(bg='green', fg='black')

        self.boutonTour1.bind("<Button-1>", partial(self.trigger_placement_tours, tour_en_cours="Projectile"))
        self.boutonTour2.bind("<Button-1>", partial(self.trigger_placement_tours, tour_en_cours="Eclair"))
        self.boutonTour3.bind("<Button-1>", partial(self.trigger_placement_tours, tour_en_cours="Poison"))

    def supprimer_menu_choix_tours(self):
        self.canvas2.delete(self.titre_choix_tours_id)
        self.canvas2.delete(self.boutonTour1_id)
        self.canvas2.delete(self.boutonTour2_id)
        self.canvas2.delete(self.boutonTour3_id)

    def create_canvases(self, canvas1_height, canvas2_height):

        self.canvas1 = tk.Canvas(self.root, bg='black', height=canvas1_height, width=1280)
        #self.canvas1.grid(row=0, column=0, sticky="nsew")


        self.canvas2 = tk.Canvas(self.root, bg='red', height=canvas2_height, width=1280)
        # self.canvas2.grid(row=1, column=0, sticky="nsew") # nord sud est ouest donc il spread pour toucher a tous les bords du grid cell
        self.canvas1.pack()
        self.canvas2.pack()

        # self.root.grid_rowconfigure(0, weight=3)  # Poids a chaque canvas
        # self.root.grid_rowconfigure(1, weight=1)

    def afficherChrono(self, time_left):
        self.chrono.config(text=str(time_left))

    def afficher_vague(self):
        self.vague.config(text=str(self.modele.vague))



    def create_circle(self, x, y, canvas):  #Méthode pour créer un cercle prenant les coordonnés du centre et la rayon
        r = 20 # test
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvas.create_oval(x0, y0, x1, y1, fill = "red3", tags = "creep")

    #Affichage des Creeps actifs sur le canvas. Utilise la méthode create_circle

    def afficher_creeps(self):
        self.canvas1.delete("creep")
        for i in self.modele.creeps_actifs:
            self.create_circle(i.posX, i.posY, self.canvas1)


    def create_troncons(self):
        for i in self.modele.chemin.keys():
            start_coord = self.modele.chemin[i][0]
            end_coord = self.modele.chemin[i][1]
            self.road_items.append(self.canvas1.create_line(start_coord, end_coord, fill = self.modele.troncon_couleur, width =70, capstyle=tk.ROUND, tags= "troncon"))


    def create_events_amelioraton(self):
        # attacher event sur le label tower1:
        self.tower1Label.bind("<Button-1>", self.create_box_amelioration)

    def create_box_amelioration(self, event):
        self.create_box(self.start_x_position + 150, 15, self.start_x_position + 450, 125, "Amélioration des tours",
                        self.choixTourTitreLabel)

    def create_chateau_canvas(self):
       # coinG_coords = self.modele.dict_pos_chateau['coinG']
       # finG_coords = self.modele.dict_pos_chateau['finG']
       # self.canvas1.create_rectangle(coinG_coords, finG_coords,
       #                               fill=self.modele.chateau_couleur, tags=("troncon",))
       #
       # coinD_coords = self.modele.dict_pos_chateau['coinD']
       # finD_coords = self.modele.dict_pos_chateau['finD']
       # self.canvas1.create_rectangle(coinD_coords,finD_coords,
       #                               fill=self.modele.chateau_couleur, tags=("troncon",))
       # blocHG_coords = self.modele.dict_pos_chateau['blocHG']
       # finHG_coords = self.modele.dict_pos_chateau['finHG']
       # self.canvas1.create_rectangle(blocHG_coords,finHG_coords,
       #                               fill=self.modele.chateau_couleur, tags=("troncon",))
       # blocHD_coords = self.modele.dict_pos_chateau['blocHD']
       # finHD_coords = self.modele.dict_pos_chateau['finHD']
       # self.canvas1.create_rectangle(blocHD_coords,finHD_coords,
       #                               fill=self.modele.chateau_couleur, tags=("troncon",))
       # blocMG_coords = self.modele.dict_pos_chateau['blocMG']
       # finMG_coords = self.modele.dict_pos_chateau['finMG']
       # self.canvas1.create_rectangle(blocMG_coords,finMG_coords,
       #                               fill=self.modele.chateau_couleur, tags=("troncon",))
       #
       # blocMD_coords = self.modele.dict_pos_chateau['blocMD']
       # finMD_coords = self.modele.dict_pos_chateau['finMD']
       # self.canvas1.create_rectangle(blocMD_coords,finMD_coords,
       #                               fill=self.modele.chateau_couleur, tags=("troncon",))
       # blocBG_coords = self.modele.dict_pos_chateau['blocBG']
       # finBG_coords = self.modele.dict_pos_chateau['finBG']
       # self.canvas1.create_rectangle(blocBG_coords,finBG_coords,
       #                               fill=self.modele.chateau_couleur, tags=("troncon",))
       #
       # blocBD_coords = self.modele.dict_pos_chateau['blocBD']
       # finBD_coords = self.modele.dict_pos_chateau['finBD']
       #
       # self.canvas1.create_rectangle(blocBD_coords,finBD_coords,
       #                               fill=self.modele.chateau_couleur, tags=("troncon",))
        self.canvas1.create_rectangle(894,438,972,528,fill=self.modele.chateau_couleur, tags= "chateau")

