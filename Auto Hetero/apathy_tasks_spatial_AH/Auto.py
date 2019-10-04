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
from time import perf_counter
import tkinter
from tkinter import *
from tkinter import Tk
from tkinter import NW
from tkinter import Canvas
from tkinter import PhotoImage
# from winsound import PlaySound
# from winsound import SND_FILENAME
# from winsound import SND_ASYNC

# Nouveaux imports
# ----------------
from counter import CounterFacile
from circle import Circle

# Chemins locaux vers les fichiers
# --------------------------------
# pour tablette windows: MAINDIR = "C:\\Users\\ECOCAPTURE\\Desktop\\ECOCAPTURE\\ICM_APATHY_TASKS"
MAINDIR = "/Users/Ada/apathy_tasks_spatial_AH"
RESULTDIR = "/Users/Ada/Resultats"

IMAGE_JAUGE_AUTOHETERO = joinpath(MAINDIR, "Image", "jaugedouble2.ppm")

SON_PACE = joinpath(MAINDIR, "Son", "Metronome.wav")
SON_PERTE = joinpath(MAINDIR, "Son", "Son_Perte2.wav")

DOSSIER_SUJETS = joinpath(RESULTDIR, "Sujets")

# Valeurs modifiables
# -------------------
TEST_TIME_SEC = 50
SUMMARY_TIME_SEC = 15

SEPARATEUR = ";"

# pondération de la vitesse de perte : n pace avant perte visuelle
DELAY_PROGRESSION = 3
# nombre de delay progression avant son de perte
N_SLOW_BEFORE_SOUND = 3


class Auto(Tk):
    valeurs_sauvees = [
        "cercle choisi",
        "acote coord (x, y)", "temps de reponse", "temps ecoule"
    ]

    def __init__(self, parent, nom, maindir, pace=1):

        self.filename = joinpath(
            DOSSIER_SUJETS, nom, "{}_Auto".format(nom)
        )
        self.pace = int(pace)
        self.save_text("TACHE SPATIALE AUTOGENEREE")
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

        self.jauge = PhotoImage(file=IMAGE_JAUGE_AUTOHETERO)
        self.imagejauge = self.fond.create_image(
            self.w - 1075, self.h/1.2,
            image=self.jauge,
            anchor=NW)

        # Initialize progress
        self.progress = self.w - 292
        self.n_old_reussites = 0
        self.n_too_slow = 0

        Tk.__init__(self, parent)

        self._initialise_counters()
        self._initialise_figures()
        self._initialise_timers()

        # self.start_new_combinaison()

    def _initialise_counters(self):
        """Mise à zéro des compteurs"""
        self.counter = CounterFacile()

        self.timer = TEST_TIME_SEC

        self.SRT = 0
        self.RTmax = 0
        self.RTmin = 360

    def _initialise_figures(self):
        """Initialisation de la partie dynamique de l'affichage"""
        # On crée tous les cercles
        self.circles = [
            Circle(0, self.x_mid - 45, self.y_mid - 225, random_color=True),
            Circle(1, self.x_mid - 45, self.y_mid - 45, random_color=True),
            Circle(2, self.x_mid - 45, self.y_mid + 135, random_color=True),
            Circle(3, self.x_mid - 135, self.y_mid - 135, random_color=True),
            Circle(4, self.x_mid + 45, self.y_mid - 135, random_color=True),
            Circle(5, self.x_mid - 225, self.y_mid - 45, random_color=True),
            Circle(6, self.x_mid + 135, self.y_mid - 45, random_color=True),
            Circle(7, self.x_mid - 135, self.y_mid + 45, random_color=True),
            Circle(8, self.x_mid + 45, self.y_mid + 45, random_color=True),
            Circle(9, self.x_mid - 225, self.y_mid + 135, random_color=True),
            Circle(10, self.x_mid + 135, self.y_mid + 135, random_color=True),
            Circle(11, self.x_mid - 315, self.y_mid + 45, random_color=True),
            Circle(12, self.x_mid + 225, self.y_mid + 45, random_color=True),
            Circle(13, self.x_mid - 405, self.y_mid + 135, random_color=True),
            Circle(14, self.x_mid + 315, self.y_mid + 135, random_color=True),
        ]

        # On trace les cercles avec les bonnes couleurs
        self.ellipses = None
        self.draw_circles()

        # On affiche la barre de progression
        self.progress_bar = None
        self.draw_progression()

        self.delta_progression = self.pace * 783 / TEST_TIME_SEC

        self.chrono = None

    def _initialise_timers(self):
        self.t0 = perf_counter()
        self.start_new_combinaison()
        self.show_chrono()
        self.after(TEST_TIME_SEC * 1000, self.finalisation)
        self.metronome_event()
        self.update_progress()
        
        # self.start()

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

        self.draw_circles()

        self.tapp = perf_counter()

        self.fond.bind("<Button-1>", self.clic)

    def store_response_time(self, dejafait=False):
        response_time = self.tclic - self.tapp
        self.string_info.append("{}".format(response_time))
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

                circle.toggle_color()
                self.draw_circles()
                circle.set_grey()

                self.after(200, self.reussite)

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

        self.save_line()
        self.start_new_combinaison()

    def acote(self):
        self.counter.add_a_cote()

        self.string_info.append("A cote")

        self.store_response_time()

        self.save_line()
        self.start_new_combinaison()

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

        print("timer=", self.timer)
        self.timer -= 1
        print("timer=", self.timer)

        self.chrono_event = self.after(1000, self.show_chrono)

    def metronome_event(self):
        # PlaySound(SON_PACE, SND_FILENAME | SND_ASYNC)
        self.after(self.pace * 1000, self.metronome_event)

    def update_progress(self):
        n_current_reussites = self.counter.n_reussites

        if n_current_reussites - self.n_old_reussites < DELAY_PROGRESSION:
            self.progress -= self.delta_progression
            self.draw_progression()

            self.n_too_slow += 1
            
        if self.n_too_slow % N_SLOW_BEFORE_SOUND == 0:
            PlaySound(SON_PERTE, SND_FILENAME | SND_ASYNC)

        self.n_old_reussites = n_current_reussites

        self.progress_event = self.after(DELAY_PROGRESSION * self.pace * 1000, self.update_progress)

    def finalisation(self):
        self.after_cancel(self.chrono_event)
        self.after_cancel(self.metronome)
        self.after_cancel(self.update_progress)

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
            RTmoytot = 180
        else:
            taux = self.counter.n_reussites / self.counter.total * 100
            if taux == 0:
                RTmoyreussi = 0
            else:
                RTmoyreussi = self.SRT / self.counter.n_reussites

            if self.counter.n_distracteur == 0:
                RTmoytot = RTmoyreussi
            else:
                RTmoytot = (
                    self.SRT / (self.counter.n_distracteur + self.counter.n_reussites)
                )

        self.save_text("Bonnes reponses (cercle): %.2f" % self.counter.n_reussites)
        self.save_text("Erreurs à côte: %.2f" % self.counter.n_a_cote)
        self.save_text("Nombre de reponses: {}".format(self.counter.total))
        self.save_text("Taux de reussite: %.2f" % taux)
        self.save_text("RTmoy reussi (sec): %.3f" % RTmoyreussi)
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

    app = Auto(None, nom, maindir)
    app.title("My application")
    app.destroy()
    app.mainloop()
