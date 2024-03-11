class Eclair:
    def __init__(self, modele, departX, departY):
        self.modele = modele
        self.departX = departX
        self.departY = departY
        self.cibleX = departX # ajusté dans cibler creep
        self.cibleY = departY
        self.vitesse = 5
        self.taille = 5
        self.dommage = 5
        self.niveau = 1 # niv 2&3 = lasers: pas d'objet
        self.cooldown = 5
        self.couleur = "yellow" # a la base niv 1


    def cibler_creep(self):
        # self.cibleX =
        # self.cibleY =
        pass


    def afficher_shot(self):
        pass

    def creep_hit(self):
        pass
