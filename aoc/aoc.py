from os.path import exists, join, basename, splitext
import inspect
import re

import click

NOWPY = "now.py"
NOWIN = "now.txt"


def lines():
    fname = None
    caller = inspect.stack()[1].filename

    if basename(caller) == "now.py":
        fname = NOWIN
    else:
        # the idea is that from the path we get the in txt
        pass
    f = open(fname, "r")
    lines = f.readlines()
    return lines

def numbers():
    # returns all lines as a list of the numbers in it
    lines = lines()
    numbers = [re.findall(r'\d+',line) for line in lines]
    return numbers