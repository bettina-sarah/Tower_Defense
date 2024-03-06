class Projectile:
    def __init__(self, x, y, target_x, target_y, damage, level, type):
        self.x = x  # Position x du projectile
        self.y = y  # Position y du projectile
        self.target_x = target_x  # Position x de la cible
        self.target_y = target_y  # Position y de la cible
        self.damage = damage  # Dégâts infligés par le projectile
        self.level = level  # Niveau de la tour qui a tiré le projectile
        self.speed = 5  # Vitesse du projectile
        self.type = type  # Type de projectile

        # Définir les caractéristiques spécifiques du projectile en fonction du type et du niveau de la tour
        if self.type == "Projectile":
            if self.level == 1:
                self.color = "red"  # Couleur du projectile de niveau 1
                self.speed = 7  # Vitesse du projectile de niveau 1
            elif self.level == 2:
                self.color = "orange"  # Couleur du projectile de niveau 2
                self.speed = 8  # Vitesse du projectile de niveau 2
            elif self.level == 3:
                self.color = "yellow"  # Couleur du projectile de niveau 3
                self.speed = 9  # Vitesse du projectile de niveau 3
        elif self.type == "Éclair":
            # Définir les caractéristiques spécifiques pour le type Éclair (à adapter)
            pass
        elif self.type == "Poison":
            # Définir les caractéristiques spécifiques pour le type Poison (à adapter)
            pass
