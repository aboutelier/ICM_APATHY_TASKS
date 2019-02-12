import pickle
from random import sample
from os.path import join as joinpath

from Auto import Auto
from Hetero import Hetero
from SpatialeFacile import SpatialeFacile
from SpatialeDifficile import SpatialeDifficile
from utils import classe_partielle

SUBJECT_FOLDER = "C:\\Users\\ECOCAPTURE\\Desktop\\ECOCAPTURE\\ICM_APATHY_TASKS\\Sujets"

# Define appropriate tasks
# ------------------------
SpatialeFacileFort = classe_partielle(SpatialeFacile, gain_faible=False)
SpatialeFacileFaible = classe_partielle(SpatialeFacile, gain_faible=True)
SpatialeDifficileFort = classe_partielle(SpatialeDifficile, gain_faible=False)
SpatialeDifficileFaible = classe_partielle(SpatialeDifficile, gain_faible=True)

# Write the list of tasks to be proposed to the user
# --------------------------------------------------
FIRST_TASK_LIST = [
    SpatialeFacileFaible,
    SpatialeFacileFort,
    SpatialeDifficileFaible,
    SpatialeDifficileFort,
]

SECOND_TASK_LIST = [
    Hetero,
    Auto,
]

def get_pace_from_file(name, maindir, category):
    filename = joinpath(
        maindir,
        "{}_pace_{}.pkl".format(name, category)
    )
    with open(filename, 'rb') as f:
        pace = pickle.load(f)

    return pace


def get_average_pace(name, maindir):
    pace_faible = get_pace_from_file(name, maindir, 'faible')
    pace_fort = get_pace_from_file(name, maindir, 'fort')

    return (pace_faible + pace_fort) / 2


def main(name, maindir):
    seance_filename = joinpath(
        maindir,
        "liste_ordonnee_des_taches_{}.txt".format(name)
    )
    task_order = []

    for task in sample(FIRST_TASK_LIST, len(FIRST_TASK_LIST)):
        task_order.append(task.__name__)

        app = task(None, name, SUBJECT_FOLDER)
        app.title("my application")
        app.destroy()
        app.mainloop()

    pace = get_average_pace(name, maindir)

    for task in sample(SECOND_TASK_LIST, len(SECOND_TASK_LIST)):
        task_order.append(task.__name__)

        app = task(None, name, SUBJECT_FOLDER, pace)
        app.title("my application")
        app.destroy()
        app.mainloop()

    with open(seance_filename, 'a') as f:
        f.write("Ordre des différentes tâches :\n")
        f.write("\n".join(task_order))


if __name__ == "__main__":
    name = input("Nom du sujet :")
    maindir = joinpath(SUBJECT_FOLDER, name)

    try:
        import os
        os.mkdir(maindir)
    except FileExistsError:
        import sys
        sys.exit("Subject name already exists. Try again with a different name.")

    main(name, maindir)
