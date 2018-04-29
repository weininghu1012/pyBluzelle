from pyBluzelle.main import Bluzelle

def create_connection(host, port, uuid):
    return Bluzelle(host, port, uuid)