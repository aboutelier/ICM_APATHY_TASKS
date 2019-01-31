import os
import random
import time
import tkinter
import winsound
from os.path import join as joinpath
from tkinter import *

# Nouveaux imports
# ----------------
from counter import Counter
from circle import Circle

# Chemins locaux vers les fichiers
# --------------------------------
MAINDIR = "C:\\Users\\ECOCAPTURE\\Desktop\\ECOCAPTURE\\ICM_APATHY_TASKS"

IMAGE_PIECES = joinpath(MAINDIR, "Image", "pieces.ppm")
IMAGE_JAUGE = joinpath(MAINDIR, "Image", "jauge.ppm")

SON_PIECES = joinpath(MAINDIR, "Son", "Pièces.wav")

DOSSIER_SUJETS = joinpath(MAINDIR, "Sujets")

# Valeurs modifiables
# -------------------
DELTA_PROGRESSION = 2.50
N_REUSSITE_AVANT_SON = 5

END_TIMER_SEC = 30
TEST_TIME_SEC = 180
SUMMARY_TIME_SEC = 15


class SDf(tkinter.Tk):
    titre = "SpatialeDifficileFaible"
    extension = "xls"

    def __init__(self, nom, parent=None):
        super().__init__(self, parent)

        self.filename = joinpath(
            DOSSIER_SUJETS, nom, "{}_{}.{}".format(nom, self.titre, self.extension)
        )
        self.save_text("TACHE SPATIALE DIFFICILE FAIBLE GAIN")
        self.save_text(
            "Coord Cercle 1,Coord Cercle 2,Coord Cercle 3,Coord Cercle 4,Combi,RT"
        )

        self.racine = tkinter.Tk()
        self.racine.attributes("-fullscreen", True)

        # Dimensions de l'écran
        self.w = self.racine.winfo_screenwidth()
        self.h = self.racine.winfo_screenheight()

        # Coordonnées du milieu de l'écran
        self.x_mid = self.w / 2
        self.y_mid = self.h / 2

        # Initialisation de la partie statique de l'affichage (fond blanc + images)
        self.fond = tkinter.Canvas(self.racine, bg="white", width=self.w, height=self.h)
        self.fond.pack(fill="both")
        self.fond.create_image(50, 10, image=PhotoImage(file=IMAGE_PIECES), anchor=NW)
        self.fond.create_image(
            self.w - 925, (self.h / 1.2), image=PhotoImage(file=IMAGE_JAUGE), anchor=NW
        )

        self._initialise_counters()
        self._initialise_figures()

        self.fond.bind("<Button-1>", self.attente)

    def _initialise_counters(self):
        """Mise à zéro des compteurs"""
        self.combi = []
        self.counter = Counter()

        self.t0 = time.perf_counter()
        self.temps = END_TIMER_SEC

        self.SRT = 0
        self.SRTdejafait = 0
        self.RTmax = 0
        self.RTmin = 360

    def _initialise_figures(self):
        """Initialisation de la partie dynamique de l'affichage"""
        # On crée tous les cercles
        self.circles = [
            Circle(self.x_mid - 45, self.y_mid - 225),
            Circle(self.x_mid - 45, self.y_mid - 45),
            Circle(self.x_mid - 45, self.y_mid + 135),
            Circle(self.x_mid - 135, self.y_mid - 135),
            Circle(self.x_mid + 45, self.y_mid - 135),
            Circle(self.x_mid - 225, self.y_mid - 45),
            Circle(self.x_mid + 135, self.y_mid - 45),
            Circle(self.x_mid - 135, self.y_mid + 45),
            Circle(self.x_mid + 45, self.y_mid + 45),
            Circle(self.x_mid - 225, self.y_mid + 135),
            Circle(self.x_mid + 135, self.y_mid + 135),
            Circle(self.x_mid - 315, self.y_mid + 45),
            Circle(self.x_mid + 225, self.y_mid + 45),
            Circle(self.x_mid - 405, self.y_mid + 135),
            Circle(self.x_mid + 315, self.y_mid + 135),
        ]

        # On pioche 5 cercles aléatoirement pour changer leur couleur
        color_index = []
        # Liste des indices des differents cercles
        circle_index = list(range(0, len(self.circles)))
        for _ in range(5):
            # Valeur aléatoire entre 0 et le nombre de cercles disponibles
            random_val = random.randrange(0, len(circle_index))
            # On extrait cette valeur de la liste des indices (on la supprime au passage)
            idx_random = circle_index.pop(random_val)
            # On l'ajoute à notre nouvelle liste
            color_index.append(idx_random)

        # Les deux premiers seront rouges
        for idx in color_index[:2]:
            self.circles[idx].set_red()

        # Les trois derniers bleus
        for idx in color_index[2:]:
            self.circles[idx].set_blue()

        # On trace les cercles avec les bonnes couleurs
        self.ellipses = None
        self.draw_circles()

        # On affiche la barre de progresion
        self.progr = self.w - 925
        self.pb = None
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
            text="Faites des combinaisons de\n4 cercles gris",
            font="Arial 20",
            justify="center",
        )

    def attente(self, event):
        "Register some events to be triggered at a later time"
        self.fond.delete(self.racine, self.start)
        self.start_new_combinaison()
        self.after((TEST_TIME_SEC - END_TIMER_SEC) * 1000, self.start_chrono)
        self.after(TEST_TIME_SEC * 1000, self.finalisation)

    def save_text(self, text, newline=True, print_=True):
        # print in the console
        if print_:
            print(text)
        # and write in the file
        with open(self.filename, "a") as f:
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
        if self.pb is not None:
            self.fond.delete(self.racine, self.pb)

        self.pb = self.fond.create_rectangle(
            self.progr,
            self.h / 1.2,
            self.w - 425,
            self.h / 1.2 + 30,
            fill="white",
            width="1",
        )

    def start_new_combinaison(self):
        self.comb = []
        self.numclic = 0

        self.draw_circles()

        self.tapp = time.perf_counter()
        self.fond.bind("<ButtonPress-1>", self.clic)

    def clic(self, event):
        # Parcours la liste de cercles jusqu'à trouver le bon, ou alors c'est à côté.
        for idx, circle in enumerate(self.circles):
            if (circle.x_min <= event.x <= circle.x_max) and (circle.y_min <= event.y <= circle.y_max):
                self.ellipse[idx] = self.fond.create_oval(circle.coords, fill="grey40", width="5")
                self.save_text("{}".format(circle.coords), newline=False, print_=False)
                self.verifcercle(idx)
                break
        else:
            coordclicx = self.fond.winfo_pointerx()
            coordclicy = self.fond.winfo_pointery()
            self.save_text("[{}, {}".format(coordclicx, coordclicy), newline=False, print_=False)
            self.acote()

    def verifcercle(self, idx: int):
        if idx in self.comb:
            self.after(100, self.memecercle)
        elif self.circles[idx].color == "blue":
            self.after(100, self.erreur, "bleu")
        elif self.circles[idx].color == "red":
            self.after(100, self.erreur, "rouge")
        else:
            self.numclic += 1
            self.comb.append(idx)
            self.comb.sort()

            if self.numclic < 4:
                self.fond.bind("<Button-1>", self.clic)
            else:
                print("Combi:{}".format(self.comb))

                if self.comb in self.combi:
                    self.after(100, self.dejafait)
                else:
                    self.after(100, self.reussite)

    def reussite(self):
        self.counter.add_reussite()

        self.combi.append(self.comb)

        tclic = time.perf_counter()

        self.RT = tclic - self.tapp
        self.RTmax = max(self.RTmax, self.RT)
        self.RTmin = min(self.RTmin, self.RT)

        print("RT sec={}\n".format(self.RT))
        self.save_text("[Nouvelle combi[", newline=False, print_=False)
        self.save_text("{}".format(self.RT), print_=False)
        self.SRT += self.RT

        self.progr += DELTA_PROGRESSION

        self.draw_progression()

        if self.counter.NR % N_REUSSITE_AVANT_SON == 0:
            winsound.PlaySound(SON_PIECES, winsound.SND_FILENAME | winsound.SND_ASYNC)

        self.start_new_combinaison()

    def erreur(self, couleur):
        self.counter.add_error()

        text = "[" * (4 - self.numclic)
        text += "Distracteur {}".format(couleur)
        self.save_text(text, print_=False)

        self.start_new_combinaison()

    def memecercle(self):
        self.counter.add_meme_cercle()

        text = "[" * (4 - self.numclic)
        text += "Meme cercle"
        self.save_text(text, print_=False)

        self.start_new_combinaison()

    def dejafait(self):
        self.counter.add_meme_combinaison()

        tclic = time.perf_counter()

        self.RTdejafait = tclic - self.tapp
        self.SRTdejafait += self.RTdejafait

        self.save_text("[Combi déjà faite[", newline=False, print_=False)
        self.save_text("{}".format(self.RTdejafait), print_=False)

        self.start_new_combinaison()

    def acote(self):
        self.counter.add_a_cote()

        text = "[" * (4 - self.numclic)
        text += "A cote"
        self.save_text(text, print_=False)

        self.start_new_combinaison()

    def start_chrono(self):
        self.save_text("\n30 sec")
        self.show_chrono()

    def show_chrono(self):
        if self.chrono is not None:
            self.fond.delete(self.racine, self.chrono)

        self.chrono = self.fond.create_text(
            self.x_mid,
            self.h / 8,
            text="{}".format(self.temps),
            font="Arial 120 bold",
            fill="black",
        )

        self.one_second = self.after(1000, self.elapse_second)

    def elapse_second(self):
        self.temps -= 1

        if self.temps > 0:
            self.show_chrono()
        else:
            self.fond.delete(self.racine, self.chrono)

    def finalisation(self):
        self.racine.after_cancel(self.one_second)

        self.fond.destroy()
        self.fond = tkinter.Canvas(self.racine, bg="white", width=self.w, height=self.h)
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
            taux = self.counter.NR / self.counter.total * 100
            if taux == 0:
                RTmoyreussi = 0
            else:
                RTmoyreussi = self.SRT / self.counter.NR

            if self.counter.ND == 0:
                RTmoydejafait = 0
                RTmoytot = RTmoyreussi
            else:
                RTmoydejafait = self.SRTdejafait / self.counter.ND
                RTmoytot = (self.SRT + self.SRTdejafait) / (self.counter.ND + self.counter.NR)

        self.save_text("\n\nBonnes reponses: %.2f" % self.counter.NR)
        self.save_text("Erreurs couleur: %.2f" % self.counter.NE)
        self.save_text("Erreurs repetition: %.2f" % self.counter.ND)
        self.save_text("Erreurs même cercle: %.2f" % self.counter.MC)
        self.save_text("Erreurs à côte: %.2f" % self.counter.AC)
        self.save_text("Erreurs totales: {}".format(self.counter.NET))
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
    os.mkdir(maindir)

    app = SDf(nom, None)
    app.title("My application")
    app.destroy()
    app.mainloop()
