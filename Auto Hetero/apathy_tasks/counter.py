"""
Classe compteur qui permet de stocker les résultats sans multiplier
le nombre de variables à instancier dans la classe principale

De nouvelles variables n_erreur_tot et total sont définies à partir des autres.

Des méthodes pour augmenter les compteurs ont été définies.

"""

class CounterDifficile(object):
    def __init__(self):
        self.n_reussites = 0
        self.n_distracteur = 0
        self.n_meme_combi = 0
        self.n_meme_cercle = 0
        self.n_a_cote = 0

    @property
    def n_erreur_tot(self):
        return (
            self.n_distracteur
            + self.n_meme_combi
            + self.n_meme_cercle
            + self.n_a_cote
        )

    @property
    def total(self):
        return self.n_erreur_tot + self.n_reussites

    def add_distracteur(self):
        self.n_distracteur += 1

    def add_reussite(self):
        self.n_reussites += 1

    def add_a_cote(self):
        self.n_a_cote += 1

    def add_meme_cercle(self):
        self.n_meme_cercle += 1

    def add_meme_combinaison(self):
        self.n_meme_combi += 1


class CounterFacile(object):
    def __init__(self):
        self.n_reussites = 0
        self.n_erreur_gris = 0
        self.n_distracteur = 0
        self.n_a_cote = 0

    @property
    def n_erreur_tot(self):
        return self.n_erreur_gris + self.n_distracteur + self.n_a_cote

    @property
    def total(self):
        return self.n_erreur_tot + self.n_reussites

    def add_error_gris(self):
        self.n_erreur_gris += 1

    def add_distracteur(self):
        self.n_distracteur += 1

    def add_reussite(self):
        self.n_reussites += 1

    def add_a_cote(self):
        self.n_a_cote += 1
