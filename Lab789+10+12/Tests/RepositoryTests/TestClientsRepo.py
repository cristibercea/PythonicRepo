'''
Created on Dec 2, 2023

@author: Cristian
'''
import unittest
from Domain.Validators import ClientValidator, ValidatorErrors, RepositoryError
from Domain.Entities import Client
from Repository.ClientRepository import ClientRepository,ClientFileRepository

class TestCaseClientRepo(unittest.TestCase):
    def setUp(self):
        self.test=ClientRepository(ClientValidator())
        self.item=Client(1,"Alin",1234567890123)
    
    def testStoreClient(self):
        self.test.store(self.item)
        self.assertRaises(RepositoryError, self.test.store, self.item)
        self.assertRaises(ValidatorErrors, self.test.store, Client(1, "Trfgy", 3849))
            
    def testGetAllClients(self):
        self.assertTrue(self.test.get_all()=={})
        self.test.store(self.item)
        self.assertEqual(self.test.get_all(),{1:self.item},"get-all error")
        
    def testUpdateClient(self):
        self.assertRaises(RepositoryError, self.test.update,self.item)
        self.test.store(self.item)
        self.test.update(self.item)
        self.assertRaises(ValidatorErrors, self.test.update, Client(1, "Alin", 23566))
            
    def testFindClientByID(self):
        self.assertTrue(self.test.find_by_id(1)==None)    
        self.test.store(self.item)
        self.assertEqual(self.test.find_by_id(1), self.item, "find-by-id error")
      
    def testDeleteClient(self):
        self.test.store(self.item)
        self.test.delete(self.item.get_id())
        self.assertRaises(RepositoryError, self.test.delete, 1)


class TestCaseFileClientRepo(unittest.TestCase):
    def setUp(self):
        self.test=ClientFileRepository(ClientValidator(),"testclients.txt")
        self.item=Client(6,"Alin",1234567890123)
        self.item1=Client(1,"Marcel",1234567890111)
        self.item2=Client(2,"sdgdfsg",5295021928629)
    
    def tearDown(self):
        del_file=open("testclients.txt",'w')
        del_file.close()
        self.test=ClientFileRepository(ClientValidator(),"testclients.txt")
        self.test.store(self.item1)
        self.test.store(self.item2)
    
    def testStoreClient(self):
        self.test.store(self.item)
        self.assertRaises(RepositoryError, self.test.store, self.item)
        self.assertRaises(ValidatorErrors, self.test.store, Client(1, "Trfgy", 3849))
        
    def testUpdateClient(self):
        self.assertRaises(RepositoryError, self.test.update,self.item)
        self.test.store(self.item)
        self.test.update(self.item)
        self.assertRaises(ValidatorErrors, self.test.update, Client(1, "Alin", 23566))
            
    def testFindClientByID(self):
        self.assertTrue(self.test.find_by_id(9)==None)    
        self.test.store(self.item)
        self.assertEqual(self.test.find_by_id(6), self.item, "find-by-id error")
      
    def testDeleteClient(self):
        self.test.store(self.item)
        self.test.delete(self.item.get_id())
        self.assertRaises(RepositoryError, self.test.delete, 7)
