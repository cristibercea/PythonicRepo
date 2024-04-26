'''
Created on Jan 6, 2024

@author: Cristian
'''

class Punct:
    """
    obiect de tip punct, cu doua coordonate in plan: x si y
    """
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
        
    def get_x(self): return self.__x
    def get_y(self): return self.__y
    def __str__(self): return "("+str(self.__x)+","+str(self.__y)+")"
    def __repr__(self): return str(self)