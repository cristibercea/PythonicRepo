'''
Created on Dec 2, 2023

@author: Cristian
'''
import unittest
from Repository.RentRepository import RentRepository
from Repository.MovieRepository import MovieRepository
from Repository.ClientRepository import ClientRepository
from Domain.Entities import Client, Movie
from Domain.Validators import RentValidator, MovieValidator, ClientValidator, ValidatorErrors, RepositoryError

class testCaseRentRepo(unittest.TestCase):
    def setUp(self):
        self.mtest=MovieRepository(MovieValidator())
        self.ctest=ClientRepository(ClientValidator())
        self.mitem=Movie(1, "Trinity", "nice movie", "action")
        self.citem=Client(1,"Alin",1234567890123)
        self.ctest.store(self.citem)
        self.mtest.store(self.mitem)
        self.rtest=RentRepository(RentValidator(),self.ctest,self.mtest)
    
    def testRentStore(self):
        self.rtest.store(1,1)
        self.assertRaises(RepositoryError, self.rtest.store,1,1)
        self.assertRaises(ValidatorErrors, self.rtest.store,2,6)
        self.assertRaises(ValidatorErrors, self.rtest.store,32,11)
        self.assertRaises(ValidatorErrors, self.rtest.store,3245,425)
    
    def testRentDelete(self):
        self.assertRaises(ValidatorErrors, self.rtest.delete,2,1)
        self.assertRaises(RepositoryError, self.rtest.delete,1,1)
        self.rtest.store(1,1)
        self.rtest.delete(1,1)
