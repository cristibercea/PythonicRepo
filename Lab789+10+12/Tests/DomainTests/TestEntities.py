'''
Created on Dec 2, 2023

@author: Cristian
'''
import unittest
from Domain.Entities import Client, Movie, Rent, DataTransferObject

class TestCaseEntities(unittest.TestCase): #whitebox tests
    def setUp(self):
        self.c=Client(1,"Alin",1234567890123)
        self.m=Movie(1,"Trinity","a b c","sci-fi")
        
    def testCreateMovie(self):
        self.assertEqual(self.m.get_id(), 1, "id error")
        self.assertEqual(self.m.get_movie_name(),"Trinity", "name error")
        self.assertEqual(self.m.get_movie_description(),"a b c", "description error")
        self.assertEqual(self.m.get_movie_genre(),"sci-fi", "genre error")
        self.assertEqual(str(self.m),"Trinity, a b c, sci-fi", "print error")
        
    def testCreateClient(self):    
        self.assertTrue(self.c.get_id()==1)
        self.assertTrue(self.c.get_client_name()=="Alin")
        self.assertTrue(self.c.get_client_CNP()==1234567890123)
        self.assertTrue(str(self.c)=="Alin, 1234567890123")
        
    def testCreateRent(self): 
        self.r=Rent(self.c,self.m)   
        self.assertEqual(self.r.get_client(),self.c, "client equals error")
        self.assertEqual(self.r.get_movie(),self.m, "movie equals error")
    
    def testDataTransferObject(self):
        self.DTO=DataTransferObject("nume",123)
        self.assertEqual(self.DTO.get_name(), "nume")
        self.assertEqual(self.DTO.get_rents(), 123)