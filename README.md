# pyBluzelle

## About pyBluzelle

pyBluzelle is a python client for developing Python applications that can connect to Bluzelle SwarmDB and performs all standard CRUD operations.

## Getting Started

1. Install [Python 3.6](https://www.python.org/downloads/release/python-360/)

2. Follow the instruction of deploying SwarmDB on Docker: https://github.com/bluzelle/swarmDB

3. Get our client code (https://github.com/weininghu1012/pyBluzelle)

4. Run `pip3 setup.py install` under the `pyBluzelle` directory

## Create a connection

1. Run `python3` in your terminal

2. Run `import pyBluzelle`

3. Run `my_connection = pyBluzelle.create_connection(localhostIP, port, UUID)`

4. Ready for test


## Testing Locally

run `python3 test/test_create.py` in the `pyBluzelle` directory


## Javascript API reference
[websocketAPI](https://bluzelle.github.io/api/#js-api)
