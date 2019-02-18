import os
import sys
from random import sample
from os.path import join as joinpath

from Auto import Auto
from Hetero import Hetero
from SpatialeFacile import SpatialeFacile
from SpatialeDifficile import SpatialeDifficile
from utils import classe_partielle
from utils import get_pace_from_file
from config import ApathyTasksConfiguration

MAINDIR = "C:\\Users\\ECOCAPTURE\\Desktop\\ECOCAPTURE\\ICM_APATHY_TASKS"

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


def get_average_pace(name, workdir):
    pace_faible = get_pace_from_file(name, workdir, 'faible')
    pace_fort = get_pace_from_file(name, workdir, 'fort')

    return (pace_faible + pace_fort) / 2


def run_app(task, *args, **kwds):
    app = task(*args, **kwds)
    app.title(task.__name__)
    app.mainloop()


def main(name, maindir):
    config = ApathyTasksConfiguration(maindir)
    workdir = joinpath(config.subject_dir, name)
    task_filename = "liste_ordonnee_des_taches_{}.txt".format(name)

    if not os.path.exists(config.subject_dir):
        os.mkdir(config.subject_dir)

    try:
        os.mkdir(workdir)
    except FileExistsError:
        sys.exit("Subject name already exists. Try again with a different name.")

    task_order = []

    for task in sample(FIRST_TASK_LIST, len(FIRST_TASK_LIST)):
        task_order.append(task.__name__)
        run_app(task, name, config)

    try:
        pace = get_average_pace(name, workdir)
    except FileNotFoundError:
        sys.exit("Probleme d'enregistrement du temps de réponse.")
    except EOFError:
        sys.exit("Le fichier du temps de réponse moyen est vide.")

    pace_msg = "Temps de réponse moyen measuré : {} secs\n".format(pace)
    if pace > config.max_response_time:
        pace = config.max_response_time
        pace_msg += "La valeur est coupée car elle ne peut pas {} secs\n".format(config.max_response_time)

    for task in sample(SECOND_TASK_LIST, len(SECOND_TASK_LIST)):
        task_order.append(task.__name__)
        run_app(task, name, config, pace=pace)

    with open(joinpath(workdir, task_filename), 'a') as f:
        f.write("Ordre des différentes tâches :\n")
        f.write("\n".join(task_order))
        f.write("\n")
        f.write(pace_msg)


if __name__ == "__main__":
    name = input("Nom du sujet : ")
    main(name, MAINDIR)
