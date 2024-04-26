'''
Created on Dec 2, 2023

@author: Cristian
'''

from Domain.Validators import ValidatorErrors, RepositoryError
from Domain.Entities import Movie

class MovieRepository:
    """
    an object of type MovieRepository.
    here are declared the CRUD functions needed for modifying our dictionary of movies
    """
    def __init__(self,validator):
        self.__movies={}
        self.__validator=validator
        
    def store(self, item):
        self.__validator.validate(item)
        duplicate = self.find_by_id(item.get_id())
        if duplicate!=None: 
            raise RepositoryError("A movie with the given Id does already exist!")
        self.__movies[item.get_id()]=item
        
    def delete(self, itemId):
        item = self.find_by_id(itemId)
        if item==None: 
            raise RepositoryError("A movie with the given Id does not exist!")
        self.__validator.validate(self.__movies[item.get_id()])
        self.__movies.pop(item.get_id())
        
    def update(self, item):
        self.__validator.validate(item)
        itemaux = self.find_by_id(item.get_id())
        if itemaux==None: 
            raise RepositoryError("A movie with the given Id does not exist!")
        for x in self.__movies:
            if x == item.get_id():
                self.__movies[x] = item
        
    def find_by_id(self, itemId):
        """
        Returns the item with the given itemId.
         
        Returns: the item with the given Id.  
                 none - if an item with the given itemId does not exist.
        """
        if not itemId in self.__movies:
            return None
        return self.__movies[itemId] 
    
    def get_all(self):
        """
        return: a dictionary, with: key = movie id, element = movie data
        """
        output={}
        for x in self.__movies:
            output[x]=self.__movies[x]
        return output


class MovieFileRepository(MovieRepository):
    """
    an object of type MovieFileRepository.
    """
    def __init__(self,validator,filename):
        MovieRepository.__init__(self,validator) #extending MovieRepository with some file functionalities
        self.__filename=filename
        self.__load_from_file()

    def __load_from_file(self):
        """Movies from file are copied in the memory repo (MovieRepository)"""
        with open(self.__filename,"r") as f:
            lines=f.readlines()    #lines = a list of all lines read from the file
            for line in lines:
                if line=="\n":
                    break
                movie_id,movie_title,movie_desc,movie_gen=[token.strip() for token in line.split(";")]
                film=Movie(int(movie_id),movie_title,movie_desc,movie_gen)
                try:
                    MovieRepository.store(self,film)
                except RepositoryError: #if the recently read film has an id already existent, it will be ignored and erased from file after following operation
                    pass
                except ValidatorErrors: #if the recently read film is invalid, it will be ignored and erased from file after following operation
                    pass

    def __save_to_file(self):
        """Saves data from memory(MovieRepository) to file"""
        with open(self.__filename,"w") as f:
            films=MovieRepository.get_all(self)
            for i in films:
                str_movie=str(i)+";"+str(films[i].get_movie_name())+";"+str(films[i].get_movie_description())+";"+str(films[i].get_movie_genre())+"\n"
                f.write(str_movie)

    """function overrides:"""
    def store(self,new_movie):
        MovieRepository.store(self,new_movie)
        self.__save_to_file()

    def delete(self,idm):
        MovieRepository.delete(self,idm)
        self.__save_to_file()

    def update(self,movie):
        MovieRepository.update(self,movie)
        self.__save_to_file()

    def find_by_id(self,idm):
        """return: movie searched for"""
        return MovieRepository.find_by_id(self,idm)

    def get_all(self):
        """return: all in-memory movies"""
        return MovieRepository.get_all(self)
