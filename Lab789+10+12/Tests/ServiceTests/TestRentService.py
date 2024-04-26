'''
Created on Dec 2, 2023

@author: Cristian
'''
import unittest
from Domain.Validators import CRUDErrors, RentValidator, ClientValidator, MovieValidator
from Repository.RentRepository import RentRepository, RepositoryError
from Domain.Entities import Client, Movie
from Repository.MovieRepository import MovieRepository
from Repository.ClientRepository import ClientRepository
from Controller.Rent_controller import ServiceRent

class TestCaseRentService(unittest.TestCase):
    def setUp(self):
        self.test_clients = ClientRepository(ClientValidator()) #in memory repo tests are easier to test 
        self.test_movies = MovieRepository(MovieValidator())
        
        self.mitem=Movie(1, "Trinity", "nice movie", "action")
        self.citem=Client(1,"Alin",1234567890123)
        self.test_clients.store(self.citem)
        self.test_movies.store(self.mitem)
        
        self.mitem=Movie(2, "Film", "ok movie", "horror")
        self.citem=Client(2,"Bogdan",8234373891073)
        self.test_clients.store(self.citem)
        self.test_movies.store(self.mitem)
        
        self.test_rents = RentRepository(RentValidator(),self.test_clients,self.test_movies)
        
        self.test_service = ServiceRent(self.test_rents)
    
    def testInsertionSort(self):
        self.assertEqual(self.test_service.insertion_sort([]),[])
        self.assertEqual(self.test_service.insertion_sort([["Alin",214],["Bogdan",346]]),[["Alin",214],["Bogdan",346]])
        self.assertEqual(self.test_service.insertion_sort([["Bogdan",346],["Alin",214]]),[["Alin",214],["Bogdan",346]])
        self.assertEqual(self.test_service.insertion_sort([["Bogdan","8234373891073","346"],["Alin","1234567890123","214"]],reverse=False),[["Alin","1234567890123","214"],["Bogdan","8234373891073","346"]])
        
        self.assertEqual(self.test_service.insertion_sort([["Alin",214],["Bogdan",346]],reverse=True),[["Bogdan",346],["Alin",214]])
        self.assertEqual(self.test_service.insertion_sort([["Bogdan",346],["Alin",214]],reverse=True),[["Bogdan",346],["Alin",214]])
        self.assertEqual(self.test_service.insertion_sort([["Bogdan","8234373891073","346"],["Alin","1234567890123","214"]],reverse=True),[["Bogdan","8234373891073","346"],["Alin","1234567890123","214"]])
        
    def testCombSort(self):
        self.assertEqual(self.test_service.comb_sort([]),[])
        self.assertEqual(self.test_service.comb_sort([["Alin",214],["Bogdan",346]]),[["Alin",214],["Bogdan",346]])
        self.assertEqual(self.test_service.comb_sort([["Bogdan",346],["Alin",214]]),[["Alin",214],["Bogdan",346]])
        self.assertEqual(self.test_service.comb_sort([["Bogdan","8234373891073","346"],["Alin","1234567890123","214"]],reverse=False),[["Alin","1234567890123","214"],["Bogdan","8234373891073","346"]])
        
        self.assertEqual(self.test_service.comb_sort([["Alin",214],["Bogdan",346]],reverse=True),[["Bogdan",346],["Alin",214]])
        self.assertEqual(self.test_service.comb_sort([["Bogdan",346],["Alin",214]],reverse=True),[["Bogdan",346],["Alin",214]])
        self.assertEqual(self.test_service.comb_sort([["Bogdan","8234373891073","346"],["Alin","1234567890123","214"]],reverse=True),[["Bogdan","8234373891073","346"],["Alin","1234567890123","214"]])
    
    def testAddRent(self):
        self.assertRaises(CRUDErrors, self.test_service.add_rent, 7,4)
        self.assertRaises(CRUDErrors, self.test_service.add_rent, 1,4) 
        self.assertRaises(CRUDErrors, self.test_service.add_rent, 7,1)
        self.test_service.add_rent(1,1)
        self.test_service.add_rent(2,1)
        self.test_service.add_rent(1,2)
        
    def testDeleteRent(self):
        self.assertRaises(CRUDErrors, self.test_service.delete_rent, 7,4)
        self.assertRaises(CRUDErrors, self.test_service.delete_rent, 1,4)
        self.assertRaises(CRUDErrors, self.test_service.delete_rent, 7,1)
        
        self.test_service.add_rent(1,1)
        self.test_service.add_rent(2,1)
        self.test_service.delete_rent(2,1)
        self.test_service.delete_rent(1,1)
        
        self.assertRaises(RepositoryError, self.test_service.delete_rent, 1,1)
    
    def testGetFrequencies(self):
        self.test_service.add_rent(1,1)
        self.test_service.add_rent(2,1)
        self.test_service.add_rent(1,2)
        self.assertTrue(self.test_service.get_movie_frequency(1)==2)
        self.assertTrue(self.test_service.get_client_frequency(1)==2)
        self.assertTrue(self.test_service.get_movie_frequency(2)==1)
        self.assertTrue(self.test_service.get_client_frequency(2)==1)
    
    def testFindMaxRentedMovies(self):
        self.assertTrue(self.test_service.find_max_rented_movies([], 235,-1,[])==[])
        self.test_service.add_rent(1,1)
        self.test_service.add_rent(2,1)
        self.test_service.add_rent(1,2)
        self.assertEqual(self.test_service.find_max_rented_movies([Movie(1, "Trinity", "nice movie", "action"),Movie(2, "Film", "ok movie", "horror")], 2,1,[]),["Trinity"])
    
        self.test_service.add_rent(2,2)
        self.assertEqual(self.test_service.find_max_rented_movies([Movie(1, "Trinity", "nice movie", "action"),Movie(2, "Film", "ok movie", "horror")], 2,1,[]),["Trinity","Film"])
    
    def testGetTop30(self):
        self.assertEqual(self.test_service.get_the30percent(["test"],[],0),["test"])
        self.assertEqual(self.test_service.get_the30percent([1,2,3,4,5,6,7,8,9],[],3),[1,2,3])
    
    def testReportByName(self):
        self.assertRaises(CRUDErrors, self.test_service.report_clients_by_name, [])

        self.test_service.add_rent(1,1)
        self.test_service.add_rent(2,1)
        self.test_service.add_rent(1,2)
        self.test_service.report_clients_by_name(self.test_clients.get_all())
    
    def testReportByRentals(self):
        self.assertRaises(CRUDErrors, self.test_service.report_clients_by_rentals, [])
        
        self.test_service.add_rent(1,1)
        self.test_service.add_rent(2,1)
        self.test_service.add_rent(1,2)
        self.test_service.report_clients_by_rentals(self.test_clients.get_all())
    
    def testReportMostRented(self):
        self.assertRaises(CRUDErrors, self.test_service.report_most_rented_movies, [])
        
        self.test_service.add_rent(1,1)
        self.test_service.add_rent(2,1)
        self.test_service.add_rent(1,2)
        self.assertEqual(self.test_service.report_most_rented_movies(self.test_movies.get_all()),self.test_service.find_max_rented_movies([Movie(1, "Trinity", "nice movie", "action"),Movie(2, "Film", "ok movie", "horror")], 2,1,[]))
        
        self.test_service.add_rent(2,2)
        self.assertEqual(self.test_service.report_most_rented_movies(self.test_movies.get_all()),self.test_service.find_max_rented_movies([Movie(1, "Trinity", "nice movie", "action"),Movie(2, "Film", "ok movie", "horror")], 2,1,[]))
        
    def testReportTop30Clients(self):
        self.test_service.add_rent(1,1)
        self.test_service.add_rent(2,1)
        self.test_service.add_rent(1,2)
        self.assertEqual(str(self.test_service.report_top_30percent_clients(self.test_clients.get_all())),"[name: Alin; rentals: 2]")
        self.assertRaises(CRUDErrors, self.test_service.report_top_30percent_clients, [])
            
    def testReportTop30Moviess(self):
        self.test_service.add_rent(1,1)
        self.test_service.add_rent(2,1)
        self.test_service.add_rent(1,2)
        self.assertEqual(str(self.test_service.report_top_30percent_movies(self.test_movies.get_all())),"[name: Trinity; rentals: 2]")
        self.assertRaises(CRUDErrors, self.test_service.report_top_30percent_movies, [])
    