class Poison:
    def __init__(self, modele, departX, departY, niveau):
        self.modele = modele
        self.departX = departX
        self.departY = departY
        self.cibleX = departX # ajusté dans cibler creep
        self.cibleY = departY
        self.vitesse = 5
        self.taille = 5
        self.dommage = 5
        self.niveau = niveau
        self.cooldown = 5
        self.couleur = "lawn green" # a la base niv 1

        if self.niveau == 2: # ACIDE RAPIDE: vitesse & dommage augmentés
            self.couleur = "spring green"
            self.vitesse = 10
            self.dommage = 10
            self.taille = 10
            self.cooldown = 2

        elif self.niveau == 3: # ACIDE FORTE: dommage augmenté, vitesse basse
            self.couleur = "dark green"
            self.vitesse = 5
            self.dommage = 15
            self.taille = 10
            self.cooldown = 5

    def cibler_creep(self):
        # self.cibleX =
        # self.cibleY =
        pass


    def afficher_shot(self):
        pass

    def creep_hit(self):
        pass
