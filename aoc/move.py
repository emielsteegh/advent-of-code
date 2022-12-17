import click
from os import join

@click.group()
def cli():
    pass

@cli.command()
@click.argument('day')
@click.argument('year')
@click.argument('clear', default = False)
def save(day, year, clear):
    # move file to year/in/day.txt
    from shutil import copyfile

    src_in = "in.txt"
    dst_in = join(year, "in", f"{day}.txt")
    copyfile(src_in, dst_in)
    src_in = "now.py"
    dst_in = join(year, f"{day}.py")
    copyfile(src_in, dst_in)
    # empty file
    if clear:
        open(src_in, 'w').close()
        open(src, 'w').close()

@cli.command()
@click.argument('day')
@click.argument('year')
def retrieve(day, year):
    # TODO comm to move file from storage to 
    pass

if __name__ == '__main__':
    cli()