# import pyBluzelle
# import unittest
# from mock import
#
# class TestDatabase(unittest.TestCase):
# 	def setUp(self):
# 		self.connection = pyBluzelle.create_connection("127.0.0.1", 51011, "137a8403-52ec-43b7-8083-91391d4c5e67")
# 		self.connection.create('key1', '1234')
#
# 	def mock_read(self):
# 		success_read = mock.Mock(return_value = '1234')
# 		self.connection.read('key1') = success_read
#     	self.assertEqual(self.connection.read('key1'), '1234')
#
# if __name__ == '__main__':
#     unittest.main()main__':
#     unittest.main()


import websocket
import json
from pyBluzelle import Connection

from pyBluzelle.proto import database_pb2
from pyBluzelle.proto import bluzelle_pb2

from mockito import when
from mockito import mock
from mockito import ANY
from mockito import captor
from mockito import unstub
import unittest
import base64


class TestConnection(unittest.TestCase):

    test_uuid = "test_uuid"
    test_host = "localhost"
    test_port = "51010"

    test_redirect_host = "www.google.com"
    test_redirect_port = 42

    test_key = "test"
    test_key_other = "test_other"
    test_value = "value"

    def setUp(self):
        self.connection = Connection(TestConnection.test_host,
                                     TestConnection.test_port,
                                     TestConnection.test_uuid)

    def tearDown(self):
        pass

    def test_create(self):

        mocket = mock(websocket.WebSocket, strict=False)
        when(websocket).create_connection("ws://{}:{}".format(TestConnection.test_host,
                                                              TestConnection.test_port)).thenReturn(mocket)
        proto_captor = captor(ANY(str))
        when(mocket).send(proto_captor)

        msg = database_pb2.database_response()
        when(mocket).recv().thenReturn(msg.SerializeToString())

        self.assertIsNone(self.connection.create(TestConnection.test_key, TestConnection.test_value))

        self.assertIsNotNone(proto_captor.value)
        send_json = json.loads(proto_captor.value)
        self.assertIn('bzn-api', send_json)
        self.assertEquals(send_json['bzn-api'], 'database')
        msg = bluzelle_pb2.bzn_msg()
        msg.ParseFromString(base64.b64decode(send_json['msg']))
        self.assertEquals(msg.db.create.key, TestConnection.test_key)
        self.assertEquals(msg.db.create.value, TestConnection.test_value)
        self.assertEquals(msg.db.header.db_uuid, TestConnection.test_uuid)
        self.assertIsNotNone(msg.db.header.transaction_id)
        unstub()

    def test_read(self):

        mocket = mock(websocket.WebSocket, strict=False)
        when(websocket).create_connection("ws://{}:{}".format(TestConnection.test_host,
                                                              TestConnection.test_port)).thenReturn(mocket)
        proto_captor = captor(ANY(str))
        when(mocket).send(proto_captor)

        msg = database_pb2.database_response()
        msg.resp.value = TestConnection.test_value
        when(mocket).recv().thenReturn(msg.SerializeToString())

        self.assertEquals(self.connection.read(TestConnection.test_key), TestConnection.test_value)

        self.assertIsNotNone(proto_captor.value)
        send_json = json.loads(proto_captor.value)
        self.assertIn('bzn-api', send_json)
        self.assertEquals(send_json['bzn-api'], 'database')
        msg = bluzelle_pb2.bzn_msg()
        msg.ParseFromString(base64.b64decode(send_json['msg']))
        self.assertEquals(msg.db.read.key, TestConnection.test_key)
        unstub()

    def test_update(self):

        mocket = mock(websocket.WebSocket, strict=False)
        when(websocket).create_connection("ws://{}:{}".format(TestConnection.test_host,
                                                              TestConnection.test_port)).thenReturn(mocket)
        proto_captor = captor(ANY(str))
        when(mocket).send(proto_captor)

        msg = database_pb2.database_response()
        when(mocket).recv().thenReturn(msg.SerializeToString())

        self.assertIsNone(self.connection.update(TestConnection.test_key, TestConnection.test_value))

        self.assertIsNotNone(proto_captor.value)
        send_json = json.loads(proto_captor.value)
        self.assertIn('bzn-api', send_json)
        self.assertEquals(send_json['bzn-api'], 'database')
        msg = bluzelle_pb2.bzn_msg()
        msg.ParseFromString(base64.b64decode(send_json['msg']))
        self.assertEquals(msg.db.update.key, TestConnection.test_key)
        self.assertEquals(msg.db.update.value, TestConnection.test_value)
        unstub()

    def test_delete(self):

        mocket = mock(websocket.WebSocket, strict=False)
        when(websocket).create_connection("ws://{}:{}".format(TestConnection.test_host,
                                                              TestConnection.test_port)).thenReturn(mocket)
        proto_captor = captor(ANY(str))
        when(mocket).send(proto_captor)

        msg = database_pb2.database_response()
        msg.resp.value = TestConnection.test_value
        when(mocket).recv().thenReturn(msg.SerializeToString())

        self.assertIsNone(self.connection.delete(TestConnection.test_key))

        self.assertIsNotNone(proto_captor.value)
        send_json = json.loads(proto_captor.value)
        self.assertIn('bzn-api', send_json)
        self.assertEquals(send_json['bzn-api'], 'database')
        msg = bluzelle_pb2.bzn_msg()
        msg.ParseFromString(base64.b64decode(send_json['msg']))
        self.assertEquals(msg.db.delete.key, TestConnection.test_key)
        unstub()

    def test_has(self):

        mocket = mock(websocket.WebSocket, strict=False)
        when(websocket).create_connection("ws://{}:{}".format(TestConnection.test_host,
                                                              TestConnection.test_port)).thenReturn(mocket)
        proto_captor = captor(ANY(str))
        when(mocket).send(proto_captor)

        msg = database_pb2.database_response()
        msg.resp.has = True
        when(mocket).recv().thenReturn(msg.SerializeToString())

        self.assertTrue(self.connection.has(TestConnection.test_key))

        self.assertIsNotNone(proto_captor.value)
        send_json = json.loads(proto_captor.value)
        self.assertIn('bzn-api', send_json)
        self.assertEquals(send_json['bzn-api'], 'database')
        msg = bluzelle_pb2.bzn_msg()
        msg.ParseFromString(base64.b64decode(send_json['msg']))
        unstub()

    def test_keys(self):
        mocket = mock(websocket.WebSocket, strict=False)
        when(websocket).create_connection("ws://{}:{}".format(TestConnection.test_host,
                                                              TestConnection.test_port)).thenReturn(mocket)
        proto_captor = captor(ANY(str))
        when(mocket).send(proto_captor)

        keys = [TestConnection.test_key, TestConnection.test_key_other]

        msg = database_pb2.database_response()
        msg.resp.keys.extend(keys)

        when(mocket).recv().thenReturn(msg.SerializeToString())
        self.assertListEqual(list(self.connection.keys()), keys)

        self.assertIsNotNone(proto_captor.value)
        send_json = json.loads(proto_captor.value)
        self.assertIn('bzn-api', send_json)
        self.assertEquals(send_json['bzn-api'], 'database')
        msg = bluzelle_pb2.bzn_msg()
        msg.ParseFromString(base64.b64decode(send_json['msg']))
        unstub()

    def test_size(self):

        mocket = mock(websocket.WebSocket, strict=False)
        when(websocket).create_connection("ws://{}:{}".format(TestConnection.test_host,
                                                              TestConnection.test_port)).thenReturn(mocket)
        proto_captor = captor(ANY(str))
        when(mocket).send(proto_captor)

        msg = database_pb2.database_response()
        msg.resp.size = 42
        when(mocket).recv().thenReturn(msg.SerializeToString())

        self.assertEqual(self.connection.size(), 42)

        self.assertIsNotNone(proto_captor.value)
        send_json = json.loads(proto_captor.value)
        self.assertIn('bzn-api', send_json)
        self.assertEquals(send_json['bzn-api'], 'database')
        msg = bluzelle_pb2.bzn_msg()
        msg.ParseFromString(base64.b64decode(send_json['msg']))
        unstub()

    def test_redirect(self):

        mocket = mock(websocket.WebSocket, strict=False)
        when(websocket).create_connection("ws://{}:{}".format(TestConnection.test_host,
                                                              TestConnection.test_port)).thenReturn(mocket)
        proto_captor = captor(ANY(str))
        when(mocket).send(proto_captor)

        msg = database_pb2.database_response()
        msg.redirect.leader_host = TestConnection.test_redirect_host
        msg.redirect.leader_port = TestConnection.test_redirect_port

        when(mocket).recv().thenReturn(msg.SerializeToString())

        redirect_mocket = mock(websocket.WebSocket, strict=False)
        when(websocket).create_connection("ws://{}:{}".format(TestConnection.test_redirect_host,
                                                              TestConnection.test_redirect_port)).thenReturn(redirect_mocket)

        msg = database_pb2.database_response()
        msg.resp.value = TestConnection.test_value
        when(redirect_mocket).recv().thenReturn(msg.SerializeToString())

        self.assertEquals(self.connection.read(TestConnection.test_key), TestConnection.test_value)

        self.assertIsNotNone(proto_captor.value)
        send_json = json.loads(proto_captor.value)
        self.assertIn('bzn-api', send_json)
        self.assertEquals(send_json['bzn-api'], 'database')
        msg = bluzelle_pb2.bzn_msg()
        msg.ParseFromString(base64.b64decode(send_json['msg']))
        self.assertEquals(msg.db.read.key, TestConnection.test_key)
        unstub()