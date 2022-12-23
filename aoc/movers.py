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

if __name__ == '__main__':
    cli()