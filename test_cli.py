from app.app import add as _add
from pathlib import Path
import click
import json


def safe_open(path, mode):
    root = '/'.join(path.split('/')[:-1])
    Path(root).mkdir(parents=True, exist_ok=True)
    return open(path, mode)

@click.group()
def cli():
    pass

@cli.command()
@click.option('-n', '--name', type=str, help='Name to greet', default='World')
def hello(name):
    click.echo(f'Hello {name}')

@cli.command()
@click.option('-a', type=int, help='first number to add')
@click.option('-b', type=int, help='second number to add')
def add(a, b):
    answer = _add(a, b)
    click.echo(f'{a} + {b} = {answer}')

@cli.command()
@click.option('-m', '--message', type=str, help='journal entry')
@click.option('-p', '--path', type=str, help='journal file path')
def entry(message, path):
    file = safe_open(path, 'a+')
    file.write(message + '\n')
    file.close()


@cli.command()
@click.option('-c', '--config_path', help='config file absolute path')
@click.option('-u', '--update', prompt=False)
def config(config_path, update):
    try:
        if update:
            config_file = safe_open(config_path, 'w')
            update = update.strip("\"\'").replace("\'","\"")
            print(update, )
            update = json.loads(update)
            print(update)
            update = json.dumps(update)
            print(update)
            config_file.write(update)
            config_file.close()
            click.echo("config updated")
        else:
            config_file = safe_open(config_path, 'r')
            config_obj = json.loads(config_file.read())
            config_file.close()
            click.echo(json.dumps(config_obj, indent=2))
    except: click.echo("config file does not exist, update env: YUZU_CONFIG_PATH")

click.echo('welcome to my test cli')
config(auto_envvar_prefix='YUZU')