"""
Classe cercle permettant d'associer un cercle avec 
ses coordonnées et sa couleur

Deux méthodes ont été rajoutées pour changer facilement 
la couleur du cercle.

"""

class Circle(object):
    def __init__(self, x_min, y_min, color, size=90):
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_min + size
        self.y_max = y_min + size
        self.color = "grey80"
    
    @property
    def coords(self):
        return (self.x_min, self.y_min, self.x_max, self.y_max)
    
    def set_red(self):
        self.color = "red"
    
    def set_blue(self):
        self.color = "blue"
