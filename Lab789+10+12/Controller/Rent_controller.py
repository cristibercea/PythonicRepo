'''
Created on Nov 25, 2023

@author: Cristian
'''
from Domain.Validators import ValidatorErrors, CRUDErrors
from Domain.Entities import DataTransferObject

class ServiceRent:
    def __init__(self, repository):
        self.__repository=repository         #rentRepository
        self.__movie_rented_frequency={}     #dictionary that contains movie ids as keys, and the number of times the movie has been rented
        self.__client_renting_frequency={}   #dictionary that contains client ids as keys, and the number of times the client rented a film
        
    def add_rent(self,idc,idm):
        """
        make a rent: client with given id, rents movie with given id 
        params: client id = idc, movie id = idm
        raise: CRUDErrors if the creation of the rent has failed (if the client or movie with given ids do not exist) 
        """
        try:
            self.__repository.store(idc,idm)
            
            if not idc in self.__client_renting_frequency:
                self.__client_renting_frequency[idc]=0
            self.__client_renting_frequency[idc]+=1
            
            if not idm in self.__movie_rented_frequency:
                self.__movie_rented_frequency[idm]=0
            self.__movie_rented_frequency[idm]+=1
        except ValidatorErrors as ve:
            raise CRUDErrors(ve)
        
    def delete_rent(self,idc,idm):
        """
        return a rent: client with given id, returns movie with given id 
        params: client id = idc, movie id = idm
        raise: CRUDErrors if the deletion of the rent has failed (if the client or movie with given ids do not exist) 
        """
        try:         
            self.__repository.delete(idc,idm)
        except ValidatorErrors as ve:
            raise CRUDErrors(ve)
    
    def get_movie_frequency(self,idm):
        """
        param: id of a movie
        return: -None, if the movie was never rented
                -the number of rents corresponding to the movie`s id
        """
        if idm in self.__movie_rented_frequency:
            return self.__movie_rented_frequency[idm]
        return None
    
    def get_client_frequency(self,idc):
        """
        param: id of a client
        return: -None, if the client did not make any rental
                -the number of rentals corresponding to the client`s id
        """
        if idc in self.__client_renting_frequency:
            return self.__client_renting_frequency[idc]
        return  None
    
    def insertion_sort(self,List,key=lambda x: x,reverse=None, cmp=lambda x,y: x<y):
        """
        --insertion sort
        orders only the clients that made at least a rent
        param: --required: -List = a list to be sorted
               --optional: -key==1 - clients/movies are done by the amount of: movies they rented/times they have been rented key==0 - clients are ordered by alphabetically by name 
                           -reverse = True - sort descendingly, = False -sort ascendingly
        return: the done List 
        """
        if reverse==None: reverse=False
        for i in range(1,len(List)):
            temp=List[i]
            p=i-1
            while p>=0 and ((reverse==True and cmp(key(List[p]),key(temp))) or (reverse==False and not cmp(key(List[p]),key(temp)))):
                List[p+1]=List[p]
                p-=1
            List[p+1]=temp
        return List
    
    def comb_sort(self,List,key=lambda x: x,reverse=None,cmp=lambda x,y: x<y):
        from math import floor
        """
        --comb sort
        orders only the clients that made at least a rent
        param: --required: -List = a list to be sorted
               --optional: -key==1 - clients/movies are done by the amount of: movies they rented/times they have been rented key==0 - clients are ordered by alphabetically by name 
                           -reverse = True - sort descendingly, = False -sort ascendingly
        return: the done List 
        """
        if reverse==None: reverse=False
        length = len(List)
        shrink = 1.3
        gap = length
        done = False
        while not done:
            gap = floor(gap / shrink)
            if gap <= 1:
                done = True
                gap = 1
            elif 9 <= gap <= 10:
                gap = 11
            # equivalent to `i = 0; while (i + gap) < length: ...{loop body}... i += 1`
            for i in range(length - gap):
                sm = gap + i
                if (reverse==True and cmp(key(List[i]) , key(List[sm]))) or (reverse==False and not cmp(key(List[i]) , key(List[sm]))):
                    List[i], List[sm] = List[sm], List[i]
                    done = False
        return List
    
    def find_max_rented_movies(self,movies,maxim,n,rez):
        """
        --recursive function 1
        param: -movies = a list of movies
               -maxim = the maximum rents
               -n = index of the last element in movies list
               -rez = the list to be returned
        return: list with names of movies rented the most
        """
        if n<0: return rez
        self.find_max_rented_movies(movies, maxim, n-1, rez)
        if self.get_movie_frequency(movies[n].get_id())==maxim:
            rez.append(movies[n].get_movie_name())
        return rez

    def get_the30percent(self,rez,top30,n):
        """
        --recursive function 2
        param: -rez = ascending ordered (by number of movies rented) list of clients that rented at least a movie
               -top30 = the list to be returned after recursions
               -n = the number of objects to append in top30 list
        return: -top 30% clients with movies rented
                -the client with the most movies rented, if there are less than 4 clients that rented movies
        """
        if n<=1: 
            top30.append(rez[0])
            return top30
        self.get_the30percent(rez,top30,n-1)
        top30.append(rez[n-1])
        return top30
    
    def report_clients_by_name(self,clients):
        """
        returns a list of clients ordered by name (format: name+CNP+number_of_rentals)
        raises CRUDErrors: -if the list of clients is empty
                            -if there is no client that made a rent
        """
        if len(clients)==0: raise CRUDErrors("There are no clients saved!")
        
        rez=[]
        for i in clients:
            number_of_rentals=self.get_client_frequency(i)
            if number_of_rentals!=None:
                self.__DTO=DataTransferObject(clients[i].get_client_name(),number_of_rentals)
                rez.append(self.__DTO)
    
        if len(rez)==0: raise CRUDErrors("There are no clients that made a rent!") 
        List= self.insertion_sort(rez,key=lambda x: x.get_name())
        return List
    
    def report_clients_by_rentals (self,clients):
        """
        returns a list of clients ordered by number of rentals (format: name+CNP+number_of_rentals)
        raises CRUDErrors: -if the list of clients is empty
                            -if there is no client that made a rent
        """
        if len(clients)==0: raise CRUDErrors("There are no clients saved!")
        
        rez=[]
        for i in clients:
            number_of_rentals=self.get_client_frequency(i)
            if number_of_rentals!=None:
                self.__DTO=DataTransferObject(clients[i].get_client_name(),number_of_rentals)
                rez.append(self.__DTO)
    
        if len(rez)==0: raise CRUDErrors("There are no clients that made a rent!") 
        
        List= self.comb_sort(rez,key=lambda x: x.get_rents(), reverse=True)
        return List
    
    def report_most_rented_movies (self,movies):
        """
        returns a list with the most rented movies (format: name+description+genre+number_of_rents)
        raises CRUDErrors: -if the list of movies is empty
                            -if there is no movie rented
        """
        if len(movies)==0: raise CRUDErrors("There are no movies saved!")
        
        maxim=0
        movie_list=[]
        for i in movies:
            number_of_rentals=self.get_movie_frequency(i)
            movie_list.append(movies[i])
            if number_of_rentals!=None and number_of_rentals>maxim:
                maxim=number_of_rentals        
        
        if maxim==0: raise CRUDErrors("There are no movies rented yet!") 
        
        n=len(movie_list)
        return self.find_max_rented_movies(movie_list,maxim,n-1,[])
    
    def report_top_30percent_clients(self,clients):
        """
        returns a top 30% list with clients that have the most rentals (format: name+number_of_rentals)
        raises CRUDErrors: -if the list of clients is empty
                            -if there is no client that made a rent
        """
        if len(clients)==0: raise CRUDErrors("There are no clients saved!")
        
        rez=[]
        for i in clients:
            number_of_rentals=self.get_client_frequency(i)
            if number_of_rentals!=None:
                self.__DTO=DataTransferObject(clients[i].get_client_name(),number_of_rentals)
                rez.append(self.__DTO)
    
        if len(rez)==0: raise CRUDErrors("There are no clients that made a rent yet!") 
        
        rez = self.comb_sort(rez,key=lambda x: x.get_rents(),reverse=True)
        
        n=(len(rez)*3)//10
        return self.get_the30percent(rez,[],n)
    
    def report_top_30percent_movies(self,movies):
        """
        returns a top 30% list with movies that have been rented (format: name+number_of_rentals)
        raises CRUDErrors: -if the list of movies is empty
                            -if there is no movie that has been rented
        """
        if len(movies)==0: raise CRUDErrors("There are no movies saved!")
        
        rez=[]
        for i in movies:
            number_of_rentals=self.get_movie_frequency(i)
            if number_of_rentals!=None:
                self.__DTO=DataTransferObject(movies[i].get_movie_name(),number_of_rentals)
                rez.append(self.__DTO)
    
        if len(rez)==0: raise CRUDErrors("There are no movies that have been rented yet!") 
        
        rez = self.insertion_sort(rez,key=lambda x: x.get_rents(),reverse=True)
    
        n=(len(rez)*3)//10
        return self.get_the30percent(rez,[],n)
