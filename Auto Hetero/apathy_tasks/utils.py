from functools import partial
from functools import update_wrapper


def classe_partielle(func, *args, **kwargs):
    partial_func = partial(func, *args, **kwargs)
    update_wrapper(partial_func, func)
    return partial_func
