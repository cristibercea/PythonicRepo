'''
Created on Dec 2, 2023

@author: Cristian
'''

from Domain.Validators import ValidatorErrors, RepositoryError
from Domain.Entities import Client

class ClientRepository:
    """
    an object of type ClientRepository.
    here are declared the CRUD functions needed for modifying our dictionary of clients
    """
    def __init__(self,validator):
        self.__clients={}
        self.__validator=validator
        
    def store(self, item):
        self.__validator.validate(item)
        duplicate = self.find_by_id(item.get_id())
        if duplicate!=None: 
            raise RepositoryError("A client with the given Id does already exist!")
        self.__clients[item.get_id()]=item
        
    def delete(self, itemId):
        item = self.find_by_id(itemId)
        if item==None: 
            raise RepositoryError("A client with the given Id does not exist!")
        self.__validator.validate(self.__clients[item.get_id()])
        self.__clients.pop(item.get_id())
        
    def update(self, item):
        self.__validator.validate(item)
        itemaux = self.find_by_id(item.get_id())
        if itemaux==None: 
            raise RepositoryError("A client with the given Id does not exist!")
        for x in self.__clients:
            if x == item.get_id():
                self.__clients[x] = item
       
    def find_by_id(self, itemId):
        """
        Returns the item with the given itemId.
         
        Returns: the item with the given Id.  
                 none - if an item with the given itemId does not exist.
        """
        if not itemId in self.__clients:
            return None
        return self.__clients[itemId] 
    
    def get_all(self):
        """
        return: a dictionary, with: key = client id, element = client data
        """
        output={}
        for x in self.__clients:
            output[x]=self.__clients[x]
        return output    
    

class ClientFileRepository(ClientRepository):
    """
    an object of type ClientFileRepository.
    """
    def __init__(self,validator,filename):
        ClientRepository.__init__(self,validator) #extending ClientRepository with some file functionalities
        self.__filename=filename
        self.__load_from_file()

    def __load_from_file(self):
        """Clients from file are copied in memory repo (ClientRepository)"""
        with open(self.__filename,"r") as f:
            lines=f.readlines()    #lines = a list of all lines read from the file
            for line in lines:
                if line=="\n":
                    break
                client_id,client_name,client_CNP=[token.strip() for token in line.split(";")]
                client=Client(int(client_id),client_name,int(client_CNP))
                try:
                    ClientRepository.store(self,client)
                except RepositoryError: #if the recently read client has an id already existent, it will be ignored and erased from file after following operation
                    pass
                except ValidatorErrors: #if the recently read client is invalid, it will be ignored and erased from file after following operation
                    pass

    def __save_to_file(self):
        """Saves data from memory(ClientRepository) to file"""
        with open(self.__filename,"w") as f:
            clients=ClientRepository.get_all(self)
            for i in clients:
                str_client=str(i)+";"+str(clients[i].get_client_name())+";"+str(clients[i].get_client_CNP())+"\n"
                f.write(str_client)

    """function overrides:"""
    def store(self,new_client):
        ClientRepository.store(self,new_client)
        self.__save_to_file()

    def delete(self,idc):
        ClientRepository.delete(self,idc)
        self.__save_to_file()

    def update(self,client):
        ClientRepository.update(self,client)
        self.__save_to_file()

    def find_by_id(self,idc):
        """return: client searched for"""
        return ClientRepository.find_by_id(self,idc)

    def get_all(self):
        """return: all in-memory clients"""
        return ClientRepository.get_all(self)
