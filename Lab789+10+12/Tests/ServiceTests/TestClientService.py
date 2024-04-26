'''
Created on Dec 2, 2023

@author: Cristian
'''
import unittest
from random import seed
from Domain.Entities import Client
from Controller.Client_controller import ServiceClient
from Repository.ClientRepository import ClientRepository
from Domain.Validators import CRUDErrors, ClientValidator, RepositoryError

class TestCaseClientService(unittest.TestCase):
    def setUp(self):
        self.test_clients = ClientRepository(ClientValidator())
        self.test_service = ServiceClient(self.test_clients)
    
    def testAddClient(self):
        self.test_service.add_client(1, "name", 1234567890123)
        self.assertRaises(CRUDErrors, self.test_service.add_client, 1, "name", 12345678901230)
        
    def testGetAll(self): 
        self.test_service.add_client(1, "name", 1234567890123)   
        self.assertEqual(self.test_service.get_all(),self.test_clients.get_all())
    
    def testEditClient(self):   
        self.assertRaises(RepositoryError, self.test_service.edit_client, 1, "name", 1234565555556)
        self.assertRaises(CRUDErrors, self.test_service.edit_client, 1, "", 1234567890123)
            
        self.test_service.add_client(1, "name", 1234567890123)
        self.test_service.edit_client(1, "name", 1234565555555)
    
    def testFindClient(self):    
        self.test_service.add_client(1, "aegfwe", 1234567890123)
        self.test_service.find_client(1)
        self.assertRaises(CRUDErrors, self.test_service.find_client, 2)
    
    def testDeleteClient(self):    
        self.test_service.add_client(1, "ewy", 1234567890123)
        self.test_service.del_client(1)
        self.assertRaises(RepositoryError, self.test_service.del_client, 2)
    
    def testAddRandomClient(self):    
        seed(5)
        t=self.test_service.add_random_client(1)
        c=Client(1, "ixlzwxuqao", 2989243529357)
        self.assertEqual(c.get_client_CNP(),t.get_client_CNP())
        self.assertEqual(c.get_client_name(),t.get_client_name())
