from tkinter import *

class Vue:
    def __init__(self, parent, modele):
        self.parent = parent
        self.modele = modele
        self.root = Tk()
        self.root.geometry("1300x700")


        self.canvas1 = Canvas(self.root, bg='white', height=450, width=800)
        self.canvas1.pack(side=TOP, fill=BOTH, expand=True)


        self.canvas2 = Canvas(self.root, bg='black', height=150, width=800)
        self.canvas2.pack(side=TOP, fill=BOTH, expand=True)

        self.chronoLabel = Label(self.root, text="10", font=('Helvetica', 11), bg='white', width=5)
        self.vagueLabel = Label(self.canvas2, text="1", font=('Helvetica', 11),bg='white', width=5)
        self.choixTourTitreLabel = Label(self.canvas2, text="", font=('Helvetica', 11), bg='yellow', width=0)
        self.nbVieLabel = Label(self.root, text="20", font=('Helvetica', 11), bg='white', width=5)
        self.argentLabel = Label(self.canvas2, text="200", font=('Helvetica', 11), bg='white', width=5)
        self.tower1Label = Label(self.root, text="Projectile", font=('Helvetica', 11), bg='purple', width=8)
        self.tower2Label = Label(self.root, text="Éclair", font=('Helvetica', 11), bg='yellow', width=8)
        self.tower3Label = Label(self.root, text="Poison", font=('Helvetica', 11), bg='green', width=8)

        self.create_box(100, 15, 200, 65, "Chrono", self.chronoLabel)
        self.create_box(100, 75, 200, 125, "Vague", self.vagueLabel)
        self.create_box(250, 15, 550, 125, "Choix de tours", self.choixTourTitreLabel)
        self.create_box(600, 15, 700, 65, "Vies", self.nbVieLabel)
        self.create_box(600, 75, 700, 125, "Argent", self.argentLabel)
        self.create_tower_box(260, 43, 340, 113, "purple",self.tower1Label)
        self.create_tower_box(360, 43, 440, 113, "yellow", self.tower2Label)
        self.create_tower_box(460, 43, 540, 113, "green", self.tower3Label)

    def create_box(self, x1, y1, x2, y2, title_text, value_widget):
        padding = 20  # espace entre titre et box
        title_height = -5  # hauteur du titre
        canvas_width = self.canvas2.winfo_reqwidth()  # get canvas2 width
        offset_x = (canvas_width - 325) // 2  # Offset pour ajuster la position des box car passé dun width de 800 a 1300 par defaut

        # Ajustement pour centrer les box apres avoir passé de 800 a 1300 de default window width
        x1 += offset_x
        x2 += offset_x

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
        canvas_width = self.canvas2.winfo_reqwidth()
        offset_x = (canvas_width - 325) // 2

        x1 += offset_x
        x2 += offset_x
        self.canvas2.create_rectangle(x1, y1, x2, y2, fill=color, outline='black')
        self.canvas2.create_window((x1 + x2) // 2, (y1 + y2) // 2, window=tower_label)

def afficherChrono(self, time_left):
        self.chronoLabel.config(text=str(time_left))
