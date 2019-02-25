"""
Classe cercle permettant d'associer un cercle avec
ses coordonnées et sa couleur

Deux méthodes ont été rajoutées pour changer facilement
la couleur du cercle.

"""
import random

COLOR_LIST = ["yellow", "green", "blue", "red"]

CONSONNES_LIST = ['X', 'C', 'V', 'G', 'H', 'M', 'P', 'Z', 'S', 'T']
VOYELLES_LIST = ['A', 'E', 'I', 'O', 'U']


class Circle(object):
    def __init__(self, id_, x_min, y_min, size=90, random_color=False):
        self.id = id_
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_min + size
        self.y_max = y_min + size

        if random_color:
            self._inner_color = random.choice(COLOR_LIST)
        else:
            self._inner_color = None

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
        self.color = random.choice(COLOR_LIST)

    def toggle_color(self):
        if self._inner_color is not None:
            if self.color == 'grey80':
                self.color = self._inner_color
            else:
                self.set_grey()

    def __repr__(self):
        return "Cercle {}".format(self.id)

class CircleVerbal(object):
    def __init__(self, id_, x_min, y_min, size=90, random_color=False):
        self.id = id_
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_min + size
        self.y_max = y_min + size

    @property
    def coords(self):
        return (self.x_min, self.y_min, self.x_max, self.y_max)

    def set_random_consonne(self):
        self.consonne = random.choice(CONSONNES_LIST)

    def set_random_voyelle(self):
        self.voyelle = random.choice(VOYELLES_LIST)

    def __repr__(self):
        return "Cercle {}".format(self.id)

