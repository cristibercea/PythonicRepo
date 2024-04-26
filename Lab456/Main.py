'''
Created on Oct 21, 2023

@author: Cristian
'''
import Interface
from Manager import taskSelecter
from TaskFunctions import citire
from Testers import test_undo,test_set_tip_cheltuiala,test_gaseste_cheltuieli_mai_mari_decat_suma,test_gaseste_cheltuieli_dupa_tip,test_gaseste_cheltuieli_mai_mici_decat_suma_mai_vechi_decat_zi,test_elimina_cheltuieli_dupa_tip,test_elimina_cheltuieli_mai_mici_decat_suma, test_cheltuieli_sume_egale, test_sortare_dupa_tip, test_suma_totala_tip, test_sterge_cheltuieli_dupa_zi, test_sterge_cheltuieli_din_perioada, test_zile_suma_totala_max


#ZONA DE TESTARE
test_set_tip_cheltuiala()
test_elimina_cheltuieli_dupa_tip()
test_elimina_cheltuieli_mai_mici_decat_suma()
test_gaseste_cheltuieli_mai_mari_decat_suma()
test_gaseste_cheltuieli_dupa_tip()
test_gaseste_cheltuieli_mai_mici_decat_suma_mai_vechi_decat_zi()
test_suma_totala_tip()
test_zile_suma_totala_max()
test_sortare_dupa_tip()
test_cheltuieli_sume_egale()
test_sterge_cheltuieli_dupa_zi()
test_sterge_cheltuieli_din_perioada()
test_undo()

#PARTEA MAIN A PROGRAMULUI
def run():
    """
    functia principala de rulare a programului
    asigura executarea continua a comenzilor, pana cand t=-101,adica utilizatorul inchide programul intentionat
    data - lista principala de cheltuieli 
    operations - lista de tip [str, [], ...]; este istoricul operatiilor efectuate de program, cu parametrii corespunzatori; 
    """
    t=[0]
    data=[]
    alldata=[]
    operations=[]
    
    Interface.interface()
    
    while t[0]!=-101:
        aux=citire("-->Introduceti datele (comanda + parametrii): ")
        t=taskSelecter(aux,data,alldata,operations)
        
        Interface.verif(t)
        if t[0] in ["actualizat", "citit", "sters1","sters2", "sters3", "filtru1", "filtru2"]: 
            operations.append(t)
        print(operations) #debugging verification of operations
        if t[0]=="undo": 
            data=t[1] 
            Interface.afislista(data)
            #Interface.afislista(alldata) #debugging verification of undo
        if t[0] in ["actualizat", "citit"]: 
            Interface.afislista(data)
            Interface.afislista(alldata) #debugging verification of undo
        elif t[0]==-101: print("\n      ~Program execution stopped.\n")

run()
