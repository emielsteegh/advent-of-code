""" This script runs archived aoc challenges
in the main folder run `ptyhon prev.py -d x` to run day x
"""

import click
from os import walk
from os.path import split, join


@click.group()
def cli():
    pass

@click.command(help="picks a script from the archive and runs it")
@click.option('-d', '--day', 'day', type=int, prompt=True, help="| AoC day  | prompted")
@click.option('-y', '--year', 'year', type=int, default=None, help="| AoC year | defaults to highest year available")
def old(day, year):
    if year is None:
        dirs = next(walk(split(__file__)[0]))[1]
        year_dirs = [int(d) for d in dirs if d.isnumeric()]
        year = max(year_dirs)
    # run the correct script by importing it
    __import__(f"{year}.{int(day):02}")

@cli.command()
@click.argument('day')
@click.argument('year')
@click.argument('clear', default = False)
def save(day, year, clear):
    # move file to year/in/day.txt
    from shutil import copyfile

    script_src = "now.py"
    script_dst = join(year, f"{day}.py")
    copyfile(script_src, script_dst)
     
    text_src = "now.txt"
    text_dst = join(year, "in", f"{day}.txt")
    copyfile(text_src, text_dst)
    # empty file
    if clear:
        open(script_src, 'w').close()
        open(text_dst, 'w').close()

@cli.command()
@click.argument('day')
@click.argument('year')
def retrieve(day, year):
    # TODO comm to move file from storage to 
    pass

@cli.command()
def now():
    print("now!")

if __name__ == "__main__":
    cli()