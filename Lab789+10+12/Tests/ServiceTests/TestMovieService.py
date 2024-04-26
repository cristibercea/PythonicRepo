'''
Created on Dec 2, 2023

@author: Cristian
'''
import unittest
from random import seed
from Domain.Entities import Movie
from Controller.Movie_controller import ServiceMovie
from Repository.MovieRepository import MovieRepository
from Domain.Validators import CRUDErrors, MovieValidator, RepositoryError
   
class TestCaseMovieService(unittest.TestCase):
    def setUp(self):
        self.test_movies = MovieRepository(MovieValidator())
        self.test_service = ServiceMovie(self.test_movies)
    
    def testAddMovie(self):    
        self.test_service.add_movie(1, "name", "description", "genre")
        self.assertRaises(CRUDErrors, self.test_service.add_movie, 1, "", "description", "")
    
    def testGetAll(self):
        self.test_service.add_movie(1, "name", "description", "genre")
        self.assertEqual(self.test_service.get_all(),self.test_movies.get_all())
    
    def testEditMovie(self):
        self.assertRaises(RepositoryError, self.test_service.edit_movie, 1, "name", "desption", "nre")
        self.assertRaises(CRUDErrors, self.test_service.edit_movie, 1, "", "description", "")
        
        self.test_service.add_movie(1, "name", "description", "genre")
        self.test_service.edit_movie(1, "name", "desption", "nre")
    
    def testFindMovie(self):
        self.test_service.add_movie(1, "name", "description", "genre")
        self.test_service.find_movie(1)
        self.assertRaises(CRUDErrors, self.test_service.find_movie, 133)
    
    def testDeleteMovie(self):
        self.test_service.add_movie(1, "name", "description", "genre")
        self.test_service.del_movie(1)
        self.assertRaises(RepositoryError, self.test_service.del_movie, 2)
    
    def testAddRandomMovie(self):
        seed(5)
        t=self.test_service.add_random_movie(1)
        m=Movie(1, "ixlzwxuqao", "ubfd", "phmrds")
        self.assertEqual(m.get_movie_description(),t.get_movie_description())
        self.assertEqual(m.get_movie_name(),t.get_movie_name())
        self.assertEqual(m.get_movie_genre(),t.get_movie_genre())
