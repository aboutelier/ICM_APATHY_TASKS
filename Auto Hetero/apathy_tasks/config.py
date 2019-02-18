from os.path import join as joinpath


class ApathyTasksConfiguration(object):
    def __init__(self, maindir):
        self.maindir = maindir
        self.subject_dir = joinpath(maindir, "Sujets")

        # Images
        # ------
        image_dir = joinpath(maindir, "Image")
        self.img_jauge = joinpath(image_dir, "jauge.ppm")
        self.img_jauge_auto = joinpath(image_dir, "jaugedouble2.ppm")
        self.img_pieces_faible = joinpath(image_dir, "pieces.ppm")
        self.img_pieces_fort = joinpath(image_dir, "pieces2.ppm")

        # Son
        # ---
        sound_dir = joinpath(maindir, "Son")
        self.son_cash = joinpath(sound_dir, "Cash.wav")
        self.son_pieces = joinpath(sound_dir, "Pièces.wav")
        self.son_metronome = joinpath(sound_dir, "Metronome.wav")
        self.son_perte = joinpath(sound_dir, "Son_Perte1.wav")

        # Timing (en secondes)
        # --------------------
        # Temps total pour les taches
        self.test_time_spatial = 30
        self.test_time_auto = 30
        # Durée du chrono à la fin des taches
        self.end_timer = 10
        # Temps de latence entre les taches
        self.summary_time = 5
        # Temps de réponse maximal utilisé pour les taches Auto/Hetero
        self.max_response_time = 5

        # Autres parametres
        # -----------------
        self.csv_separator = ";"

