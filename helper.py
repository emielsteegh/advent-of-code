""" This script runs archived aoc challenges
in the main folder run `ptyhon prev.py -d x` to run day x
"""

import click
from os import walk
from os.path import split, join
from aoc import helpers


def get_year_or_default_year(year):
    if year is None:
        dirs = next(walk(split(__file__)[0]))[1]
        year_dirs = [int(d) for d in dirs if d.isnumeric()]
        return max(year_dirs)
    else:
        return year


@click.group()
def cli():
    pass


@click.command(help="picks a script from the archive and runs it")
@click.option('-d', '--day', 'day', type=int, prompt=True, help="| AoC day  | prompted")
@click.option('-y', '--year', 'year', type=int, default=None, help="| AoC year | defaults to highest year available")
def old(day, year):
    year = get_year_or_default_year(year=year)
    # run the correct script by importing it
    __import__(f"{year}.{int(day):02}")


@cli.command()
@click.option('-d', '--day', 'day', type=int, prompt=True, help="| AoC save day  | prompted")
@click.option('-y', '--year', 'year', type=int, default=None, help="| AoC save year | defaults to highest year available")
@click.option('-F', 'force', is_flag=True, help="Will overwrite existing files")
@click.option('-C', 'clear', is_flag=True, help="Clear the now files")
def save(day, year, force, clear):
    """move file to archive"""
    year = get_year_or_default_year(year=year)
    helpers.if_exists(day, year, force)

    from shutil import copyfile

    script_src, text_src = "now.py", "now.txt"
    script_dst, text_dst = helpers.get_fnames(day, year)

    copyfile(script_src, script_dst)
    copyfile(text_src, text_dst)

    if clear:
        # TODO probably better to copy a template file
        f = open(script_src, 'w')
        f.write("from aoc import *\n\n")
        f.close()
        open(text_src, 'w').close()


@cli.command()
@click.argument('day')
@click.argument('year')
def retrieve(day, year):
    # TODO comm to move file from storage to
    pass


@cli.command()
@click.option('-C', 'clear', is_flag=True, help="Clear the now files")
def now(clear):
    exit(" This funciton is not yet available")
    pass


if __name__ == "__main__":
    cli()
