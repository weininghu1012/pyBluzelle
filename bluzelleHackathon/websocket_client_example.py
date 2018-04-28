from websocket import create_connection
import json

c = create_connection("ws://127.0.0.1:51012")

data = {
  "bzn-api": "crud",
  "cmd": "create",
  "data": {
      "key": "myKey",
      "value": "I2luY2x1ZGUgPG1vY2tzL21vY2tfbm9kZV9iYXNlLmhwcD4NCiNpbmNsdWRlIDxtb2Nrcy9tb2NrX3Nlc3Npb25fYmFzZS5ocHA+DQojaW5jbHVkZSA8bW9ja3MvbW9ja19yYWZ0X2Jhc2UuaHBwPg0KI2luY2x1ZGUgPG1vY2tzL21vY2tfc3RvcmFnZV9iYXNlLmhwcD4NCg=="
  },
  "db-uuid": "137a8403-52ec-43b7-8083-91391d4c5e67",
  "request-id": 33
}


c.send(json.dumps(data))        # dict object to json string
ret = c.recv()
ret = eval(ret)                 # json string to object

print(ret['error'])             # get error code
