import tkinter as tk

from tkinter import *


class Vue:
    def __init__(self, parent, modele):
        self.parent = parent
        self.modele = modele
        self.root = Tk()
        self.root.geometry("1260x960")  # 32x24 (x40) 24 = hauteur 32 = largeur
        self.window_width = 1280
        self.window_heigth = 960
        # self.create_canvases()
        total_height = 960
        canvas1_height = (3 / 4) * total_height # 3/4 du ratio
        canvas2_height = total_height - canvas1_height  # 1/4

        self.create_canvases(canvas1_height, canvas2_height)
        self.create_labels()
        self.create_boxes()
        self.create_troncons()
        self.create_events_amelioraton()
        self.create_chateau_canvas()

    def create_canvases(self, canvas1_height, canvas2_height):

        self.canvas1 = tk.Canvas(self.root, bg='white', height=canvas1_height, width=1280)
        self.canvas1.grid(row=0, column=0, sticky="nsew")


        self.canvas2 = tk.Canvas(self.root, bg='black', height=canvas2_height, width=1280)
        self.canvas2.grid(row=1, column=0, sticky="nsew") # nord sud est ouest donc il spread pour toucher a tous les bords du grid cell


        self.root.grid_rowconfigure(0, weight=3)  # Poids a chaque canvas
        self.root.grid_rowconfigure(1, weight=1)

    # def create_canvases(self):
    #
    #     # 18 rangées en hauteur, 32 largeur: 18*40 = 720? #ancien: 432
    #     self.canvas1 = Canvas(self.root, bg='white', height=720, width=1280)
    #     self.canvas1.pack(side=TOP, fill=BOTH, expand=True)
    #     # self.canvas1.pack()
    #     # self.canvas1.place(x=0,y=0)
    #
    #     # 6 rangées en bas, 32 largeur ... 6*40 = 240 (canvas1+canvas2 = 960) #ancien: 144
    #     self.canvas2 = Canvas(self.root, bg='black', height=240, width=1280)
    #     self.canvas2.pack(side=TOP, fill=BOTH, expand=True)
    #     # self.canvas2.pack()
    #     # self.canvas2.place(x=0, y=220)
    #
    #     self.btn_commencer = Button(self.canvas2, text="Commencer", font=('Helvetica', 11),
    #                                 command=self.parent.commencer_partie)
    #
    #     self.btn_commencer.pack(side=tk.LEFT, padx=100, pady=(20, 20),
    #                             anchor='n')  # Align buttons to the left with some padding
    #

    def create_labels(self):
        # Le contenu modifiable de chaque boite de linterface joueur
        self.chronoLabel = Label(self.root, text=str(self.modele.chrono), font=('Helvetica', 11), bg='white', width=5)
        self.vagueLabel = Label(self.canvas2, text=str(self.modele.vague), font=('Helvetica', 11), bg='white', width=5)
        self.choixTourTitreLabel = Label(self.canvas2, text="", font=('Helvetica', 11), bg='yellow', width=0)
        self.nbVieLabel = Label(self.root, text=str(self.modele.nbVies), font=('Helvetica', 11), bg='white', width=5)
        self.argentLabel = Label(self.canvas2, text=str(self.modele.argent), font=('Helvetica', 11), bg='white',
                                 width=5)
        self.tower1Label = Label(self.root, text="Projectile", font=('Helvetica', 11), bg='purple', width=8)
        self.tower2Label = Label(self.root, text="Éclair", font=('Helvetica', 11), bg='yellow', width=8)
        self.tower3Label = Label(self.root, text="Poison", font=('Helvetica', 11), bg='green', width=8)

        # La ou commencent les box de linterface joueur
        self.collective_boxes_width = 600
        self.margin = (self.window_width - self.collective_boxes_width) / 2  # pour centrer les box de linterface joueur
        self.start_x_position = self.margin

    def create_boxes(self):
        # Chaque widget de linterface joueur
        self.create_box(self.start_x_position + 0, 15, self.start_x_position + 100, 65, "Chrono", self.chronoLabel)
        self.create_box(self.start_x_position + 0, 75, self.start_x_position + 100, 125, "Vague", self.vagueLabel)
        self.create_box(self.start_x_position + 150, 15, self.start_x_position + 450, 125, "Choix de tours",
                        self.choixTourTitreLabel)
        self.create_box(self.start_x_position + 500, 15, self.start_x_position + 600, 65, "Vies", self.nbVieLabel)
        self.create_box(self.start_x_position + 500, 75, self.start_x_position + 600, 125, "Argent", self.argentLabel)


        self.create_tower_box(self.start_x_position + 160, 43, self.start_x_position + 240, 113, "purple",
                              self.tower1Label)


        self.create_tower_box(self.start_x_position + 260, 43, self.start_x_position + 340, 113, "yellow",
                              self.tower2Label)
        self.create_tower_box(self.start_x_position + 360, 43, self.start_x_position + 440, 113, "green",
                              self.tower3Label)




    def create_box(self, x1, y1, x2, y2, title_text, value_widget):
        padding = 20  # espace entre titre et box
        title_height = -5  # hauteur du titre

        # Titre au dessus des box
        title_label = Label(self.canvas2, text=title_text, font=('Helvetica', 11), fg='white', bg='black')
        self.canvas2.create_window((x1 + x2) // 2, y1 - title_height // 2, window=title_label)

        # Diminue la hauteur des box relativement au padding et hauteur des titres
        y1 += title_height + padding

        # Cree le rectangle de valeur
        self.canvas2.create_rectangle(x1, y1, x2, y2, fill='white', outline='white')

        # Place le label dans la box, au centre
        self.canvas2.create_window((x1 + x2) // 2, (y1 + y2) // 2, window=value_widget)

    def create_tower_box(self, x1, y1, x2, y2, color, tower_label):
        self.canvas2.create_rectangle(x1, y1, x2, y2, fill=color, outline='black')
        self.canvas2.create_window((x1 + x2) // 2, (y1 + y2) // 2, window=tower_label)

    def afficherChrono(self, time_left):
        self.chronoLabel.config(text=str(time_left))
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
        start1_coords = self.modele.dict_rect['start1']
        end1_coords = self.modele.dict_rect['end1']

        self.canvas1.create_rectangle(start1_coords, end1_coords,
                                      fill=self.modele.troncon_couleur, tags=("troncon1",))

        start2_coords = self.modele.dict_rect['start2']
        end2_coords = self.modele.dict_rect['end2']
        self.canvas1.create_rectangle(start2_coords, end2_coords,
                                      fill=self.modele.troncon_couleur, tags=("troncon2",))

        start3_coords = self.modele.dict_rect['start3']
        end3_coords = self.modele.dict_rect['end3']

        self.canvas1.create_rectangle(start3_coords, end3_coords,
                                      fill=self.modele.troncon_couleur, tags=("troncon3",))

        start4_coords = self.modele.dict_rect['start4']
        end4_coords = self.modele.dict_rect['end4']

        self.canvas1.create_rectangle(start4_coords, end4_coords,
                                      fill=self.modele.troncon_couleur, tags=("troncon4",))

        start5_coords = self.modele.dict_rect['start5']
        end5_coords = self.modele.dict_rect['end5']

        self.canvas1.create_rectangle(start5_coords, end5_coords,
                                      fill=self.modele.troncon_couleur, tags=("troncon5",))

        start6_coords = self.modele.dict_rect['start6']
        end6_coords = self.modele.dict_rect['end6']

        self.canvas1.create_rectangle(start6_coords, end6_coords,
                                      fill=self.modele.troncon_couleur, tags=("troncon6",))

        start7_coords = self.modele.dict_rect['start7']
        end7_coords = self.modele.dict_rect['end7']

        self.canvas1.create_rectangle(start7_coords, end7_coords,
                                      fill=self.modele.troncon_couleur, tags=("troncon7",))

        start8_coords = self.modele.dict_rect['start8']
        end8_coords = self.modele.dict_rect['end8']

        self.canvas1.create_rectangle(start8_coords, end8_coords,
                                      fill=self.modele.troncon_couleur, tags=("troncon8",))

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

