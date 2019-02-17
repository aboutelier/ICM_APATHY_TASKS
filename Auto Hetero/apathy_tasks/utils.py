import pickle
from os.path import join as joinpath
from functools import partial
from functools import update_wrapper


def classe_partielle(func, *args, **kwargs):
    partial_func = partial(func, *args, **kwargs)
    update_wrapper(partial_func, func)
    return partial_func


def get_pace_from_file(name, workdir, category):
    filename = joinpath(
        workdir,
        "{}_pace_{}.pkl".format(name, category)
    )
    with open(filename, 'rb') as f:
        pace = pickle.load(f)

    return pace
