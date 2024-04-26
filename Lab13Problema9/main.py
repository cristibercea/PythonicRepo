'''
Created on Jan 5, 2024

@author: Cristian
'''
"""
Rezolvați problema folosind BACKTRACKING, scrieți o varianta recursivă și una iterativă:

9). Se dau coordonatele pentru n puncte în plan. Determinați toate mulţimile de puncte cu
proprietatea că cel puţin trei puncte din mulţime sunt colineare. Tipăriţi un mesaj dacă
problema nu are soluţie.
"""
from backtracking_utils import backtracking_iter, backtracking_rec
from console import read, message, read_coords

def run():
    while True:
        command=-11
        while command>1 or command<-1: command=read("\n Inserati -1(opreste aplicatia), 0 (backtracing recursiv) sau 1 (backtracing iterativ): ")
        if command==-1: break
        points=[]
        n=read("\nDati numarul de puncte: ")
        read_coords(n,points)
        found=[]
        if command==0: backtracking_rec([0],points,n,found)
        if command==1: backtracking_iter([0],points,n,found)
        if found==[]: message() #nu s-a gasit nicio multimes
run()

""" n=6
    x1 =1 ; y1 =9
    x2 =3 ; y2 =3
    x3 =4 ; y3 =0
    x4 =5 ; y4 =5
    x5 =2 ; y5 =2
    x6 =9 ; y6 =1

---recursiv---
[(1,9), (3,3), (4,0)]
[(1,9), (3,3), (4,0), (5,5)]
[(1,9), (3,3), (4,0), (5,5), (2,2)]
[(1,9), (3,3), (4,0), (5,5), (2,2), (9,1)]
[(1,9), (3,3), (4,0), (5,5), (9,1)]
[(1,9), (3,3), (4,0), (2,2)]
[(1,9), (3,3), (4,0), (2,2), (9,1)]
[(1,9), (3,3), (4,0), (9,1)]
[(1,9), (3,3), (5,5), (2,2)]
[(1,9), (3,3), (5,5), (2,2), (9,1)]
[(1,9), (3,3), (5,5), (9,1)]
[(1,9), (4,0), (5,5), (2,2), (9,1)]
[(1,9), (4,0), (5,5), (9,1)]
[(1,9), (5,5), (2,2), (9,1)]
[(1,9), (5,5), (9,1)]
[(3,3), (4,0), (5,5), (2,2)]
[(3,3), (4,0), (5,5), (2,2), (9,1)]
[(3,3), (5,5), (2,2)]
[(3,3), (5,5), (2,2), (9,1)]

---iterativ---
[(3,3), (5,5), (2,2)]
[(3,3), (5,5), (2,2), (9,1)]
[(3,3), (4,0), (5,5), (2,2)]
[(3,3), (4,0), (5,5), (2,2), (9,1)]
[(1,9), (5,5), (9,1)]
[(1,9), (5,5), (2,2), (9,1)]
[(1,9), (4,0), (5,5), (9,1)]
[(1,9), (4,0), (5,5), (2,2), (9,1)]
[(1,9), (3,3), (4,0)]
[(1,9), (3,3), (5,5), (2,2)]
[(1,9), (3,3), (5,5), (9,1)]
[(1,9), (3,3), (5,5), (2,2), (9,1)]
[(1,9), (3,3), (4,0), (5,5)]
[(1,9), (3,3), (4,0), (2,2)]
[(1,9), (3,3), (4,0), (9,1)]
[(1,9), (3,3), (4,0), (2,2), (9,1)]
[(1,9), (3,3), (4,0), (5,5), (2,2)]
[(1,9), (3,3), (4,0), (5,5), (9,1)]
[(1,9), (3,3), (4,0), (5,5), (2,2), (9,1)]
"""