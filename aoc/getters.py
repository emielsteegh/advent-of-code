from os.path import join, basename
import inspect
import re

NOWPY = "now.py"
NOWIN = "now.txt"


def lines(as_list=True):
    '''
    based on the path of the calling script (not this one),
    returns the input of the matching advent of code day as lines
    if called by now.py returns the content of now.txt
    if called by an archived date.py will return the content of that date.txt
    '''
    fname = None
    caller = inspect.stack()  # [1].filename
    caller = [stack.filename for stack in caller]
    caller = next((c for c in caller if c is not caller[0]), None)

    if basename(caller) == "now.py":
        fname = NOWIN
    else:
        # the idea is that from the path we get the in txt
        caller = caller.split("/")
        fname = join(caller[-2], "in", caller[-1][:-2]+"txt")
        pass
    f = open(fname, "r")
    if as_list:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
    else:
        lines = f.read()
    return lines


def string_to_numbers(s: str, delimiter: str = ','):
    # start with or without -, <0 digits, with or without a single delmiter character followed by <0 digits
    if delimiter not in ['.', ',', None]:
        raise Exception("Delimiter must be ',' or '.' or None")

    re_numbers = re.compile(
        f'(-?\d+(?:\{delimiter}\d+)?)' if delimiter != None else f'(-?\d+)')

    def convert(x): return float(x.replace(",", ".")
                                 ) if delimiter != None else int(x)  # ! not very effcient
    numbers_in_string = [(convert(x)) for x in re.findall(re_numbers, s)]
    return numbers_in_string


def numbers(delimiter: str = ',', keep_empty=True):
    '''takes the appropriate input to a script,
     uses simple regex to convert them to a list of numbers per line'''

    ls = lines()
    # returns all lines as a list of the numbers in it
    numbers = [string_to_numbers(s=line, delimiter=delimiter)
               for line in ls if (keep_empty or line != '')]
    return numbers
