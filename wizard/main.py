import click
from wizard.server import app

@click.group()
def cli():
    pass

@click.command()
def server():
    app.run("0.0.0.0", 8040)

@click.command()
def add_file():
    click.echo('Add text file')

cli.add_command(server)
cli.add_command(add_file)
