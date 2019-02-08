from random import shuffle
from functools import partial
from os.path import join as joinpath

from apathy_tasks import Auto
from apathy_tasks import Hetero
from apathy_tasks import SpatialeFacile
from apathy_tasks import SpatialeDifficile


SUBJECT_FOLDER = "C:\\Users\\ECOCAPTURE\\Desktop\\ECOCAPTURE\\ICM_APATHY_TASKS\\Sujets"

# Define appropriate tasks
# ------------------------
SpatialeFacileFort = partial(SpatialeFacile, gain_faible=False)
SpatialeFacileFaible = partial(SpatialeFacile, gain_faible=True)
SpatialeDifficileFort = partial(SpatialeDifficile, gain_faible=False)
SpatialeDifficileFaible = partial(SpatialeDifficile, gain_faible=True)

# Write the list of tasks to be proposed to the user
# --------------------------------------------------
FIRST_TASK_LIST = shuffle([
    SpatialeFacileFaible,
    SpatialeFacileFort,
    SpatialeDifficileFaible,
    SpatialeDifficileFort,
])

SECOND_TASK_LIST = shuffle([
    Hetero,
    Auto,
])

TASK_ORDER = [task.__name__ for task in FIRST_TASK_LIST + SECOND_TASK_LIST]


def main(name, maindir):
    seance_filename = joinpath(
        maindir,
        "liste_ordonnee_des_taches_{}.txt".format(name)
    )
    with open(seance_filename, 'a') as f:
        f.write("Ordre des différentes tâches :\n")
        f.write("\n".join(TASK_ORDER))

    for task in FIRST_TASK_LIST:
        app = task(None, name, maindir)
        app.title("my application")
        app.destroy()
        app.mainloop()

    pace = 0

    for task in SECOND_TASK_LIST:
        app = task(None, name, maindir, pace)
        app.title("my application")
        app.destroy()
        app.mainloop()


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