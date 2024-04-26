'''
Created on Jan 5, 2024

@author: Cristian
'''
import unittest
from domain import Punct
from backtracking_utils import collinear, solution, consistent

class Test(unittest.TestCase):
    def setUp(self):
        self.a=[]
        self.a.append(Punct(1,9))
        self.a.append(Punct(7,2))
        self.a.append(Punct(3,3))
        self.a.append(Punct(1,6))
        self.a.append(Punct(4,0))
        
    def test_get_x(self):
        self.assertEqual(self.a[0].get_x(), 1)
        self.assertEqual(self.a[1].get_x(), 7)
        self.assertEqual(self.a[2].get_x(), 3)
        self.assertEqual(self.a[3].get_x(), 1)
        self.assertEqual(self.a[4].get_x(), 4)
        
    def test_get_y(self):
        self.assertEqual(self.a[0].get_y(), 9)
        self.assertEqual(self.a[1].get_y(), 2)
        self.assertEqual(self.a[2].get_y(), 3)
        self.assertEqual(self.a[3].get_y(), 6)
        self.assertEqual(self.a[4].get_y(), 0)
        
    def test_collinear(self):
        self.assertTrue(collinear(self.a[0], self.a[2], self.a[4]))
        self.assertFalse(collinear(self.a[0], Punct(5,5), self.a[4]))
        self.assertTrue(collinear(self.a[2], Punct(5,5), Punct(999,999)))
        self.assertFalse(collinear(self.a[0], Punct(1,8), self.a[4]))
        
    def test_solution(self):
        self.assertTrue(solution([0,0,2,3,4],4,self.a))
        self.assertFalse(solution([0,2,3,4],3,self.a))
        self.assertFalse(solution([0,1,2,3,4],4,self.a))
        self.assertFalse(solution([0,2,3,4,1],4,self.a))
        
    def test_consistent(self):
        self.assertTrue(consistent([0,1],1))
        self.assertFalse(consistent([0,1],0))
        self.assertTrue(consistent([0,1,5,999],3))
        self.assertFalse(consistent([0,777,1],2))
