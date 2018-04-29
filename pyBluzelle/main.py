from websocket import create_connection
import json
import time


# example form:
"""
data = {
    "bzn-api": "crud",
    "cmd": None,
    "data": {
        "key": None,
        "value": None
    },
    "db-uuid": None,
    "request-id": None
}
"""



class Bluzelle:

    def __init__(self):

        self.c = None
        self.uuid = ""

        pass

    def connect(self,ip,uuid):
        self.c = create_connection(ip)
        self.uuid = uuid
        pass

    def create(self,key,value):
        data = {
            "bzn-api": "crud",
            "cmd": "create",
            "data": {
                "key": key,
                "value": value
            },
            "db-uuid": self.uuid,
            "request-id": 33
        }

        self.c.send(json.dumps(data))  # dict object to json string
        ret = self.c.recv()
        ret = eval(ret)  # json string to object

        print(ret)
        # print(ret['error'])  # get error code
        pass

    def update(self,key,value):
        data = {
            "bzn-api": "crud",
            "cmd": "update",
            "data": {
                "key": key,
                "value": value
            },
            "db-uuid": self.uuid,
            "request-id": 33
        }

        self.c.send(json.dumps(data))  # dict object to json string
        ret = self.c.recv()
        ret = eval(ret)  # json string to object
        # add polling part to check if value is changed within timeout

        print(ret)
        # print(ret['error'])  # get error code

        pass

    def read(self,key):
        data = {
            "bzn-api": "crud",
            "cmd": "read",
            "data": {
                "key": key,
            },
            "db-uuid": self.uuid,
            "request-id": 33
        }

        self.c.send(json.dumps(data))  # dict object to json string
        ret = self.c.recv()
        ret = eval(ret)  # json string to object

        print(ret)
        # print(ret['error'])  # get error code

        pass

    def delete(self, key):
        data = {
            "bzn-api": "crud",
            "cmd": "delete",
            "data": {
                "key": key,
            },
            "db-uuid": self.uuid,
            "request-id": 33
        }

        self.c.send(json.dumps(data))  # dict object to json string
        ret = self.c.recv()
        ret = eval(ret)  # json string to object

        print(ret)
        # print(ret['error'])  # get error code
        pass

    def has(self, key):
        pass

    def keys(self):
        pass

    def poll(self, operation, key, value):
        pollRate = 200; //ms
        pollTimeout = 2000;
        sleepTime = 2
        current_milli_time = lambda: int(round(time.time() * 1000))


        startTime = current_milli_time()
        while (current_milli_time() - startTime < pollTimeout):
            if (operation(key) == value):
                return 
            time.sleep(sleepTime)
            sleepTime = sleepTime*2
        raise TimeoutError("Time out for this operation")




b = Bluzelle()
b.connect("ws://127.0.0.1:51012","137a8403-52ec-43b7-8083-91391d4c5e67")
# b.create("gg","1234")
# b.update("gg","4321")
# b.read("gg")
# b.delete("gg")