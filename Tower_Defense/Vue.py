import tkinter as tk

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

        self.create_canvases(canvas1_height, self.canvas2_height)
        self.creer_infos_joueur()
        self.creer_menu_choix_tours()
        self.create_troncons()
        # self.create_events_amelioraton()
        self.create_chateau_canvas()



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
        self.titre_choix_tours = Label(self.canvas2, text='Choix des tours', font=('Helvetica', 11), fg='white', bg='black')
        self.canvas2.create_window(x * 2, y/2, anchor="center", window=self.titre_choix_tours)
        self.boutonTour1 = Button(self.canvas2, text='Tour Projectile', font=('Helvetica', 11), bg='white', width=10, height=5)
        self.canvas2.create_window(x*1.5, y * 2, anchor="center", window=self.boutonTour1)
        self.boutonTour1.config(bg='orange', fg='black')
        self.boutonTour2 = Button(self.canvas2, text='Tour Eclair', font=('Helvetica', 11), bg='white', width=10,height=5)
        self.canvas2.create_window(x*2, y * 2, anchor="center", window=self.boutonTour2)
        self.boutonTour2.config(bg='blue', fg='black')
        self.boutonTour3 = Button(self.canvas2, text='Tour Poison', font=('Helvetica', 11), bg='white', width=10,height=5)
        self.canvas2.create_window(x*2.5, y * 2, anchor="center", window=self.boutonTour3)
        self.boutonTour3.config(bg='green', fg='black')

    def create_canvases(self, canvas1_height, canvas2_height):

        self.canvas1 = tk.Canvas(self.root, bg='black', height=canvas1_height, width=1280)
        print(canvas1_height)
        #self.canvas1.grid(row=0, column=0, sticky="nsew")


        self.canvas2 = tk.Canvas(self.root, bg='red', height=canvas2_height, width=1280)
        # self.canvas2.grid(row=1, column=0, sticky="nsew") # nord sud est ouest donc il spread pour toucher a tous les bords du grid cell
        self.canvas1.pack()
        self.canvas2.pack()

        # self.root.grid_rowconfigure(0, weight=3)  # Poids a chaque canvas
        # self.root.grid_rowconfigure(1, weight=1)



    # def create_boxes(self):
    #     # Chaque widget de linterface joueur
    #     self.create_box(self.start_x_position + 0, 15, self.start_x_position + 100, 65, "Chrono", self.chronoLabel)
    #     self.create_box(self.start_x_position + 0, 75, self.start_x_position + 100, 125, "Vague", self.vagueLabel)
    #     self.create_box(self.start_x_position + 150, 15, self.start_x_position + 450, 125, "Choix de tours",
    #                     self.choixTourTitreLabel)
    #     self.create_box(self.start_x_position + 500, 15, self.start_x_position + 600, 65, "Vies", self.nbVieLabel)
    #     self.create_box(self.start_x_position + 500, 75, self.start_x_position + 600, 125, "Argent", self.argentLabel)
    #
    #
    #     self.create_tower_box(self.start_x_position + 160, 43, self.start_x_position + 240, 113, "purple",
    #                           self.tower1Label)
    #
    #
    #     self.create_tower_box(self.start_x_position + 260, 43, self.start_x_position + 340, 113, "yellow",
    #                           self.tower2Label)
    #     self.create_tower_box(self.start_x_position + 360, 43, self.start_x_position + 440, 113, "green",
    #                           self.tower3Label)




    # def create_box(self, x1, y1, x2, y2, title_text, value_widget):
    #     padding = 20  # espace entre titre et box
    #     title_height = 5  # hauteur du titre
    #
    #     # Titre au dessus des box
    #     # title_label = Label(self.menu_choix_tours, text=title_text, font=('Helvetica', 11), fg='white', bg='black')
    #     title_label = Label(self.canvas2, text=title_text, font=('Helvetica', 11), fg='white', bg='black')
    #     title_label_window = self.canvas2.create_window((x1 + x2) // 2, y1 - title_height // 2, window=title_label,
    #                                                     anchor='n')
    #
    #     self.monMenuChoixTours = self.canvas2.create_window((x1 + x2) // 2, y1 - title_height // 2, window=self.menu_choix_tours, tags="menuChoixTours")
    #     self.monMenuAmelioration = self.canvas2.create_window((x1 + x2) // 2, y1 - title_height // 2, window=self.menu_amelioration_tours, tags="menuAmeliorationTours")
    #
    #     # Diminue la hauteur des box relativement au padding et hauteur des titres
    #     y1 += title_height + padding
    #
    #     # Cree le contour blanc de Choix de tours.
    #     self.canvas2.create_rectangle(x1, y1, x2, y2, fill='white', outline='white')
    #
    #     # Place le label dans la box, au centre
    #     self.canvas2.create_window((x1 + x2) // 2, (y1 + y2) // 2, window=value_widget)

    # def create_tower_box(self, x1, y1, x2, y2, color, tower_label):
    #     self.canvas2.create_rectangle(x1, y1, x2, y2, fill=color, outline='black')
    #     self.canvas2.create_window((x1 + x2) // 2, (y1 + y2) // 2, window=tower_label)

    def afficherChrono(self, time_left):
        self.chrono.config(text=str(time_left))
        print("afficher chrono: timeleft", time_left)

    def create_circle(self, x, y, r, canvas):  #Méthode pour créer un cercle prenant les coordonnés du centre et la rayon
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvas.create_oval(x0, y0, x1, y1, fill = "red3", tags = ("creep",))

    #Affichage des Creeps actifs sur le canvas. Utilise la méthode create_circle

    def afficher_Creeps(self, x, y):
        #for i in self.modele.creeps_actifs:
            self.create_circle(x, y, 20, self.canvas1)


    def create_troncons(self):
        # A AMELIORER
        for i in self.modele.chemin.keys():
            start_coord = self.modele.chemin[i][0]
            end_coord = self.modele.chemin[i][1]
            self.canvas1.create_line(start_coord, end_coord, fill = self.modele.troncon_couleur, width =70, capstyle=tk.ROUND, tags= ("troncon"))

        # start1_coords = self.modele.dict_rect['start1']
        # end1_coords = self.modele.dict_rect['end1']
        #
        # self.canvas1.create_rectangle(start1_coords, end1_coords,
        #                               fill=self.modele.troncon_couleur, tags=("troncon1",))
        #
        # start2_coords = self.modele.dict_rect['start2']
        # end2_coords = self.modele.dict_rect['end2']
        # self.canvas1.create_rectangle(start2_coords, end2_coords,
        #                               fill=self.modele.troncon_couleur, tags=("troncon2",))
        #
        # start3_coords = self.modele.dict_rect['start3']
        # end3_coords = self.modele.dict_rect['end3']
        #
        # self.canvas1.create_rectangle(start3_coords, end3_coords,
        #                               fill=self.modele.troncon_couleur, tags=("troncon3",))
        #
        # start4_coords = self.modele.dict_rect['start4']
        # end4_coords = self.modele.dict_rect['end4']
        #
        # self.canvas1.create_rectangle(start4_coords, end4_coords,
        #                               fill=self.modele.troncon_couleur, tags=("troncon4",))
        #
        # start5_coords = self.modele.dict_rect['start5']
        # end5_coords = self.modele.dict_rect['end5']
        #
        # self.canvas1.create_rectangle(start5_coords, end5_coords,
        #                               fill=self.modele.troncon_couleur, tags=("troncon5",))
        #
        # start6_coords = self.modele.dict_rect['start6']
        # end6_coords = self.modele.dict_rect['end6']
        #
        # self.canvas1.create_rectangle(start6_coords, end6_coords,
        #                               fill=self.modele.troncon_couleur, tags=("troncon6",))
        #
        # start7_coords = self.modele.dict_rect['start7']
        # end7_coords = self.modele.dict_rect['end7']
        #
        # self.canvas1.create_rectangle(start7_coords, end7_coords,
        #                               fill=self.modele.troncon_couleur, tags=("troncon7",))
        #
        # start8_coords = self.modele.dict_rect['start8']
        # end8_coords = self.modele.dict_rect['end8']
        #
        # self.canvas1.create_rectangle(start8_coords, end8_coords,
        #                               fill=self.modele.troncon_couleur, tags=("troncon8",))

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
        self.canvas1.create_rectangle(894,438,972,528,fill=self.modele.chateau_couleur)

