"""
Petite explication des changements
----------------------------------

En haut du fichier et dans l'ordre tu trouveras

1) des imports de deux nouvelles classes qui vont servir:
    - Cercle pour définir les positions, la couleur et le numéro des cercles
    - Counter pour la partie comptage des différentes réponses

2) des liens absolus vers des fichiers sur l'appareil qui sont utilisés
dans le code

3) des variables globales qui vont modifier le comportement général du
programme. Ex: changer TEST_TIME_SEC permet de diminuer le temps d'acquisition
ce qui est pratique pour tester le code

Dans la classe SDf j'ai:
- changé les noms des variables et des méthodes pour augmenter la clarté
- remplacé toutes les coordonnées écrites en dur par mes objets Cercles
- séparé clairement la partie initialisation du reste
- ajouté certaines méthodes partant du principe: une action = une méthode
- créé deux fichiers de sortie, un au format CSV (facile à lire dans Excel)
avec les infos que tu veux et l'autre en fichier texte classique avec les
valeurs qui résument le test.

"""
from os import mkdir
from os.path import join as joinpath
from random import randrange
from time import perf_counter
import tkinter
from tkinter import *
from tkinter import Tk
from tkinter import NW
from tkinter import Canvas
from tkinter import PhotoImage
from winsound import PlaySound
from winsound import SND_FILENAME
from winsound import SND_ASYNC

# Nouveaux imports
# ----------------
from .counter import CounterFacile
from .circle import Circle

# Chemins locaux vers les fichiers
# --------------------------------
MAINDIR = "C:\\Users\\ECOCAPTURE\\Desktop\\ECOCAPTURE\\ICM_APATHY_TASKS"

IMAGE_JAUGE_AUTOHETERO = joinpath(MAINDIR, "Image" , "jaugedouble2.ppm")

SON_PACE = joinpath(MAINDIR, "Son", ".wav")
SON_PERTE = joinpath(MAINDIR, "Son", "BOUH.wav")

DOSSIER_SUJETS = joinpath(MAINDIR, "Sujets")

# Valeurs modifiables
# -------------------
TEST_TIME_SEC = 50
END_TIMER_SEC = 20
SUMMARY_TIME_SEC = 15

SEPARATEUR = ";"

DELTA_PROGRESSION = 2
# N_REUSSITE_AVANT_SON = 5


class Hetero(Tk):
    valeurs_sauvees = [
        "distracteur", "cible",
        "cercle choisi",
        "resultat", "temps de reponse", "temps ecoule"
    ]

    def __init__(self, parent, nom):

        self.filename = joinpath(
            DOSSIER_SUJETS, nom, "{}_Hetero".format(nom)
        )
        self.save_text("TACHE SPATIALE HETEROGENEREE")
        self.save_csv(SEPARATEUR.join(self.valeurs_sauvees))

        self.racine = Tk()
        self.racine.attributes("-fullscreen", True)

        # Dimensions de l'écran
        self.w = self.racine.winfo_screenwidth()
        self.h = self.racine.winfo_screenheight()

        # Coordonnées du milieu de l'écran
        self.x_mid = self.w / 2
        self.y_mid = self.h / 2

        # Initialisation de la partie statique de l'affichage
        # (fond blanc + images)
        self.fond = Canvas(
            self.racine, bg="white", width=self.w, height=self.h
        )
        self.fond.pack(fill="both")

        self.jauge = PhotoImage(file = IMAGE_JAUGE_AUTOHETERO)
        self.imagejauge = self.fond.create_image(
            self.w - 1075, self.h/1.2,
            image = self.jauge,
            anchor = NW)

        Tk.__init__(self, parent)

        self._initialise_counters()
        self._initialise_figures()

        self.fond.bind("<Button-1>", self.attente)

    def _initialise_counters(self):
        """Mise à zéro des compteurs"""
        self.counter = CounterFacile()

        self.timer = END_TIMER_SEC

        self.SRT = 0
        self.SRTdejafait = 0
        self.RTmax = 0
        self.RTmin = 360

    def _initialise_figures(self):
        """Initialisation de la partie dynamique de l'affichage"""
        # On crée tous les cercles
        self.circles = [
            Circle(0, self.x_mid - 45, self.y_mid - 225),
            Circle(1, self.x_mid - 45, self.y_mid - 45),
            Circle(2, self.x_mid - 45, self.y_mid + 135),
            Circle(3, self.x_mid - 135, self.y_mid - 135),
            Circle(4, self.x_mid + 45, self.y_mid - 135),
            Circle(5, self.x_mid - 225, self.y_mid - 45),
            Circle(6, self.x_mid + 135, self.y_mid - 45),
            Circle(7, self.x_mid - 135, self.y_mid + 45),
            Circle(8, self.x_mid + 45, self.y_mid + 45),
            Circle(9, self.x_mid - 225, self.y_mid + 135),
            Circle(10, self.x_mid + 135, self.y_mid + 135),
            Circle(11, self.x_mid - 315, self.y_mid + 45),
            Circle(12, self.x_mid + 225, self.y_mid + 45),
            Circle(13, self.x_mid - 405, self.y_mid + 135),
            Circle(14, self.x_mid + 315, self.y_mid + 135),
        ]

        # on initialise les indices distracteur et cible
        self.distracteur_idx = 0
        self.cible_idx = 1

        # On trace les cercles avec les bonnes couleurs
        self.ellipses = None
        self.draw_circles()

        # On affiche la barre de progression
        self.progress = self.w - 292
        self.progress_bar = None
        self.draw_progression()

        self.chrono = None

        # On affiche les consignes
        self.start = self.fond.create_text(
            self.x_mid,
            self.y_mid,
            text="Touchez l'ecran pour démarrer",
            font="Arial 60 bold",
            fill="green",
        )
        self.consigne = self.fond.create_text(
            self.w / 1.3,
            (self.h / 1.6) - 300,
            text="Touchez le cercle bleu",
            font="Arial 20",
            justify="center",
        )

    def randomize_index(self):
        """Choix des indices aléatoires pour distracteur et cible"""
        circle_index = list(range(0, len(self.circles)))
        for _ in range(2):
            self.distracteur_idx = circle_index.pop(randrange(0, len(circle_index)))
            self.cible_idx = circle_index.pop(randrange(0, len(circle_index)))

    def attente(self, event):
        "Register some events to be triggered at a later time"
        self.fond.delete(self.racine, self.start)
        self.t0 = perf_counter()
        self.start_new_combinaison()
        self.after((TEST_TIME_SEC - END_TIMER_SEC) * 1000, self.start_chrono)
        self.after(TEST_TIME_SEC * 1000, self.finalisation)

    def save_text(self, text, newline=True, print_=True):
        # print in the console
        if print_:
            print(text)
        # and write in the file
        with open(self.filename + ".txt", "a") as f:
            f.write(text)
            if newline:
                f.write("\n")

    def save_csv(self, text, newline=True):
        with open(self.filename + ".csv", "a") as f:
            f.write(text)
            if newline:
                f.write("\n")

    def draw_circles(self):
        # Retire les cercles précédents si ils existent
        if self.ellipses is not None:
            for ellipse in self.ellipses:
                self.fond.delete(self.racine, ellipse)

        # Créé de nouveaux cercles
        self.ellipses = [
            self.fond.create_oval(circle.coords, fill=circle.color, width="5")
            for circle in self.circles
        ]

    def update_and_draw_circles(self):
        #on recolore les anciens cible et distracteur en gris#
        self.circles[self.distracteur_idx].set_grey()
        self.circles[self.cible_idx].set_grey()

        self.randomize_index()
        # Le premier est rouge (distracteur)
        self.circles[self.distracteur_idx].set_red()
        # Le deuxieme est bleu (cible)
        self.circles[self.cible_idx].set_blue()

        self.draw_circles()


    def draw_progression(self):
        if self.progress_bar is not None:
            self.fond.delete(self.racine, self.progress_bar)

        self.progress_bar = self.fond.create_rectangle(
            self.w - 292,
            self.h / 1.2 + 1,
            self.progress,
            self.h / 1.2 + 95,
            fill="white",
            width="1",
        )

    def start_new_combinaison(self):
        self.string_info = []

        self.update_and_draw_circles()

        self.string_info.append("Circle {}".format(self.distracteur_idx))
        self.string_info.append("Circle {}".format(self.cible_idx))

        self.tapp = perf_counter()

        self.fond.bind("<Button-1>", self.clic)

    #affichage RT et classement dans somme RT combi réussies ou déjà faites
    def store_response_time(self, dejaf = False):
        response_time = self.tclic - self.tapp
        self.string_info.append("{}".format(response_time))
        if dejaf:
            self.SRTdejafait += response_time
        else:
            self.SRT += response_time

        return response_time

    def save_line(self):
        # Add elapsed time
        self.string_info.append("{}".format(self.tclic - self.t0))

        # Join into a string and save as a new line in CSV file
        self.save_csv(SEPARATEUR.join(self.string_info))

    def clic(self, event):
        self.tclic = perf_counter()
        # Parcours la liste de cercles jusqu'à trouver le bon
        # Sinon on est tombé à côté.
        for idx, circle in enumerate(self.circles):
            isin_x = circle.x_min <= event.x <= circle.x_max
            isin_y = circle.y_min <= event.y <= circle.y_max
            if isin_x and isin_y:
                self.string_info.append("{}".format(circle))

                if circle.color == "blue":
                    self.after(100, self.reussite)
                elif circle.color == "red":
                    self.after(100, self.distrait)
                else:
                    self.after(100, self.cercle_gris)

                break
        else:
            coordclicx = self.fond.winfo_pointerx()
            coordclicy = self.fond.winfo_pointery()
            self.string_info.append(
                "Coords({},{})".format(coordclicx, coordclicy)
            )
            self.after(100, self.acote)

    def reussite(self):
        self.counter.add_reussite()

        self.string_info.append("Cible")

        response_time = self.store_response_time()
        print("RT (sec) = {}\n".format(response_time))
        self.RTmax = max(self.RTmax, response_time)
        self.RTmin = min(self.RTmin, response_time)

        self.progress -= DELTA_PROGRESSION
        self.draw_progression()

        # if self.counter.n_reussites % self.n_reussite_avant_son == 0:
        #     PlaySound(self.son, SND_FILENAME | SND_ASYNC)

        self.save_line()
        self.start_new_combinaison()

    def distrait(self):
        self.counter.add_distracteur()

        self.string_info.append("Distracteur")

        self.store_response_time()

        self.save_line()
        self.start_new_combinaison()

    def cercle_gris(self):
        self.counter.add_error_gris()

        self.string_info.append("Cercle gris")

        self.store_response_time()

        self.save_line()
        self.start_new_combinaison()

    def acote(self):
        self.counter.add_a_cote()

        self.string_info.append("A cote")

        self.store_response_time()

        self.save_line()
        self.start_new_combinaison()

    def start_chrono(self):
        self.save_csv("# ***** 30 sec line *****")
        self.show_chrono()

    def show_chrono(self):
        if self.chrono is not None:
            self.fond.delete(self.racine, self.chrono)

        self.chrono = self.fond.create_text(
            self.x_mid,
            self.h / 8,
            text="{}".format(self.timer),
            font="Arial 120 bold",
            fill="black",
        )

        self.one_second = self.after(1000, self.next_second)

    def next_second(self):
        self.timer -= 1

        if self.timer > 0:
            self.show_chrono()
        else:
            self.fond.delete(self.racine, self.chrono)

    def finalisation(self):
        self.racine.after_cancel(self.one_second)

        self.fond.destroy()
        self.fond = Canvas(
            self.racine, bg="white", width=self.w, height=self.h
        )
        self.fond.pack(fill="both")

        self.fond.create_text(
            self.x_mid,
            self.y_mid,
            text="FIN DE CETTE TACHE",
            font="Arial 30",
            justify="center",
        )
        print("THE END\n")

        if self.counter.total == 0:
            taux = 0
            RTmoyreussi = 180
            RTmoydejafait = 0
            RTmoytot = 180
        else:
            taux = self.counter.n_reussites / self.counter.total * 100
            if taux == 0:
                RTmoyreussi = 0
            else:
                RTmoyreussi = self.SRT / self.counter.n_reussites

            if self.counter.n_distracteur == 0:
                RTmoydejafait = 0
                RTmoytot = RTmoyreussi
            else:
                RTmoydejafait = self.SRTdejafait / self.counter.n_distracteur
                RTmoytot = (self.SRT + self.SRTdejafait) / (
                    self.counter.n_distracteur + self.counter.n_reussites
                )

        self.save_text("Bonnes reponses: %.2f" % self.counter.n_reussites)
        self.save_text("Erreurs couleur: %.2f" % self.counter.n_erreurs)
        self.save_text("Erreurs repetition: %.2f" % self.counter.n_distracteur)
        self.save_text("Erreurs à côte: %.2f" % self.counter.n_a_cote)
        self.save_text("Erreurs totales: {}".format(self.counter.n_erreur_tot))
        self.save_text("Nombre de reponses: {}".format(self.counter.total))
        self.save_text("Taux de reussite: %.2f" % taux)
        self.save_text("RTmoy reussi (sec): %.3f" % RTmoyreussi)
        self.save_text("RTmoy deja fait (sec): %.3f" % RTmoydejafait)
        self.save_text("RTmoy tot (sec): %.3f" % RTmoytot)
        self.save_text("RTmax (sec): %.3f" % self.RTmax)
        self.save_text("RTmin (sec): %.3f" % self.RTmin)

        self.after(SUMMARY_TIME_SEC * 1000, self.racine.destroy)


if __name__ == "__main__":
    nom = input("Nom sujet :")
    maindir = joinpath(DOSSIER_SUJETS, nom)
    try:
        mkdir(maindir)
    except FileExistsError:
        import sys
        sys.exit(
            "Subject name already exists. Try again with a different name."
        )

    app = Hetero(None, nom)
    app.title("My application")
    app.destroy()
    app.mainloop()
