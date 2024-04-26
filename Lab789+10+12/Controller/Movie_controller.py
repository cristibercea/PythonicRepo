'''
Created on Nov 14, 2023

@author: Cristian
'''
from Domain.Entities import Movie
from Domain.Validators import ValidatorErrors, CRUDErrors
from random import randint, choice
import string

class ServiceMovie:
    def __init__(self, repository):
        self.__repository=repository
    
    def add_random_movie(self,idm):
        letters = string.ascii_lowercase
        
        number=randint(1,10)
        name_r =''.join(choice(letters) for i in range(number))
        
        number=randint(1,10)
        description_r =''.join(choice(letters) for i in range(number))
        
        number=randint(1,10)
        genre_r =''.join(choice(letters) for i in range(number))
        
        try:
            m = Movie(idm,name_r,description_r,genre_r)
            self.__repository.store(m)
            return m
        except ValidatorErrors as ve:
            raise CRUDErrors(ve)
    
    def add_movie(self,idm,name,description,genre):
        try:
            m = Movie(idm,name,description,genre)
            self.__repository.store(m)
        except ValidatorErrors as ve:
            raise CRUDErrors(ve) 
        
    def edit_movie(self,idm,name,description,genre):
        try:
            m = Movie(idm,name,description,genre)
            self.__repository.update(m)
        except ValidatorErrors as ve:
            raise CRUDErrors(ve)
        pass
        
    def del_movie(self,idm):
        try:
            self.__repository.delete(idm)
        except ValidatorErrors as ve:
            raise CRUDErrors(ve) 
        
    def find_movie(self, idm):
        if self.__repository.find_by_id(idm)==None:
            raise CRUDErrors("A movie with the given Id does not exist!")
        else:
            return str(self.__repository.find_by_id(idm))
    
    def get_all(self):
        return self.__repository.get_all()
    