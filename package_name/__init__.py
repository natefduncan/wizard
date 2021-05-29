import click

@click.group()
def cli():
    pass

@click.command()
def command1():
    click.echo('Command1')

@click.command()
def command2():
    click.echo('Command2')

cli.add_command(command1)
cli.add_command(command2)
