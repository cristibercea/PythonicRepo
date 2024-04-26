'''
Created on Oct 22, 2023

@author: Cristian
'''

from TaskFunctions import citire, actualizare, gaseste_cheltuieli_mai_mari_decat_suma, gaseste_cheltuieli_mai_mici_decat_suma_mai_vechi_decat_zi, gaseste_cheltuieli_dupa_tip, filtraretip,face_eliminarea,suma_totala_tip, cheltuieli_sume_egale, sortare_dupa_tip, zile_suma_totala_max, undo
from Interface import info,err,afisare_date_filtrate,afisare_suma_totala,afislista

#FUNCTIA SCHELET
def taskSelecter(userin,data,alldata,operations): 
    #MODIFICA ASTFEL INCAT SA NU MAI RETURNEZE NUMELE OPERATIEI CAND NU S-A MODIFICAT EFECTIV LISTA DATA
    """
    selecteaza task-ul in functie de codul acestuia, furnizat prin lista comm.
    input: lista "comm", care contine un string reprezentand comanda introdusa de utilizator
           daca "comm[0]" contine o alta valoare decat unul din codurile operatiilor, functia returneaza -2
           lista "data", care stocheaza toate cheltuielile introduse de utilizator
    return: numele ultimei operatii efectuate (+anumiti parametrii)
            -1 daca una din operatiile care modifica lista de cheltuieli nu a avut niciun efect asupra listei
    """
    match userin[0]:
        case "read":
            data.append(userin[1])
            alldata.append(userin[1])
            info("","",4)
            return ["citit"]
        case "update":
            if len(data)==0:
                err(5)
            else:
                r=actualizare(data,userin[1])
                if r==0:
                    alldata.append(userin[1])
                    return ["citit"]
                if r==1:
                    alldata.append(userin[1])
                    return ["actualizat"]
            return -1
        case "2a":
            aux=citire("-->Introduceti ziua: ", 5)
            dataaux=face_eliminarea(data,aux,11,12,3)
            if dataaux!=-1:
                data=dataaux
                afislista(data)
                return ["sters1",aux]
            return -1
        case "2b":
            aux=citire("-->Introduceti ziua de inceput si ziua de final ale perioadei (cu virgula si spatiu intre ele[\", \"]): ", 6)
            dataaux=face_eliminarea(data,aux,13,14,4)
            if dataaux!=-1:
                data=dataaux
                afislista(data)
                return ["sters2",aux]
            return -1
        case "2c":
            aux=filtraretip()
            dataaux=face_eliminarea(data,aux,7,8,1)
            if dataaux!=-1:
                data=dataaux
                afislista(data)
                return ["sters3",aux]
            return -1
        case "search":
            suma=userin[1][0]
            d=gaseste_cheltuieli_mai_mari_decat_suma(data,suma)
            afisare_date_filtrate(d,2,str(suma), "")
            return "caut1"
        case "3b":
            aux=citire("-->Introduceti ziua si suma (cu virgula si spatiu intre ele[\", \"]): ", 4)
            zi=aux[0]
            suma=aux[1]
            d=gaseste_cheltuieli_mai_mici_decat_suma_mai_vechi_decat_zi(data,zi,suma)
            afisare_date_filtrate(d,3,str(aux[1]),str(aux[0]))
            return "caut2"
        case "3c":
            aux=filtraretip()
            tip=aux[0]
            d=gaseste_cheltuieli_dupa_tip(data,tip)
            afisare_date_filtrate(d,6,aux[0],"")
            return "caut3"
        case "4a":
            if len(data)!=0:
                aux=filtraretip()
                s=suma_totala_tip(data, aux[0])
                afisare_suma_totala(s,aux)
                return "raport1"
            else: 
                err(0)
                return -1
        case "4b":
            if len(data)!=0:
                aux=zile_suma_totala_max(data)
                afisare_date_filtrate(aux, 0, "", "")
                return "raport2"
            else:
                err(0)
                return -1
        case "4c":
            if len(data)!=0:
                aux=citire("-->Introduceti suma: ", 3)
                d=cheltuieli_sume_egale(data, aux[0])
                afisare_date_filtrate(d, 0, "", "")
                return "raport3"
            else:
                err(0)
                return -1
        case "4d":
            if len(data)!=0:
                d=sortare_dupa_tip(data)
                afisare_date_filtrate(d, 0, "", "")
                return "raport4"
            else:
                err(0)
                return -1
        case "elim":
            userin[1]=filtraretip(userin[1])
            if userin[1]!=-1:
                dataaux=face_eliminarea(data,userin[1],7,8,1)
                if dataaux!=-1:
                    data=dataaux
                    afislista(data)
                    return ["filtru1", aux]
            return [-1]
        case "5b":
            aux=citire("-->Introduceti suma: ", 3)
            dataaux=face_eliminarea(data,aux,9,10,2)
            if dataaux!=-1:
                data=dataaux
                afislista(data)
                return ["filtru2",aux]
            return -1
        case "undo":
            if operations!=[]:
                if operations[-1] in [["citit"],["actualizat"]]:
                    alldata.pop()
                data.clear()
                data=undo(alldata,operations)
            else:
                err(10)
            return ["undo",data]
        case "exit":
            return [-101]
    return [-2]
