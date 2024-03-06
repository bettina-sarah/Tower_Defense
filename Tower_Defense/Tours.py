class Tour:
    def __init__(self, x, y, type):
        self.x = x  # Position x de la tour
        self.y = y  # Position y de la tour
        self.type = type  # Type de la tour (Projectile, Éclair, Poison)
        self.level = 1  # Niveau de la tour (peut être amélioré)
        self.range = 100  # Portée d'attaque de la tour
        self.damage = 10  # Dégâts infligés par la tour
        self.cost = 100  # Coût initial de la tour
        self.upgrade_cost = 50  # Coût d'amélioration de la tour

    def create_projectile(self, target_x, target_y):
        # Créer un projectile en fonction du type de la tour
        return Projectile(self.x, self.y, target_x, target_y, self.damage, self.level, self.type)

    def upgrade(self):
        # Méthode pour améliorer la tour
        if self.level < 3:
            self.level += 1
            # Augmenter les caractéristiques de la tour en fonction du niveau
            # (par exemple, augmenter les dégâts, la portée, etc.)
            self.damage *= 1.5
            self.range *= 1.2
            self.upgrade_cost *= 1.5
