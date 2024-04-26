'''
Created on Nov 14, 2023

@author: Cristian
'''
class RepositoryError(Exception):
    """repository errors "definition". they extend Exception class """
    pass  

class CRUDErrors(Exception): 
    """store errors "definition". they extend Exception class """
    pass

class ValidatorErrors(CRUDErrors): 
    """validation errors "definition". they extend Exception class """
    pass

class MovieValidator:
    """
    validates a movie
    raises a validation error if the parameter movie is not valid 
    """
    def validate(self, movie):
        errors=[]
        if not type(movie.get_id()) is int or movie.get_id()<=0:
            errors.append("Movie ID must be a natural number, greater than 0!")
        if movie.get_movie_name()=="":
            errors.append("The movie must have a non-empty name!")
        if movie.get_movie_description()=="":
            errors.append("The movie must have a description!")
        if movie.get_movie_genre()=="":
            errors.append("The movie must be part of a genre!")
            
        if len(errors)>0:
            raise ValidatorErrors(str(errors))
    
class ClientValidator:
    """
    validates a client
    raises a validation error if the parameter client is not valid 
    """
    def validate(self, client):
        errors=[]
        if not type(client.get_id()) is int or client.get_id()<=0:
            errors.append("Client ID must be a natural number, greater than 0!")
        if client.get_client_name()=="":
            errors.append("The client must have a non-empty name!")
        if not type(client.get_client_CNP()) is int or client.get_client_CNP()<1e12 or client.get_client_CNP()>=1e13:
            errors.append("The client CNP must be a 13 digit number!")
            
        if len(errors)>0:
            raise ValidatorErrors(str(errors))

class RentValidator:
    """
    validates a rent
    raises a validation error if there is no client and/or movie in the repo, to be included in a rent action
    """
    def validate(self, c, m):
        errors=[]
        if m==None:
            errors.append("There is no movie with given ID")
        if c==None:
            errors.append("There is no client with given ID")
            
        if len(errors)>0:
            raise ValidatorErrors(str(errors))
