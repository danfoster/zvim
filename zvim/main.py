import click
import fabric

from .utils import get_distro


@click.group()
def main(host):
    print(get_distro())


@main.command()
def install():
    pass


@main.command()
@click.argument("host")
def remoteinstall(host):
    pass


if __name__ == "__main__":
    main()
