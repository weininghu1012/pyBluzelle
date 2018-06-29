# pyBluzelle


## About pyBluzelle

pyBluzelle is a python client for developing Python applications that can connect to Bluzelle SwarmDB and performs all standard CRUD operations. It is built on top of [WebSocket API](https://bluzelle.github.io/api/#websocket-api).

## Getting Started

1. Install [Python 2.7](https://www.python.org/download/releases/2.7/)

2. Follow the instruction of deploying SwarmDB on Docker: https://github.com/bluzelle/swarmDB

3. Get our client code (https://github.com/bluzelle/pyBluzelle)

4. Install the protobuf compiler

Ubuntu 

`apt-get install protobuf-compiler`

OSX

`brew install protobuf`

5. Run  protoc --python_out=./pyBluzelle/proto --proto_path=proto/proto bluzelle.proto database.proto audit.proto in the `pyBluzelle` directory

6. Run `pip install .` under the `pyBluzelle` directory

## Run in Interpreter

1. Run `python2.7` in your terminal

2. Run `import pyBluzelle`

3. Run `my_connection = pyBluzelle.create_connection(localhostIP, port, UUID)`

4. Ready for test

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

run `python2.7 test/test_connection` in the `pyBluzelle` directory

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

##Python CRUD Test App

Steps to run the Bluzelle SwarmDB test application in a Python Virtual Environment. **Ensure that you activate your virtualenv each time you want to run the application**.


##Install Virtual Environment


    $ sudo pip install virtualenv
    $ cd workspace
    $ virtualenv crud-app

## Activate Virtual Environment
    $ . ~/workspace/crud-app/bin/activate
    
## Install Dependencies

    (crud-app)$ pip install .
    (crud-app)$ pip install .

### Generate Protobuf Code
    (crud-app)$ cd ../workspace/swarmdb/scripts
    (crud-app)$ protoc --python_out=../scripts ./bluzelle.proto ./database.proto
    
### Run Script
    (crud-app)$ crud -h

## Javascript API reference
[JsAPI](https://bluzelle.github.io/api/#js-api)
