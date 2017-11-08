import click

from ttools import bnu, heart, remover


@click.command()
@click.argument('mode')
def cli(mode):
    mode_map = {
        'bnu': bnu.main,
        'heart': heart.main,
        'remover': remover.main,
    }
    if mode not in mode_map:
        exit(1)

    return mode_map[mode]()


if __name__ == '__main__':
    cli()
