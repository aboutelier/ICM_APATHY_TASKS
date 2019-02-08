"""
Classe cercle permettant d'associer un cercle avec
ses coordonnées et sa couleur

Deux méthodes ont été rajoutées pour changer facilement
la couleur du cercle.

"""
import random


class Circle(object):
    def __init__(self, id_, x_min, y_min, size=90):
        self.id = id_
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_min + size
        self.y_max = y_min + size
        self.set_grey()

    @property
    def coords(self):
        return (self.x_min, self.y_min, self.x_max, self.y_max)

    def set_red(self):
        self.color = "red"

    def set_blue(self):
        self.color = "blue"

    def set_grey(self):
        self.color = "grey80"

    def set_random_color(self):
        liste_couleur = ["jaune", "vert", "bleu", "rouge"]
        self.color = random.choice(liste_couleur)

    def __repr__(self):
        return "Cercle {}".format(self.id)
