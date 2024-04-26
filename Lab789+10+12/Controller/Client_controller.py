'''
Created on Nov 14, 2023

@author: Cristian
'''
from Domain.Entities import Client
from Domain.Validators import ValidatorErrors, CRUDErrors
from random import randint, choice
import string

class ServiceClient:
    def __init__(self, repository):
        self.__repository=repository
        
    def add_random_client(self, idc):
        letters = string.ascii_lowercase
        
        number=randint(1,10)
        name_r =''.join(choice(letters) for t in range(number))
        
        CNP_r = randint(1000000000000,9999999999998)
        
        try:
            c = Client(idc,name_r,CNP_r)
            self.__repository.store(c)
            return c
        except ValidatorErrors as ve:
            raise CRUDErrors(ve)
        
    def add_client(self,idc,name,CNP):
        try:
            c = Client(idc,name,CNP)
            self.__repository.store(c)
        except ValidatorErrors as ve:
            raise CRUDErrors(ve) 
        
    def edit_client(self,idc,name,CNP):
        try:
            c = Client(idc,name,CNP)
            self.__repository.update(c)
        except ValidatorErrors as ve:
            raise CRUDErrors(ve) 
        
    def del_client(self,idc):
        try:
            self.__repository.delete(idc)
        except ValidatorErrors as ve:
            raise CRUDErrors(ve) 
    
    def find_client(self, idc):
        if self.__repository.find_by_id(idc)==None:
            raise CRUDErrors("A client with the given Id does not exist!")
        else:
            return str(self.__repository.find_by_id(idc))
        
    def get_all(self):
        return self.__repository.get_all()
    