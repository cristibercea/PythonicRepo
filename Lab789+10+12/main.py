'''
Created on Nov 14, 2023

@author: Cristian

The app will work by default with file repositories, but the information will be passed through memory repositories (where it will be processed)
'''
from UI.Console import UserInterface
from Controller.Movie_controller import ServiceMovie
from Controller.Client_controller import ServiceClient
from Controller.Rent_controller import ServiceRent
from Domain.Validators import MovieValidator, ClientValidator, RentValidator
from Repository.RentRepository import RentRepository
from Repository.ClientRepository import ClientFileRepository
from Repository.MovieRepository import MovieFileRepository


all_movies=MovieFileRepository(MovieValidator(),"data/movies.txt")
all_clients=ClientFileRepository(ClientValidator(),"data/clients.txt")
all_rents=RentRepository(RentValidator(),all_clients,all_movies)

servmov=ServiceMovie(all_movies)
servcln=ServiceClient(all_clients)
servrent=ServiceRent(all_rents)

ui=UserInterface(servmov,servcln,servrent)
ui.show()
ui.run()