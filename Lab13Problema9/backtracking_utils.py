'''
Created on Jan 6, 2024

@author: Cristian
'''
from console import solution_print

def backtracking_iter(l,points,n,found):
    """
    param: l=o lista care va reprezenta o multime de minim 3 index-uri (numere naturale >0)
           points=lista care reprezinta multimea de puncte citite
           n=numarul de puncte
           found=a list that is modified when a solution is found
    """
    stack=[l[:]]
    while stack:
        l = stack.pop()
        l.append(0)
        for i in range(n):
            if len(l)>n+1: break
            l[-1]=i
            if consistent(l, len(l)-1):
                if len(l) >= 3 and solution(l, len(l)-1, points):
                    solution_print(l, len(l)-1, points)
                    if found==[]: found.append(1)
                stack.append(l[:])
        l.pop()

def backtracking_rec(l,points,n,found):
    """
    param: l=o lista care va reprezenta o multime de minim 3 index-uri (numere naturale >0)
           points=lista care reprezinta multimea de puncte citite
           n=numarul de puncte
           found=a list that is modified when a solution is found
    """
    if len(l)>n: return
    l.append(0)
    for i in range(n):
        l[-1]=i
        if consistent(l, len(l)-1):
            if len(l)>=3 and solution(l, len(l)-1, points):
                solution_print(l, len(l)-1, points)
                if found==[]: found.append(1)
            backtracking_rec(l, points, n, found)
    l.pop()

def consistent(l,k):
    """
    param: l=o lista care va reprezenta o multime de minim 3 index-uri (numere naturale >0)
           k=un index
    return: True, daca lista generata pana acum este o multime
            False, altfel
    """
    if k==1:
        return True
    if l[k]>l[k-1]:
        return True
    return False

def solution(l,k,points):
    """
    param: l=o lista care va reprezenta o multime de minim 3 index-uri (numere naturale >0)
           k=numarul de elemente din l
           points=lista care reprezinta multimea de puncte citite
    """
    for i in range(1,k-1):
        for j in range(i+1,k):
            for t in range(j+1,k+1):
                if collinear(points[l[i]],points[l[j]],points[l[t]]):
                    return True
    return False

def collinear(a,b,c):
    """
    formula utilizata si adaptata: determinantul format cu coord punctelor sa fie 0
    params: a,b,c=obiecte de tip Punct
    return: True, daca punctele sunt coliniare
            False, altfel
    """
    if (b.get_x()-a.get_x())*(c.get_y()-a.get_y())==(c.get_x()-a.get_x())*(b.get_y()-a.get_y()): return True
    return False