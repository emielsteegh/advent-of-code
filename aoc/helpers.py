from os.path import join, exists
from os import remove
from sys import exit
from functools import wraps
import re
import time


def if_exists(day, year, force: bool = False):
    scr, inp = get_fnames(day, year)
    scr_exist = exists(scr)
    inp_exist = exists(inp)
    if not force and (scr_exist or inp_exist):
        exit(
            f"""
        Error! Stopped archiving operation!
        {scr} {"already exists" if scr_exist else "does not yet exist"}
        {inp} {"already exists" if inp_exist else "does not yet exist"}
        pass -F to force overwrite or remove them manually\n"""
        )
    elif force:
        if scr_exist:
            remove(scr)
            print(f"Removed {scr}")
        if inp_exist:
            remove(inp)
            print(f"Removed {inp}")


def get_fnames(day, year):
    """returns filenames of script and input for day, year"""
    script_fname = join(str(year), f"{day}.py")
    input_fname = join(str(year), "in", f"{day}.txt")

    return script_fname, input_fname


def string_to_numbers(s: str, delimiter: str = ","):
    # start with or without -, <0 digits, with or without a single delmiter character followed by <0 digits
    if delimiter not in [".", ",", None]:
        raise Exception("Delimiter must be ',' or '.' or None")

    re_numbers = re.compile(
        f"(-?\d+(?:\{delimiter}\d+)?)" if delimiter != None else f"(-?\d+)"
    )
    convert = (
        lambda x: float(x.replace(",", ".")) if delimiter != None else int(x)
    )  # ! not very effcient
    numbers_in_string = [(convert(x)) for x in re.findall(re_numbers, s)]
    return numbers_in_string


def timed(func):
    @wraps(func)
    def timed_wrapper(*args, **kwargs):
        pre = time.perf_counter()
        result = func(*args, **kwargs)
        post = time.perf_counter()
        elapsed_time = post - pre
        print(
            f"-> {func.__name__}({args}, {kwargs}) ran in: {elapsed_time:0.5f} seconds"
        )
        return result

    return timed_wrapper
