'''
Created on Jan 6, 2024

@author: Cristian
'''
from domain import Punct

def read(prompt):
    """
    param: prompt-string pentru citire
    return n- nr intreg
    """
    n=-1
    while n==-1:
        try:
            n=int(input(prompt))
            return n
        except ValueError: 
            print("\nInvalid input. Try again!")

def read_coords(n,points):
    for i in range(0,n):
        points.append(Punct(read("x"+str(i+1)+" = "),read("y"+str(i+1)+" = ")))
        print()
            
def message(): print("Nu s-au gasit multimi cu cel putin 3 puncte coliniare!")

def solution_print(l,k,points): 
    """
    param: l=o lista care va reprezenta o multime de minim 3 index-uri (numere naturale >0)
           k=numarul de elemente din l
           points=lista care reprezinta multimea de puncte citite
    """
    sol=[]
    
    for i in range(1,k+1): sol.append(points[l[i]])
    
    print(sol)
    print()