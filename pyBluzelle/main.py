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
        self.ip = None
        self.uuid = ""

    def connect(self, host, port, uuid):
        self.host = host
        self.ip = 'ws://' + host + ':' + str(port)
        self.uuid = uuid
        self.payload = {
            "bzn-api": "crud",
            "cmd": None,
            "data": {},
            "db-uuid": self.uuid,
            "request-id": 0
        }

    def create(self,key,value):
        req = self.payload
        req["cmd"] = "create"
        req["data"]["key"] = key
        req["data"]["value"] = value
        # test if the workder nodes all get updated
        self.__sendRequest(req)
        self.__poll(self.read, key, value)

    def update(self,key,value):
        req = self.payload
        req["cmd"] = "update"
        req["data"]["key"] = key
        req["data"]["value"] = value
        self.__sendRequest(req)
        self.__poll(self.read, key, value)


    def read(self,key):
        req = self.payload
        req["cmd"] = "read"
        req["data"]["key"] = key
        return self.__sendRequest(req)

    def delete(self, key):
        req = self.payload
        req["cmd"] = "delete"
        req["data"]["key"] = key
        return self.__sendRequest(req)

    def has(self, key):
        pass

    def keys(self):
        

    def __poll(self, operation, key, value):
        pollRate = 200
        pollTimeout = 2000
        sleepTime = 0.1
        current_milli_time = lambda: int(round(time.time() * 1000))

        startTime = current_milli_time()
        while (current_milli_time() - startTime < pollTimeout):
            updatedObjectDic = operation(key)
            if ("data" in updatedObjectDic and updatedObjectDic["data"]["value"] == value):
                return 
            time.sleep(sleepTime)
            sleepTime = sleepTime*2
        raise TimeoutError("Time out for this operation")

    def __sendRequest(self, data):
        c = create_connection(self.ip)
        c.send(json.dumps(data))
        ret = c.recv()
        c.close()
        d = eval(ret)
        if 'error' in d and d['error'] == 'NOT_THE_LEADER':
            self.ip = 'ws://' + self.host + ':' + str(d['data']['leader-port'])
            self.__sendRequest(data)
        return d


