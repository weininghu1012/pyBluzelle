# pyBluzelle

## About pyBluzelle

pyBluzelle is a python client for developing Python applications that can connect to Bluzelle SwarmDB and perform all standard operations.

## Getting Started

1. Install [Python 3.6](https://www.python.org/downloads/release/python-360/)

2. Follow the instruction of deploying SwarmDB on Docker: https://github.com/bluzelle/swarmDB

3. Get our client code (https://github.com/weininghu1012/pyBluzelle)

4. Run `pip3 setup.py install` under the `pyBluzelle` directory

5. Try it in the python interpreter

```
>>> import pyBluzelle
>>> b = pyBluzelle.create_connection("127.0.0.1", 51011, "137a8403-52ec-43b7-8083-91391d4c5e67")
>>> b.create("kk","1234")
True
>>> b.read("kk")
'1234'
```

## Testing Locally

run `python3 test/test_create.py` in the `pyBluzelle` directory

## List of API
create an key value pair, return false if the key exists, return true if success.
```
create(key, value)
```
update the key with the value, return false if the key does not exist, return true if success.
```
update(key, value)
```
return the value of the key, return None if key does not exist.
```
read(key)
```
delete key, return false if the key does not exist, return true if success.
```
delete(key)
```
return false if the key does not exist, return true if success.
```
has(key)
```
return the list of the keys in the DB
```
keys()
```
