'''
Created on Dec 2, 2023

@author: Cristian
'''
import unittest
from Domain.Validators import ClientValidator, MovieValidator, RentValidator, ValidatorErrors
from Domain.Entities import Client,Movie,Rent

class TestCaseClientValidator(unittest.TestCase):
    def setUp(self):
        self.v=ClientValidator()
        
    def testValidate(self): #whitebox test (all cases are verified)
        self.c=Client(1,"Alin",1234555555728)
        self.assertEqual(self.v.validate(self.c),None,"error")
        self.c=Client(1,"Alin",123555728)
        self.assertRaises(ValidatorErrors, self.v.validate, self.c)
        self.c=Client(1,"",1234555555728)
        self.assertRaises(ValidatorErrors, self.v.validate, self.c)
        self.c=Client(-1,"",1234555555728)
        self.assertRaises(ValidatorErrors, self.v.validate, self.c)
        
class TestCaseMovieValidator(unittest.TestCase):
    def setUp(self):
        self.v=MovieValidator()
        
    def testValidate(self): #blackbox test (there is only tested if the given movie is valid or not)
        self.m=Movie(1,"aeggdg","skjdfh","dlklfn")
        self.assertEqual(self.v.validate(self.m),None,"error")
        self.m=Movie(1,"aeggdg","","dlklfn")
        self.assertRaises(ValidatorErrors, self.v.validate, self.m)
        
class TestCaseRentValidator(unittest.TestCase):
    def setUp(self):
        self.v=RentValidator()
        self.m=Movie(1,"aeggdg","skjdfh","dlklfn")
        self.c=Client(1,"Alin",1234555555728)
        
    def testValidate(self): #whitebox test (all cases are verified)
        self.r=Rent(self.c,self.m)
        self.assertEqual(self.v.validate(self.r.get_client(),self.r.get_movie()),None,"error")
        self.r=Rent(self.c,None)
        self.assertRaises(ValidatorErrors, self.v.validate, self.r.get_client(),self.r.get_movie())
        self.r=Rent(None,self.m)
        self.assertRaises(ValidatorErrors, self.v.validate, self.r.get_client(),self.r.get_movie())
        self.r=Rent(None,None)
        self.assertRaises(ValidatorErrors, self.v.validate, self.r.get_client(),self.r.get_movie())
        
        