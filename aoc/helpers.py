from os.path import join, exists
from os import remove
from sys import exit


def if_exists(day, year, force:bool=False):
    scr, inp = get_fnames(day, year)
    scr_exist = exists(scr)
    inp_exist = exists(inp)
    if not force and (scr_exist or inp_exist):
        exit(f"""
        Error! Stopped archiving operation!
        {scr} {"already exists" if scr_exist else "does not yet exist"}
        {inp} {"already exists" if inp_exist else "does not yet exist"}
        pass -F to force overwrite or remove them manually\n""")
    elif force:
        if scr_exist: 
            remove(scr)
            print(f"Removed {scr}")
        if inp_exist: 
            remove(inp)
            print(f"Removed {inp}")

def get_fnames(day, year):
    """returns filenames of script and input for day, year"""
    script_fname  = join(str(year), f"{day}.py")
    input_fname = join(str(year), "in", f"{day}.txt")

    return script_fname, input_fname