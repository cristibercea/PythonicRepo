'''
Created on Nov 14, 2023

@author: Cristian
'''
from Domain.Validators import CRUDErrors, RepositoryError

class UserInterface:
    def __init__(self,servmov,servcln,servrent): #params: a movie service, a client service, a rent service
        self.__serv_movies=servmov
        self.__serv_clients=servcln
        self.__serv_rent=servrent
    
    def show(self): #shows the main menu
        print("<=============================| MOVIE APP |=============================>")
        print(" _______________________________________________________________________ ")
        print("|_|                                                                   |_|")
        print("|       App Commands:                                                   |")
        print("|                                                                       |")
        print("|  ~List Modifiers:                                                     |")
        print("| -> 1. Add a movie                                                     |")
        print("| -> 2. Add a client                                                    |")
        print("| -> 3. Delete a movie by id                                            |")
        print("| -> 4. Delete a client by id                                           |")
        print("| -> 5. Edit a movie                                                    |")
        print("| -> 6. Edit a client                                                   |")
        print("|                                                                       |")
        print("|  ~Searchers:                                                          |")
        print("| -> 7. Search movie by id                                              |")
        print("| -> 8. Search client by id                                             |")
        print("|                                                                       |")
        print("|  ~Random generators:                                                  |")
        print("| -> 9. Generate a random movie into the movie repo                     |")
        print("| -> 10. Generate a random client into the client repo                  |")
        print("|                                                                       |")
        print("|  ~Actions:                                                            |")
        print("| -> 11. Rent a movie to a client                                       |")
        print("| -> 12. Retrieve a movie from a client                                 |")
        print("|                                                                       |")
        print("|  ~Reports:                                                            |")
        print("| -> 13. Print clients with rented films, ordered by name               |")
        print("| -> 14. Print clients ordered by number of movies rented - ascending   |")
        print("| -> 15. Print the most rented movies - only top 1                      |")
        print("| -> 16. Print top 30% clients with most movies                         |")
        print("| -> 17. Print top 30% rented movies                                    |")
        print("|                                                                       |")
        print("|_  ~Exit command: 0                                                   _|")
        print("|_|___________________________________________________________________|_|\n")
        print("<=============================| MAIN MENU |=============================>\n")
        
    def run(self): #runs the program and prints the current state of the repositories
        operations=[self.add_movie,self.add_client,self.del_movie,self.del_client,self.edit_movie,self.edit_client,self.find_movie,self.find_client,self.add_movie_random,self.add_client_random,self.make_rent,self.return_rent,self.order_by_name,self.order_by_rented,self.most_wanted,self.movie_lovers,self.movies_30percent] 
        while True:
            try:
                error=""
                command=int(input(">>>Insert your command's number: "))
                if command==0: 
                    print("  [i] Program execution stopped. ")
                    break;
                if command>17:
                    error+="input number must be \"<=\" than 17"
                    raise ValueError(error)
                operations[command-1]()
            except ValueError as vErr:
                print("  [!] Invalid input! ("+str(vErr)+")")
                
            print("Clients saved: "+str(self.__serv_clients.get_all()))
            print("Movies saved: "+str(self.__serv_movies.get_all()))
        
    def add_movie(self): #adds a movie to the repo or prints error messages
        try:
            Id=int(input(">>Insert movie id: "))
            name=input(">>Insert movie name: ")
            description=input(">>Insert movie description: ")
            genre=input(">>Insert movie genre: ")
            self.__serv_movies.add_movie(Id,name,description,genre)
        except CRUDErrors as se:
            print(se)
        except RepositoryError as re:
            print(re)    
    
    def add_movie_random(self): #adds a randomly generated movie to the repo or prints error messages
        try:
            Id=int(input(">>Insert movie id: "))
            self.__serv_movies.add_random_movie(Id)
        except CRUDErrors as se:
            print(se)
        except RepositoryError as re:
            print(re)
    
    def add_client(self): #adds a client to the repo or prints error messages
        try:
            Id=int(input(">>Insert client id: "))
            name=input(">>Insert client name: ")
            CNP=int(input(">>Insert client CNP: "))
            self.__serv_clients.add_client(Id,name,CNP)
        except CRUDErrors as se:
            print(se)
        except RepositoryError as re:
            print(re)
    
    def add_client_random(self): #adds a randomly client to the repo or prints error messages
        try:
            Id=int(input(">>Insert client id: "))
            self.__serv_clients.add_random_client(Id)
        except CRUDErrors as se:
            print(se)
        except RepositoryError as re:
            print(re)
        
    def del_movie(self): #deletes a movie from the repo or prints error messages
        try:
            Id=int(input(">>Insert movie id: "))
            self.__serv_movies.del_movie(Id)
        except CRUDErrors as se:
            print(se)
        except RepositoryError as re:
            print(re)
    
    def del_client(self): #deletes a client from the repo or prints error messages
        try:
            Id=int(input(">>Insert client id: "))
            self.__serv_clients.del_client(Id)
        except CRUDErrors as se:
            print(se)
        except RepositoryError as re:
            print(re)
    
    def edit_movie(self): #edits an existing movie in the repo or prints error messages
        try:
            Id=int(input(">>Insert movie id: "))
            name=input(">>Insert new movie name: ")
            description=input(">>Insert new movie description: ")
            genre=input(">>Insert new movie genre: ")
            self.__serv_movies.edit_movie(Id,name,description,genre)
        except CRUDErrors as se:
            print(se)
        except RepositoryError as re:
            print(re)
    
    def edit_client(self): #edits an existing client in the repo or prints error messages
        try:
            Id=int(input(">>Insert client id: "))
            name=input(">>Insert new client name: ")
            CNP=int(input(">>Insert new client CNP: "))
            self.__serv_clients.edit_client(Id,name,CNP)
        except CRUDErrors as se:
            print(se)
        except RepositoryError as re:
            print(re)
            
    def find_movie(self): #finds and prints a movie in the repo or prints error messages
        try:
            Id=int(input(">>Insert movie id: "))
            print(str(self.__serv_movies.find_movie(Id)))  
        except ValueError:
            print("Movie ID must be a natural number, greater than 0!")
        except CRUDErrors as se:
            print(se)
    
    def find_client(self): #finds and prints a client in the repo or prints error messages
        try:
            Id=int(input(">>Insert client id: "))
            print(str(self.__serv_clients.find_client(Id))) 
        except ValueError:
            print("Client ID must be a natural number, greater than 0!")
        except CRUDErrors as se:
            print(se)
            
    def make_rent(self): #makes a rent relation between a client and a movie or prints error messages
        try:
            idc=int(input(">>Insert client id: ")) 
            if idc<=0: raise ValueError
        except ValueError:
            print("Client ID must be a natural number, greater than 0!")
            return
        try:
            idm=int(input(">>Insert movie id: "))
            if idm<=0: raise ValueError  
        except ValueError:
            print("Movie ID must be a natural number, greater than 0!")
            return
        try:
            self.__serv_rent.add_rent(idc,idm)
            print("~A Movie has been successfully rented to a Client!")
        except CRUDErrors as se:
            print(se)
        except RepositoryError as re:
            print(re)
            
    def return_rent(self): #deletes an existing rent relation between a client and a movie or prints error messages
        try:
            idc=int(input(">>Insert client id: ")) 
            if idc<=0: raise ValueError
        except ValueError:
            print("Client ID must be a natural number, greater than 0!")
            return
        try:
            idm=int(input(">>Insert movie id: "))
            if idm<=0: raise ValueError  
        except ValueError:
            print("Movie ID must be a natural number, greater than 0!")
            return
        try:
            self.__serv_rent.delete_rent(idc,idm)
            print("~A Movie has been successfully received back from a Client!")
        except CRUDErrors as se:
            print(se)
        except RepositoryError as re:
            print(re)
        
    
    def order_by_name(self): #orders by name and prints clients that made at least a rental or prints error message
        try:
            rezult=self.__serv_rent.report_clients_by_name(self.__serv_clients.get_all())
            print("Clients who rented movies, ordered by name (alphabetical): \n",rezult)
        except CRUDErrors as se:
            print(se)
            
    def order_by_rented(self): #orders by the numbers of films rented and prints clients that made at least a rental or prints error message
        try:
            rezult=self.__serv_rent.report_clients_by_rentals(self.__serv_clients.get_all())
            print("Clients who rented movies, ordered by the number of movies rented (ascending): \n",rezult)
        except CRUDErrors as se:
            print(se)
    
    def most_wanted(self): #finds and prints movies that are rented the most (biggest numbers of rentals only) or prints error message
        try:
            rezult=self.__serv_rent.report_most_rented_movies(self.__serv_movies.get_all())
            print("Most rented movies: \n",rezult)
        except CRUDErrors as se:
            print(se)
            
    def movie_lovers(self): #finds and prints top 30% clients that rented the most amount of films or prints error message
        try:
            rezult=self.__serv_rent.report_top_30percent_clients(self.__serv_clients.get_all())
            print("Top 30% clients with most films: \n",rezult)
        except CRUDErrors as se:
            print(se)
    
    def movies_30percent(self): #finds and prints top 30% movies that were rented the most
        try:
            rezult=self.__serv_rent.report_top_30percent_movies(self.__serv_movies.get_all())
            print("Top 30% of most rented films: \n",rezult)
        except CRUDErrors as se:
            print(se)