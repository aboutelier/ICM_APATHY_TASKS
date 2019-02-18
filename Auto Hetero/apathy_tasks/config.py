from os.path import join as joinpath


class ApathyTasksConfiguration(object):
    def __init__(self, maindir):
        self.maindir = maindir
        self.subject_dir = joinpath(maindir, "Sujets")

        # Images
        image_dir = joinpath(maindir, "Image")
        self.img_jauge = joinpath(image_dir, "jauge.ppm")
        self.img_jauge_auto = joinpath(image_dir, "jaugedouble2.ppm")
        self.img_pieces_faible = joinpath(image_dir, "pieces.ppm")
        self.img_pieces_fort = joinpath(image_dir, "pieces2.ppm")

        # Sound
        sound_dir = joinpath(maindir, "Son")
        self.son_cash = joinpath(sound_dir, "Cash.wav")
        self.son_pieces = joinpath(sound_dir, "Pièces.wav")
        self.son_metronome = joinpath(sound_dir, "Metronome.wav")
        self.son_perte = joinpath(sound_dir, "Son_Perte1.wav")

        # Timing in seconds
        self.test_time_spatial = 10
        # self.test_time_spatial = 180
        self.test_time_auto = 10
        # self.test_time_auto = 120
        self.end_timer = 5
        # self.end_timer = 30
        self.summary_time = 5
        # self.summary_time = 15

        # Other parameters
        self.csv_separator = ";"
