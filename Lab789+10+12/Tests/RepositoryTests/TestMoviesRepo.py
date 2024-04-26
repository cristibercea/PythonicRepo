'''
Created on Dec 2, 2023

@author: Cristian
'''
import unittest
from Domain.Validators import MovieValidator, ValidatorErrors, RepositoryError
from Domain.Entities import Movie
from Repository.MovieRepository import MovieRepository,MovieFileRepository

class testCaseMovieRepo(unittest.TestCase):
    def setUp(self):
        self.test=MovieRepository(MovieValidator())
        self.item=Movie(1, "Trinity", "nice movie", "action")
    
    def testStoreMovie(self):
        self.test.store(self.item)
        self.assertRaises(RepositoryError, self.test.store,Movie(1, "Trinity", "nice movie", "action"))
        self.assertRaises(ValidatorErrors, self.test.store,Movie(3, "", "nice movie", "action"))
    
    def testGetAllMovies(self):
        self.assertTrue(self.test.get_all()=={})
        self.test.store(self.item)
        self.assertEqual(self.test.get_all(),{1:self.item},"get-all error")
    
    def testUpdateMovie(self):
        self.assertRaises(RepositoryError, self.test.update,Movie(1, "Trinity", "nice movie", "action"))
        self.assertRaises(ValidatorErrors, self.test.update,Movie(1, "Trinity", "", "action"))
        self.test.store(self.item)
        self.test.update(self.item)
            
    def testFindMovieById(self):        
        self.assertTrue(self.test.find_by_id(1)==None)
        self.test.store(self.item)
        self.assertEqual(self.test.find_by_id(1),self.item,"find-by-id error")
        
    def testDeleteMovie(self):
        self.test.store(self.item)
        self.test.delete(self.item.get_id())
        self.assertRaises(RepositoryError, self.test.delete, 7)


class testCaseFileMovieRepo(unittest.TestCase):
    def setUp(self):
        self.test=MovieFileRepository(MovieValidator(),"testmovies.txt")
        self.item=Movie(3, "Trinity", "nice movie", "action")
        self.item1=Movie(1,"aaaawst","sryhtrjtf","fxtjl")
        self.item2=Movie(2,"Finch","Un film ok","drama")
    
    def tearDown(self):
        del_file=open("testmovies.txt",'w')
        del_file.close()
        self.test=MovieFileRepository(MovieValidator(),"testmovies.txt")
        self.test.store(self.item1)
        self.test.store(self.item2)
    
    def testStoreMovie(self):
        self.test.store(self.item)
        self.assertRaises(RepositoryError, self.test.store,Movie(1, "Trinity", "nice movie", "action"))
        self.assertRaises(ValidatorErrors, self.test.store,Movie(4, "", "nice movie", "action"))
    
    def testUpdateMovie(self):
        self.assertRaises(RepositoryError, self.test.update,Movie(3, "Trinity", "nice movie", "action"))
        self.assertRaises(ValidatorErrors, self.test.update,Movie(4, "Trinity", "", "action"))
        self.test.store(self.item)
        self.test.update(self.item)
            
    def testFindMovieById(self):        
        self.assertTrue(self.test.find_by_id(3)==None)
        self.test.store(self.item)
        self.assertEqual(self.test.find_by_id(3),self.item,"find-by-id error")
        
    def testDeleteMovie(self):
        self.test.store(self.item)
        self.test.delete(self.item.get_id())
        self.assertRaises(RepositoryError, self.test.delete, 7)
