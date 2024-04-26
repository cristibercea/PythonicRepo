'''
Created on Nov 14, 2023

@author: Cristian
'''
class Movie:
    """
    an object that resembles a movie and their properties
    multiple getters are defined
    """
    def __init__(self, idm, name, description, genre):
        self.__idm=idm
        self.__name=name
        self.__description=description
        self.__genre=genre
    
    def get_id(self): 
        """returns movie id"""
        return self.__idm
    
    def get_movie_name(self): 
        """returns movie name"""
        return self.__name
    
    def get_movie_description(self): 
        """returns movie description"""
        return self.__description
    
    def get_movie_genre(self): 
        """returns movie genre"""
        return self.__genre
    
    def set_movie_name(self,name): 
        """returns movie name"""
        self.__name=name
    
    def set_movie_description(self,desc): 
        """returns movie description"""
        self.__description=desc
    
    def set_movie_genre(self,genre): 
        """returns movie genre"""
        self.__genre=genre
    
    def __str__(self):
        return self.get_movie_name()+", "+self.get_movie_description()+", "+self.get_movie_genre()
    
    def __repr__(self):
        return str(self)


class Client:
    """
    an object that resembles a client and their properties
    multiple getters are defined
    """
    def __init__(self, idc, name, CNP):
        self.__idc=idc
        self.__name=name
        self.__CNP=CNP
    
    def get_id(self): 
        """returns client id"""
        return self.__idc
    
    def get_client_name(self): 
        """returns client name"""
        return self.__name
    
    def get_client_CNP(self): 
        """returns client CNP"""
        return self.__CNP
    
    def set_client_name(self,name): 
        """returns client name"""
        self.__name=name
    
    def set_client_CNP(self,CNP): 
        """returns client CNP"""
        self.__CNP=CNP
    
    def __str__(self):
        return self.get_client_name()+", "+str(self.get_client_CNP())
    
    def __repr__(self):
        return str(self)

class Rent:
    """
    an object that resembles a client with the movies they rented
    multiple getters are defined
    """
    def __init__(self, client, movie):
        self.__client=client
        self.__movie=movie
    
    def get_client(self): 
        """returns client id"""
        return self.__client
    
    def get_movie(self): 
        """returns movie id"""
        return self.__movie
    
    def __eq__(self,r):
        return self.__client.get_id()==r.__client.get_id() and self.__movie.get_id()==r.__movie.get_id()
    
class DataTransferObject:
    def __init__(self,name,number_of_rentals):
        """
        a Data transfer object
        multiple getters are defined
        """
        self.__name=name
        self.__rents=number_of_rentals
    
    def get_name(self):
        return self.__name
    
    def get_rents(self):
        return self.__rents
    
    def __str__(self):
        return "name: "+str(self.__name)+"; rentals: "+str(self.__rents)
    
    def __repr__(self):
        return str(self)
        