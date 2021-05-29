import click
import requests as r
from pathlib import Path

from wizard.server import app
from wizard import utils
from wizard import term

@click.group()
def cli():
    pass

@click.command()
@click.option("--host", default="127.0.0.1", help="Server host")
@click.option("--port", default="8040", help="Server port")
def server(host, port):
    Path('wizard/audio').mkdir(parents=True, exist_ok=True)
    app.run(host, port, debug=True)

@click.command()
def init():
    ip = input("Type in host and port of server: ")
    try:
        d = utils.json_to_dict("data.json")
    except:
        d = {}
    d["server"] = ip
    utils.dict_to_json(d, "data.json")
    click.echo(f'Saved configuration.')

@click.command()
@click.argument('file')
def add(file):
    text = utils.file_to_text(file)
    file_name = utils.get_file_name(file)
    url = utils.get_url()
    if url:
        res = r.post(f'http://{url}/add-file', json={"text":text, "file_name":file_name})
        if res.json().get("message") == "OK":
            click.echo(f'Added {file} to audio list.')
        else:
            click.echo("Error occurred.")
    else:
        click.echo("Error occurred.")

@click.command()
@click.argument('name')
def playlist(name):
    url = utils.get_url()
    res = r.get(f'http://{url}/files')
    files = res.json().get("files")
    if files:
        selected = term.multi_select(files, "Select audio files to add to playlist: ")
        if selected:
            r.post(f"http://{url}/add-playlist", json={"name" : name, "files" : selected})
            click.echo(f"Added new playlist: {name}")
        else:
            click.echo("Error occurred.")
    else:
        click.echo("Error occurred.")

cli.add_command(init)
cli.add_command(playlist)
cli.add_command(server)
cli.add_command(add)
