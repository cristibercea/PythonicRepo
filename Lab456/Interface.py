'''
Created on Oct 22, 2023

@author: Cristian

Aici se gasesc functiile pentru UI din consola
'''
#FUNCTII INTERFATA
def interface(): #printeaza meniul principal
    print("\n\n             ~Aplicatie cheltuieli lunare~\n\n")
    print("   Lista de comenzi:\n")
    print("     1. Adaugare:")
    print(" -adaugare cheltuiala noua; (command: read + cheltuiala)")
    print(" -actualizare cheltuiala existenta; (command: update + cheltuiala)\n")
    print("     2. Stergere:")
    print(" -stergere cheltuieli pentru o anumita zi; (COD: 2a)")
    print(" -stergere cheltuieli dintr-un interval de zile; (COD: 2b)")
    print(" -stergere cheltuieli de un anumit tip; (COD: 2c)\n")
    print("     3. Cautare:")
    print(" -afisare cheltuieli mai mari decat o anumita suma; (command: search + \"suma\")")
    print(" -afisare cheltuieli efectuate inaintea unei zile si mai mici decat o suma anume; (COD: 3b)")
    print(" -afisare cheltuieli de un anumit tip; (COD: 3c)\n")
    print("     4. Rapoarte:")
    print(" -afisare suma totala pentru un tip de cheltuieli; (COD: 4a)")
    print(" -afisare ziua cu suma maxima de cheltuieli; (COD: 4b)")
    print(" -afisare cheltuieli care au o anumita suma; (COD: 4c)")
    print(" -afisare cheltuieli, sortate dupa tip; (COD: 4d)\n")
    print("     5. Eliminare:")
    print(" -eliminare cheltuieli de un anume tip; (command: elim + \"tip\")")
    print(" -eliminare cheltuieli mai mici decat o suma; (COD: 5b)\n")
    print("     6. UNDO:\n -anuleaza efectul ultimei operatii care modifica lista de date (stergerea, citirea, actualizarea, eliminarea).  (COD: 6)\n")
    print("[!] Pentru a iesi din aplicatie introduceti codul: x")
    print("[!] Tipuri de cheltuieli: \"mancare\", \"intretinere\", \"imbracaminte\", \"telefon\", \"altele\"\n")

def info(s1,s2,nr): #printeaza mesajul de tip info, avand 2 parametrii de tip string sau, pentru nr==14, s2 e de tip lista de doua int-uri
    match nr:
        case 1:
            print("\n [INFO] Cheltuiala din ziua "+s1+" si de tipul \""+s2+"\" nu a fost gasita! Programul a adaugat-o acum, automat, in lista de cheltuieli! \n")
        case 2:
            print(" [INFO] Nu s-a gasit nicio cheltuiala mai mare decat suma "+s1+"! ")
        case 3:
            print(" [INFO] Nu s-a gasit nicio cheltuiala, inainte de ziua "+s2+", mai mica decat suma "+s1+"! ")
        case 4:
            print("\n [INFO] Date salvate cu succes! \n")
        case 5:
            print("\n [INFO] Date actualizate cu succes! \n")
        case 6:
            print(" [INFO] Nu s-a gasit nicio cheltuiala de tipul \""+s1+"\"! ")
        case 7:
            print(" [INFO] Nu s-a gasit nicio cheltuiala de tipul \""+s1+"\"! \n")
        case 8:
            print(" [INFO] S-au eliminat cu succes "+s1+" cheltuieli de tipul \""+s2+"\"! \n")
        case 9:
            print(" [INFO] Nu s-a gasit nicio cheltuiala cu o suma mai mica decat \""+s1+"\"! \n")
        case 10:
            print(" [INFO] S-au eliminat cu succes "+s1+" cheltuieli cu sume mai mici decat \""+s2+"\"! \n")
        case 11:
            print(" [INFO] Nu s-a gasit nicio cheltuiala in ziua \""+s1+"\"! \n")
        case 12:
            print(" [INFO] S-au eliminat cu succes "+s1+" cheltuieli din ziua \""+s2+"\"! \n")
        case 13:
            print(" [INFO] Nu s-a gasit nicio cheltuiala in perioada \""+s1+"\" - \""+s2+"\"! \n")
        case 14:
            print(" [INFO] S-au eliminat cu succes "+s1+" cheltuieli din perioada \""+str(s2["zi1"])+"\" - \""+str(s2["zi2"])+"\"! \n")
        case 15:
            print(" [INFO] Exista deja o cheltuiala in ziua "+s1+", de tipul "+s2+", cu suma data! \n")

def err(nr): #printeaza mesajul de tip eroare, in functie de numarul erorii
    match nr:
        case 0:
            print(" [ERROR] Atentie! Nu este salvata nicio cheltuiala! \n")
        case 1:
            print(" [ERROR] Comanda necunoscuta, mai incearca! \n")
        case 2:
            print(" [ERROR] Atentie! Nu ai introdus toate datele cheltuielii! (zi, suma, tip) \n")
        case 3:
            print(" [ERROR] Atentie! Ziua si suma trebuie sa fie numere naturale! \n")
        case 4:
            print(" [ERROR] Atentie! Luna are maxim 31 de zile! \n")
        case 5:
            print(" [ERROR] Atentie! Nu poti actualiza nicio cheltuiala, deoarece inca nu ai introdus niciuna! (Incearca sa introduci o cheltuiala prin comanda cu COD: 1a) \n")
        case 6:
            print(" [ERROR] Suma trebuie sa fie un numar! \n")
        case 7:
            print(" [ERROR] Tip de cheltuieli necunoscut! (Tipuri posibile: \"mancare\", \"intretinere\", \"imbracaminte\", \"telefon\", \"altele\") \n")
        case 8:
            print(" [ERROR] Ziua de inceput a perioadei trebuie sa fie mai mica decat ziua de sfarsit a acesteia! \n")
        case 9:
            print(" [ERROR] Atentie! Zilele trebie sa fie numere naturale! \n")
        case 10:
            print(" [ERROR] Atentie! Inca nu s-a efectuat nicio operatie! \n")
            
def verif(t):
    """
    input: t- un termen care contine un int sau un str
    output: mesaj de eroare daca t==-1
    """
    if t==-2: err(1)
    
def afislista(data):
    """
    input: data- lista principala de cheltuieli 
    output: se printeaza lista, daca aceasta nu este vida
    """
    if len(data)!=0:
        print("Cheltuieli salvate: " + str(data)) #verificarea evolutiei listei de cheltuieli
        print()
    
def afisare_date_filtrate(d,tip,s1,s2):
    """
    input: d- lista de date filtrata
           tip- int care reprezinta tipul de mesaj din functia "info" care sa fie afisat
           s1,s2- date de tip str care contin diferite informatii care vor fi afisate, daca este cazul, de catre functia "info"
    output: se printeaza mesaj de informare sau lista de date
    """
    if len(d)==0:
        info(s1,s2,tip)
    else:
        print(d)
        
def afisare_suma_totala(s,aux):
    if s==0: 
        info(aux[0], "", 7)
    else: 
        print("Suma totala pentru tipul de cheltuieli \""+aux[0]+"\" este: "+ str(s)+"\n")
