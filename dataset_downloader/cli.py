import click
import json
from dataset_downloader.downloader import run


def validateConfig(config):
    if config['ratio'] > 1:
        raise Exception('Ratio can\'t be bigger than 1')


@click.command()
@click.option('--processes', default=8, help="Number of processes")
def cli(processes):
    try:
        with open('dataset.json') as f:
            config = json.load(f)
        validateConfig(config)
        run(config, processes)
    except FileNotFoundError:
        print('Config file dataset.json not found')
