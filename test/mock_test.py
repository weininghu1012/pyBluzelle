import pyBluzelle
import unittest
from unittest import mock

class TestDatabase(unittest.TestCase):
	def setUp(self):
		self.connection = pyBluzelle.create_connection("127.0.0.1", 51011, "137a8403-52ec-43b7-8083-91391d4c5e67")
		self.connection.create('key1', '1234')



	def mock_read(self):
		success_read = mock.Mock(return_value = '1234')
		self.connection.read('key1') = success_read
    	self.assertEqual(self.connection.read('key1'), '1234')

if __name__ == '__main__':
    unittest.main()