class Projectile:
    def __init__(self, modele, departX, departY, niveau):
        self.modele = modele
        self.departX = departX
        self.departY = departY
        self.cibleX = departX # ajusté dans cibler creep
        self.cibleY = departY
        self.vitesse = 3
        self.taille = 3
        self.dommage = 3
        self.niveau = niveau
        self.cooldown = 5
        self.couleur = "azure4" # a la base niv 1

        if self.niveau == 2: # balle rapide
            self.couleur = "MediumPurple4"
            self.vitesse = 10
            self.dommage = 10
            self.taille = 10
            self.cooldown = 2

        elif self.niveau == 3: # grenade : taille grande, vitesse lente,
            self.couleur = "tomato"
            self.vitesse = 5
            self.dommage = 15
            self.taille = 10
            self.cooldown = 50

    def cibler_creep(self):
        # self.cibleX =
        # self.cibleY =
        pass


    def afficher_shot(self):
        pass

    def creep_hit(self):
        pass
