'''
Created on Nov 14, 2023

@author: Cristian
'''
from Domain.Validators import RepositoryError
from Domain.Entities import Rent
    
class RentRepository: 
    def __init__(self,validator,clientsrepo,moviesrepo):
        self.__rents=[]
        self.__validator=validator
        self.__clients=clientsrepo
        self.__movies=moviesrepo
        
    def store(self,idc,idm):
        """
        stores a rent in the rent list if in ClientsRepo and MoviesRepo exist a client and a movie with given id
        raise ValidatorError: if there is not a movie or/and a client with given idm, respectively idc
        raise RepositoryError: if there is a rent item (in the list of rents) with a client and a movie that have given idc, respectively idm
        """
        c=self.__clients.find_by_id(idc)
        m=self.__movies.find_by_id(idm)
        self.__validator.validate(c,m)
        r=Rent(c,m)
        for t in self.__rents:
            if t==r:
                raise RepositoryError("There is already a rent between the client and movie with given ids!")
        self.__rents.append(r)
        
    def delete(self,idc,idm):
        """
        deletes a rent from the rent list if in ClientsRepo and MoviesRepo exist a client and a movie with given id
        raise ValidatorError: if there is not a movie or/and a client with given idm, respectively idc
        raise RepositoryError: if there is no rent item (in the list of rents) with a client and a movie that have given idc, respectively idm
        """
        c=self.__clients.find_by_id(idc)
        m=self.__movies.find_by_id(idm)
        self.__validator.validate(c,m)
        r=Rent(c,m)
        for t in self.__rents:
            if t==r:
                self.__rents.remove(t)
                return
        raise RepositoryError("There is no rent between the client and movie with given ids!")
