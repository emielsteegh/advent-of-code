""" This script runs archived aoc challenges
in the main folder run `ptyhon prev.py -d x` to run day x
"""

import click
from os import walk
from os.path import split
@click.group()
def cli():
    pass

@click.command(help="picks a script from the archive and runs it")
@click.option('-d', '--day', 'day', type=int, prompt=True, help="| AoC day  | prompted")
@click.option('-y', '--year', 'year', type=int, default=None, help="| AoC year | defaults to highest year available")
def aoc(day, year):
    if year is None:
        dirs = next(walk(split(__file__)[0]))[1]
        year_dirs = [int(d) for d in dirs if d.isnumeric()]
        year = max(year_dirs)
    # run the correct script by importing it
    __import__(f"{year}.{int(day):02}")

if __name__ == "__main__":
    aoc()