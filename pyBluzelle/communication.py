from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import websocket
import json
import logging
import base64
import sys
import random

try:
    from pyBluzelle.proto import bluzelle_pb2
    from pyBluzelle.proto import database_pb2
except ImportError as e:
    raise ImportError("{}\n\nTo generate Bluzelle protobuf modules:\n"
                      "\n"
                      "$ protoc --python_out=./pyBluzelle/proto --proto_path=proto/proto bluzelle.proto database.proto audit.proto\n".format(e.message))

logger = logging.getLogger(__name__)


class Connection(object):

    def __init__(self, host, port, uuid):
        """
        Create a connection to a Bluzelle database
        :param host: hostname for the Bluzelle node
        :param port: port of the Bluzelle node
        :param uuid: uuid of the database to connect
        """
        self._host = host
        self._port = port
        self._uuid = uuid

    def _send_request(self, host, port, msg):
        ws = websocket.create_connection("ws://{}:{}".format(host, port))
        msg.db.header.db_uuid = self._uuid
        msg.db.header.transaction_id = random.randint(1, sys.maxint)

        req = {}
        req["bzn-api"] = "database"
        req["msg"] = base64.b64encode(msg.SerializeToString())

        logger.debug("Sending: {}".format(msg))
        logger.debug("-" * 60 + '\n')
        var = json.dumps(req)
        ws.send(json.dumps(req))
        resp = database_pb2.database_response()
        resp.ParseFromString(ws.recv())

        if resp.WhichOneof('success') == 'redirect':
            host = resp.redirect.leader_host
            port = resp.redirect.leader_port
            logger.debug("redirecting to leader at {}:{}...\n".format(host, port))
            resp = self._send_request(host, port, msg)
        else:
            logger.debug("Response: \n{}".format(resp))
            logger.debug("-" * 60 + '\n')

        ws.close()

        return resp

    def create(self, key, value):
        """
        Create a new K/V
        :param key: New key to create
        :param value: New value to add to the key
        :return:
        """
        msg = bluzelle_pb2.bzn_msg()
        msg.db.create.key = key
        msg.db.create.value = value
        self._send_request(self._host, self._port, msg)

    def read(self, key):
        """
        Read a value at a key
        :param key: Key to read
        :return: value
        """
        msg = bluzelle_pb2.bzn_msg()
        msg.db.read.key = key
        resp = self._send_request(self._host, self._port, msg)
        return resp.resp.value

    def update(self, key, value):
        """
        Update a K/V
        :param key: Key to update
        :param value: Value to update
        :return:
        """
        msg = bluzelle_pb2.bzn_msg()
        msg.db.update.key = key
        msg.db.update.value = value
        self._send_request(self._host, self._port, msg)

    def delete(self, key):
        """
        Create a new K/V
        :param key: Key to delete
        :return:
        """
        msg = bluzelle_pb2.bzn_msg()
        msg.db.delete.key = key
        self._send_request(self._host, self._port, msg)

    def has(self, key):
        """
        Create a new K/V
        :param key: Key to test
        :return: true if key exists
        """
        msg = bluzelle_pb2.bzn_msg()
        msg.db.has.key = key
        resp = self._send_request(self._host, self._port, msg)
        return resp.resp.has

    def keys(self):
        """
        Query for all keys in a database
        :return: List of keys in the database
        """
        msg = bluzelle_pb2.bzn_msg()
        msg.db.keys.SetInParent()
        resp = self._send_request(self._host, self._port, msg)
        return resp.resp.keys

    def size(self):
        """
        Query for size of the database in bytes
        :return: Size of the database in bytes
        """
        msg = bluzelle_pb2.bzn_msg()
        msg.db.size.SetInParent()
        resp = self._send_request(self._host, self._port, msg)
        return resp.resp.size