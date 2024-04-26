'''
Created on Oct 22, 2023

@author: Cristian
'''
from Interface import err, info

#GETTERS/SETTERS
def get_zi(t):
    return t['zi']

def get_suma(t):
    return t['suma']

def get_tip(t):
    return t['tip']

def set_zi(t):
    return t[0]

def set_suma(t):
    return t[1]

def set_tip(t):
    return t[2]

def creaza_cheltuiala(b):
    aux={}
    aux["zi"]=set_zi(b)
    aux["suma"]=set_suma(b)
    aux["tip"]=set_tip(b)
    return aux

def set_tip_cheltuiala(a): 
    """
    stabileste tipul de cheltuiala pentru setul curent de date
    input: stringul a, care contine tipul de cheltuiala
    return: stringul a, reprezentand unul din cele 5 tipuri de cheltuieli valide pentru acest program
    """
    if a not in ["mancare", "intretinere", "imbracaminte", "telefon"]: a="altele" 
    return a

#FUNCTII CALCUL
def transformator_inputs_str_to_int(strn,a,tip): 
    """
    transforma ziua si suma de bani citite in valori de tip int sau afiseaza mesaj de eroare in cazul in care acestea nu corespund
    input: strn-un mesaj pentru citire de tip string
           a- lista cu string-uri continand datele unei cheltuieli
           tip- variabila de tip int care defineste tipul de citire care va fi folosit pentru a citi din nou a, daca input-ul nu a putut fi transformat in int
    return: a- lista de forma [int,int,str] reprezentand datele formatate ale cheltuielii, pentru tip==2
            a- lista de forma [int, int] reprezentand ziua si suma introduse de utilizator pentru anumite operatii
    """
    try:
        if tip==6:
            a["zi1"]=int(a["zi1"])
            a["zi2"]=int(a["zi2"])
            if a["zi1"]>31 or a["zi2"]>31:
                err(4)
                a=citire(strn)
            elif a["zi1"]>=a["zi2"]:
                err(8)
                a=citire(strn)
        else:
            a["zi"]=int(get_zi(a))
            a["suma"]=int(get_suma(a))
            if a["zi"]>31:
                err(4)
                a=citire(strn)
    except ValueError:
        if tip==6:
            err(9)
        else:
            err(3)
        a=citire(strn)
    return a

def filtraretip(aux): 
    """
    se asigura ca utilizatorul introduce un tip de cheltuiala valid
    return: aux- o lista cu un string reprezentand unul din cele 5 tipuri valide de cheltuieli
    """
    if aux not in ["mancare", "intretinere", "imbracaminte", "telefon", "altele"]:
        err(7)
        return -1
    return aux 

def citire(strn):
    """
    input: strn- mesaj pentru citire (str)
           tip- tipul de citire care se va efectua (int)
    citire: tip==1 <= citeste comanda    tip>=2 <= citeste date
    functia principala pentru citit, citeste si salveaza datele daca sunt corecte sau cere reintroducerea lor daca sunt eronate
    returneaza:
    -pentru tip==1: o lista cu un singur string care reprezinta o comanda (sau un tip) introdusa de utilizator
    -pentru tip==2: un dictionar de tipul {"zi":int, "suma":int, "tip":str} reprezentand o cheltuiala din lista de cheltuieli
    -pentru tip==3: o lista cu un singur int care reprezinta suma introdusa de utilizator
    -pentru tip==4: o lista de tipul [int, int] care contine ziua si suma introduse de user
    -pentru tip==5: o lista de tipul [int] care contine ziua introdusa de user
    -pentru tip==6: un dictionar de tipul {"zi1":int, "zi2":int} care contine ziua de inceput si ziua de final ale unei perioade introduse de user
    """
    c=input(strn)
    a=[]
    c=c.split(" ")
    b=c[1:]
    if c[0]=="read" or c[0]=="update":
        if len(b)>2:
                a=creaza_cheltuiala(b)
                a=transformator_inputs_str_to_int(strn,a,2)
                a["tip"]=set_tip_cheltuiala(get_tip(a))        
        elif len(b)<=2:
            err(2)
            a=citire(strn)
    elif c[0]=="search": 
            a=b
            try:
                a[0]=int(a[0])
                """if tip==5:
                    if a[0]>31:
                        err(4)
                        a=citire(strn)"""
            except ValueError:
                err(6)
                a=citire(strn)
    """elif tip==4:
            a=b
            a=transformator_inputs_str_to_int(strn,a,tip)
        elif tip==6:
            a={}
            a["zi1"]=b[0]
            a["zi2"]=b[1]
            a=transformator_inputs_str_to_int(strn,a,tip)
    """
    return [c[0],a]

def face_eliminarea(data,aux,t1,t2,op):
    """
    input: data -lista principala de cheltuieli
           aux -o lista/dictionar reprezentand datele unei cheltuieli nou introdusa de utilizator ( [int, int, str]/ [int]/ {int, int}/ [str] )
           t1,t2 -variabile de tip int, care reprezinta tipurile de mesaje de informare
           op -int, reprezinta numarul subfunctiei de la operatia 5
    return: data -lista principala de cheltuieli modificata
    output: se printeaza doua mesaje de informare
    """
    if op==1:
        x=elimina_cheltuieli_dupa_tip(data, aux[0])
    elif op==2:
        x=elimina_cheltuieli_mai_mici_decat_suma(data,aux[0])
    elif op==3:
        x=sterge_cheltuieli_dupa_zi(data, aux[0])
    elif op==4: 
        x=sterge_cheltuieli_din_perioada(data, aux["zi1"], aux["zi2"])
    if len(data)==len(x):
        if op==4:
            info(str(aux["zi1"]),str(aux["zi2"]),t1)
        else:
            info(str(aux[0]),"",t1) 
        return -1
    else:
        if op==4:
            info(str(len(data)-len(x)),aux,t2)
        else:
            info(str(len(data)-len(x)),str(aux[0]),t2)
        data.clear()
        for item in x:
            data.append(item)
        return data

def actualizare(data, aux): 
    """
    actualizeaza suma pt cheltuiala de un anume tip, dintr-o anume zi, daca exista; 
    daca nu exista, o introduce pur si simplu in lista de cheltuieli
    input: data -lista principala de cheltuieli
           aux -dictionar reprezentand datele unei cheltuieli nou introdusa de utilizator {"zi":int, "suma":int, "tip":str}
    output: se printeaza mesaj de eroare;
            se modifica lista data:
                se introduce o noua cheltuiala
                se modifica cheltuiala din ziua aux[0] si de tipul aux[2]
    """
    for i in range(0, len(data)):
        if get_zi(data[i])==get_zi(aux) and get_tip(data[i])==get_tip(aux):
            if get_suma(data[i])==get_suma(aux):
                info(str(get_zi(aux)),get_tip(aux),15)
                return 2
            else:
                data[i]=aux
                info("","",5)
                return 1
    info(str(get_zi(aux)),get_tip(aux),1)
    data.append(aux)
    return 0

def gaseste_cheltuieli_mai_mari_decat_suma(data,suma): #cerinta 3, subpunct 1
    """
    input: data -lista principala de cheltuieli
           suma -int care reprezinta suma introdusa de user
    return: d -lista care contine toate cheltuielile cu sume mai mari decat "suma"
    """
    d=[]  
    for t in data:
        if get_suma(t)>suma:
            d.append(t)
    return d 

def gaseste_cheltuieli_mai_mici_decat_suma_mai_vechi_decat_zi(data,zi,suma): #cerinta 3, subpunct 2
    """
    input: data -lista principala de cheltuieli
           zi,suma -[int,int] care reprezinta ziua si suma introduse de user
    return: d -lista care contine toate cheltuielile cu sume mai mici decat "suma" si mai vechi decat "zi"
    """
    d=[]
    for t in data:
        if get_zi(t)<zi and get_suma(t)<suma:
            d.append(t)
    return d 

def gaseste_cheltuieli_dupa_tip(data,tip): #cerinta 3, subpunct 3
    """
    input: data -lista principala de cheltuieli
           tip -str care reprezinta un tip de cheltuiala introdus de user
    return: d -lista care contine toate cheltuielile de tipul "tip"
    """
    d=[]
    for t in data:
        if get_tip(t)==tip:
            d.append(t)
    return d 
    
def elimina_cheltuieli_dupa_tip(data,tip): #cerinta 5, subpunct 1
    """
    input: data -lista principala de cheltuieli
           tip -str care reprezinta un tip de cheltuiala introdus de user
    return: dataaux -lista care contine toate cheltuielile care nu sunt de tipul "tip"
    """
    dataaux=[]
    for x in data:
        if get_tip(x)!=tip:
            dataaux.append(x)
    return dataaux

def elimina_cheltuieli_mai_mici_decat_suma(data,suma): #cerinta 5, subpunct 2 
    """
    input: data -lista principala de cheltuieli
           suma -int care reprezinta suma introdusa de user
    return: dataaux -lista care contine toate cheltuielile cu sume mai mari decat "suma"
    """
    dataaux=[]
    for x in data:
        if get_suma(x)>=suma:
            dataaux.append(x)
    return dataaux

def suma_totala_tip(data, tip): #cerinta 4, subpunct 1
    """
    input: data -lista principala de cheltuieli
           tip -tip de cheltuiala introdus de user
    return: s -suma totala pentru cheltuielile de tip "tip"
    """
    s=0
    for t in data:
        if get_tip(t)==tip:
            s+=t["suma"]
    return s

def zile_suma_totala_max(data): #cerinta 4, subpunct 2
    """
    input: data -lista principala de cheltuieli
    return: zi -lista cu zilele in care suma cheltuita e maxima
    """
    daysum=[]
    z=0
    maxsum=0
    zi=[]
    for t in data:
        if get_zi(t)>z:
            z=get_zi(t)
    for i in range(0, z):
        daysum.append(0)
    for t in data:
        daysum[get_zi(t)-1]+=get_suma(t)
    for t in daysum:
        if t>maxsum:
            maxsum=t
    for i in range(0, z):
        if maxsum==daysum[i]:
            zi.append(i+1)
    return zi

def cheltuieli_sume_egale(data,suma): #cerinta 4, subpunct 3
    """
    input: data -lista principala de cheltuieli
           suma -int care reprezinta suma introdusa de user
    return: d -lista care contine toate cheltuielile cu sume egale cu "suma"
    """
    dataaux=[]
    for x in data:
        if get_suma(x)==suma:
            dataaux.append(x)
    return dataaux

def sortare_dupa_tip(data): #cerinta 4, subpunct 4
    """
    input: data -lista principala de cheltuieli
    return: d -lista care contine cheltuielile ordonate alfabetic dupa tip
    """
    d=[]
    aux=["altele", "imbracaminte", "intretinere", "mancare", "telefon"]
    for x in aux:    
        for t in data:
            if get_tip(t)==x:
                d.append(t)
    return d

def sterge_cheltuieli_dupa_zi(data,zi): #cerinta 5, subpunct 1
    """
    input: data -lista principala de cheltuieli
           zi -int care reprezinta o zi introdusa de user
    return: dataaux -lista care contine toate cheltuielile care nu sunt in ziua "zi"
    """
    dataaux=[]
    for x in data:
        if get_zi(x)!=zi:
            dataaux.append(x)
    return dataaux

def sterge_cheltuieli_din_perioada(data,zi1,zi2): #cerinta 5, subpunct 1
    """
    input: data -lista principala de cheltuieli
           zi1,zi2 -int-uri care reprezinta cate o zi introdusa de user
    return: dataaux -lista care contine toate cheltuielile care nu sunt in perioada zi1-zi2
    """
    dataaux=[]
    for x in data:
        if get_zi(x)<zi1 or get_zi(x)>zi2:
            dataaux.append(x)
    return dataaux

def undo(alldata,operations): #cerinta 6
    """
    input: alldata- lista de dictionare cu toate cheltuielile introduse vreodata in program
           operations- lista cu operatiile facute pana in acest punct
    return: data- lista de date principala, revenita la stadiul sau inaintea efectuarii ultimei operatii: operations[-1]
    """
    if len(operations)>1:
        index=0
        data=[]
        for i in range(0, len(operations)-1):
            if operations[i]=="citit":
                data.append(alldata[index])
                index+=1
            if operations[i]=="actualizat":
                actualizare(data,alldata[index])
                index+=1
            if operations[i][0]=="filtru1":
                data=face_eliminarea(data,operations[i][1],7,8,1)
            if operations[i][0]=="filtru2":
                data=face_eliminarea(data,operations[i][1],9,10,2)
            if operations[i][0]=="sters1":
                data=face_eliminarea(data,operations[i][1],11,12,3)
            if operations[i][0]=="sters2":
                data=face_eliminarea(data,operations[i][1],13,14,4)
            if operations[i][0]=="sters3":
                data=face_eliminarea(data,operations[i][1],7,8,1)
        operations.pop()
        return data
    else:
        operations.pop()
        return []
    