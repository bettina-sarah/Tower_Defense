from tkinter import *

class Vue:
    def __init__(self, parent, modele):
        self.parent = parent
        self.modele = modele
        self.root = Tk()
        self.root.geometry("800x600")


        self.canvas1 = Canvas(self.root, bg='white', height=450, width=800)
        self.canvas1.pack(side=TOP, fill=BOTH, expand=True)


        self.canvas2 = Canvas(self.root, bg='black', height=150, width=800)
        self.canvas2.pack(side=TOP, fill=BOTH, expand=True)

        self.chronoLabel = Label(self.root, text="10", font=('Helvetica', 11), bg='white', width=5)
        self.vagueLabel = Label(self.canvas2, text="1", font=('Helvetica', 11),bg='white', width=5)
        self.choixTourTitreLabel = Label(self.canvas2, text="", font=('Helvetica', 11), bg='white', width=30)
        self.nbVieLabel = Label(self.root, text="20", font=('Helvetica', 11), bg='white', width=5)
        self.argentLabel = Label(self.canvas2, text="200", font=('Helvetica', 11), bg='white', width=5)
        self.tower1Label = Label(self.root, text="Tour Projectile", font=('Helvetica', 7), bg='white')
        self.tower2Label = Label(self.root, text="Tour Eclair", font=('Helvetica', 7), bg='white')
        self.tower3Label = Label(self.root, text="Tour Poison", font=('Helvetica', 7), bg='white')

        self.create_box(100, 15, 200, 65, "Chrono", self.chronoLabel)
        self.create_box(100, 75, 200, 125, "Vague", self.vagueLabel)
        self.create_box(250, 15, 550, 125, "Choix de tours", self.choixTourTitreLabel)
        self.create_box(600, 15, 700, 65, "Vies", self.nbVieLabel)
        self.create_box(600, 75, 700, 125, "Argent", self.argentLabel)
        self.create_tower_box(260, 35, 340, 105, self.tower1Label)
        self.create_tower_box(360, 35, 440, 105, self.tower2Label)
        self.create_tower_box(460, 35, 540, 105, self.tower3Label)

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

    def create_tower_box(self, x1, y1, x2, y2, tower_label):

        self.canvas2.create_rectangle(x1, y1, x2, y2, fill='white', outline='black')
        self.canvas2.create_window((x1 + x2) // 2, (y1 + y2) // 2, window=tower_label)

def afficherChrono(self, time_left):
        self.chronoLabel.config(text=str(time_left))
