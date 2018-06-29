import logging
from pyBluzelle.communication import Connection

__version__ = (0, 1, 0)


def create_connection(host, port, uuid):
    return Connection(host, port, uuid)


def get_version():
    return '.'.join(str(bit) for bit in __version__[:3])


# Be nice and set up logging to /dev/null
class NullHandler(logging.Handler):
    def emit(self, record):
        pass

log = logging.getLogger('pyBluzelle')
log.addHandler(NullHandler())
