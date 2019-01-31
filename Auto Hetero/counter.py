"""
Classe compteur qui permet de stocker les résultats sans multiplier
le nombre de variables à instancier dans la classe principale

De nouvelles variables NET et total sont définies à partir des autres.

Des méthodes pour augmenter les compteurs ont été définies.

"""

class Counter(object):
    def __init__(self):
        self.NR = 0
        self.NE = 0
        self.ND = 0
        self.MC = 0
        self.AC = 0

    @property
    def NET(self):
        return self.NE + self.ND + self.MC + self.AC

    @property
    def total(self):
        return self.NET + self.NR
    
    def add_error(self):
        self.NE += 1
    
    def add_reussite(self):
        self.NR += 1
    
    def add_a_cote(self):
        self.AC += 1
    
    def add_meme_cercle(self):
        self.MC += 1

    def add_meme_combinaison(self):
        self.ND += 1
