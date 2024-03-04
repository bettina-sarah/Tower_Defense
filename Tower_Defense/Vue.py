import tkinter as tk

from tkinter import *
class Vue:
    def __init__(self, parent, modele):
        self.parent = parent
        self.modele = modele
        self.root = Tk()
        self.root.geometry("1280x960")  # 32x24 (x40)
        self.window_width = 1280
        self.create_canvases()
        self.create_labels()
        self.create_boxes()

    def create_canvases(self):
        # frame?
        self.canvas1 = Canvas(self.root, bg='white', height=432, width=1280)
        self.canvas1.pack(side=TOP, fill=BOTH, expand=True)

        self.canvas2 = Canvas(self.root, bg='black', height=144, width=1280)
        self.canvas2.pack(side=TOP, fill=BOTH, expand=True)

        self.btn_commencer = Button(self.canvas2, text="Commencer", font=('Helvetica', 11),
                                    command=self.parent.commencer_partie)

        self.btn_commencer.pack(side=tk.LEFT, padx=100, pady=(20, 20),
                                     anchor='n')  # Align buttons to the left with some padding

    def create_labels(self):
        # Le contenu modifiable de chaque boite de linterface joueur
        self.chronoLabel = Label(self.root, text=str(self.modele.chrono), font=('Helvetica', 11), bg='white', width=5)
        self.vagueLabel = Label(self.canvas2, text=str(self.modele.vague), font=('Helvetica', 11), bg='white', width=5)
        self.choixTourTitreLabel = Label(self.canvas2, text="", font=('Helvetica', 11), bg='yellow', width=0)
        self.nbVieLabel = Label(self.root, text=str(self.modele.nbVies), font=('Helvetica', 11), bg='white', width=5)
        self.argentLabel = Label(self.canvas2, text=str(self.modele.argent), font=('Helvetica', 11), bg='white', width=5)
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


