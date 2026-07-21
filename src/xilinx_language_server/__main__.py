from . import __name__ as NAME
from . import __version__
from .server import XilinxLanguageServer as Server


def main():
    server = Server(NAME, __version__)
    server.start_io()


if __name__ == "__main__":
    main()
