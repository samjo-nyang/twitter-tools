import click

from ttools import bnu, remover


@click.command()
@click.argument('mode')
def cli(mode):
    mode_map = {
        'bnu': bnu.main,
        'remover': remover.main,
    }
    if mode not in mode_map:
        exit(1)

    return mode_map[mode]()


if __name__ == '__main__':
    cli()
