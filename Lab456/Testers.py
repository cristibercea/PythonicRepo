'''
Created on Oct 23, 2023

@author: Cristian

Aici se gasesc functiile de test (assertions) ale functiilor de calcul pentru operatiile programului
'''

from TaskFunctions import undo,set_tip_cheltuiala,gaseste_cheltuieli_mai_mari_decat_suma,gaseste_cheltuieli_dupa_tip,gaseste_cheltuieli_mai_mici_decat_suma_mai_vechi_decat_zi,elimina_cheltuieli_mai_mici_decat_suma,elimina_cheltuieli_dupa_tip, suma_totala_tip, cheltuieli_sume_egale, sortare_dupa_tip, sterge_cheltuieli_dupa_zi, sterge_cheltuieli_din_perioada, zile_suma_totala_max

def test_set_tip_cheltuiala():
    t="telefon"
    assert set_tip_cheltuiala(" ")=="altele"
    #assert set_tip_cheltuiala(t)=="altele" #good assertion error
    #assert set_tip_cheltuiala(t)=="intretinere" #good assertion error
    assert set_tip_cheltuiala("adgfasegds")=="altele"
    assert set_tip_cheltuiala("imbracaminte")=="imbracaminte"
    assert set_tip_cheltuiala(t)=="telefon"

def test_gaseste_cheltuieli_mai_mari_decat_suma():
    test= [{"zi":12, "suma":123, "tip":"altele"},{"zi":30, "suma":478, "tip":"telefon"},{"zi":5, "suma":10, "tip":"imbracaminte"}]
    assert gaseste_cheltuieli_mai_mari_decat_suma([], 1)==[]
    #assert gaseste_cheltuieli_mai_mari_decat_suma(test, 100)==[[12, 123, "altele"]] #good assertion error
    #assert gaseste_cheltuieli_mai_mari_decat_suma(test, 1)==[] #good assertion error
    assert gaseste_cheltuieli_mai_mari_decat_suma(test, 100)==[{"zi":12, "suma":123, "tip":"altele"},{"zi":30, "suma":478, "tip":"telefon"}]
    assert gaseste_cheltuieli_mai_mari_decat_suma(test, 10000)==[]
    assert gaseste_cheltuieli_mai_mari_decat_suma(test, 1)==test

def test_gaseste_cheltuieli_dupa_tip():
    test= [{"zi":12, "suma":123, "tip":"altele"},{"zi":30, "suma":478, "tip":"telefon"},{"zi":5, "suma":10, "tip":"imbracaminte"}]
    assert gaseste_cheltuieli_dupa_tip([], "altele")==[]
    #assert gaseste_cheltuieli_dupa_tip(test, "telefon")==[[12, 123, "altele"]]#good assertion error
    #assert gaseste_cheltuieli_dupa_tip(test, "telefon")==[[5, 10, "imbracaminte"]]#good assertion error
    assert gaseste_cheltuieli_dupa_tip(test, "telefon")==[{"zi":30, "suma":478, "tip":"telefon"}]
    assert gaseste_cheltuieli_dupa_tip(test, "lsidfgersgfioh")==[]
    assert gaseste_cheltuieli_dupa_tip(test, "intretinere")==[]

def test_gaseste_cheltuieli_mai_mici_decat_suma_mai_vechi_decat_zi():
    test= [{"zi":12, "suma":123, "tip":"altele"},{"zi":30, "suma":478, "tip":"telefon"},{"zi":5, "suma":10, "tip":"imbracaminte"}]
    assert gaseste_cheltuieli_mai_mici_decat_suma_mai_vechi_decat_zi([], 1, 2355)==[]
    #assert gaseste_cheltuieli_mai_mici_decat_suma_mai_vechi_decat_zi(test, [5, 2355])==[[5, 10, "imbracaminte"]]#good assertion error
    #assert gaseste_cheltuieli_mai_mici_decat_suma_mai_vechi_decat_zi(test, [6, 2])==[[5, 10, "imbracaminte"]]#good assertion error
    assert gaseste_cheltuieli_mai_mici_decat_suma_mai_vechi_decat_zi(test, 1, 2355)==[]
    assert gaseste_cheltuieli_mai_mici_decat_suma_mai_vechi_decat_zi(test, 6, 2355)==[{"zi":5, "suma":10, "tip":"imbracaminte"}]
    assert gaseste_cheltuieli_mai_mici_decat_suma_mai_vechi_decat_zi(test, 31, 2355)==test
 
def test_elimina_cheltuieli_dupa_tip():
    test= [{"zi":12, "suma":123, "tip":"altele"},{"zi":30, "suma":478, "tip":"telefon"},{"zi":5, "suma":10, "tip":"imbracaminte"}]
    assert elimina_cheltuieli_dupa_tip([], "intretinere")==[]
    #assert  elimina_cheltuieli_dupa_tip([[12, 123, "altele"],[30, 478, "altele"],[5, 10, "imbracaminte"]], "altele")==[[12, 123, "altele"],[5, 10, "imbracaminte"]]#good assertion error
    #assert  elimina_cheltuieli_dupa_tip(test, "diverse")==[[30, 478, "telefon"],[5, 10, "imbracaminte"]]#good assertion error
    assert elimina_cheltuieli_dupa_tip(test, "intretinere")==test
    assert elimina_cheltuieli_dupa_tip(test, "altele")==[{"zi":30, "suma":478, "tip":"telefon"},{"zi":5, "suma":10, "tip":"imbracaminte"}]
    assert elimina_cheltuieli_dupa_tip([{"zi":12, "suma":123, "tip":"altele"},{"zi":30, "suma":478, "tip":"altele"},{"zi":5, "suma":10, "tip":"altele"}], "altele")==[]
    
def test_elimina_cheltuieli_mai_mici_decat_suma():
    test= [{"zi":12, "suma":123, "tip":"altele"},{"zi":30, "suma":478, "tip":"telefon"},{"zi":5, "suma":10, "tip":"imbracaminte"}]
    assert elimina_cheltuieli_mai_mici_decat_suma([], 215)==[]
    #assert elimina_cheltuieli_mai_mici_decat_suma(test, 300)==[30, 478, "telefon"]#good assertion error
    #assert elimina_cheltuieli_mai_mici_decat_suma(test, 1)==[]#good assertion error
    assert elimina_cheltuieli_mai_mici_decat_suma(test, 1000)==[]
    assert elimina_cheltuieli_mai_mici_decat_suma(test, 300)==[{"zi":30, "suma":478, "tip":"telefon"}]
    assert elimina_cheltuieli_mai_mici_decat_suma(test, 1)==test
   
def test_suma_totala_tip():
    test= [{"zi":12, "suma":123, "tip":"altele"},{"zi":30, "suma":478, "tip":"telefon"},{"zi":5, "suma":10, "tip":"imbracaminte"}]
    assert suma_totala_tip([], "altele")==0
    #assert suma_totala_tip(test, "altele")==123 #good assertion error
    #assert suma_totala_tip(test, "imbracaminte")==[] #good assertion error
    assert suma_totala_tip(test, "imbracaminte")==10
    assert suma_totala_tip(test, "altele")==123
    assert suma_totala_tip(test, "telefon")==478

def test_zile_suma_totala_max():
    test= [{"zi":3, "suma":100, "tip":"intretinere"},{"zi":12, "suma":123, "tip":"altele"},{"zi":30, "suma":478, "tip":"telefon"},{"zi":5, "suma":10, "tip":"imbracaminte"}]
    assert zile_suma_totala_max([])==[]
    #assert zile_suma_totala_max([])!=[] #good assertion error
    #assert zile_suma_totala_max(test)==[5] #good assertion
    assert zile_suma_totala_max(test)==[30]
    assert zile_suma_totala_max(test)!=[3]
    test=[{"zi":3, "suma":100, "tip":"intretinere"},{"zi":12, "suma":100, "tip":"altele"},{"zi":30, "suma":100, "tip":"telefon"},{"zi":5, "suma":10, "tip":"imbracaminte"}]
    assert zile_suma_totala_max(test)==[3,12,30]

def test_cheltuieli_sume_egale():
    test=[{"zi":3, "suma":100, "tip":"intretinere"},{"zi":12, "suma":123, "tip":"altele"},{"zi":30, "suma":478, "tip":"telefon"},{"zi":5, "suma":123, "tip":"imbracaminte"}]
    assert cheltuieli_sume_egale([], 10000)==[]
    #assert cheltuieli_sume_egale(test, 100)==[[5, 123, "imbracaminte"]] #good assertion error
    #assert cheltuieli_sume_egale(test, 102156)!=[] #good assertion error
    assert cheltuieli_sume_egale(test, 100)==[{"zi":3, "suma":100, "tip":"intretinere"}]
    assert cheltuieli_sume_egale(test, 123)==[{"zi":12, "suma":123, "tip":"altele"},{"zi":5, "suma":123, "tip":"imbracaminte"}]
    assert cheltuieli_sume_egale(test, "sdzhx")==[]
    
def test_sortare_dupa_tip():
    test=[{"zi":3, "suma":100, "tip":"intretinere"},{"zi":12, "suma":123, "tip":"altele"},{"zi":30, "suma":478, "tip":"telefon"},{"zi":5, "suma":10, "tip":"imbracaminte"}]
    assert sortare_dupa_tip([])==[]
    #assert sortare_dupa_tip(test)==test #good assertion error
    #assert sortare_dupa_tip(test)==[] #good assertion error
    assert sortare_dupa_tip(test)==[{"zi":12, "suma":123, "tip":"altele"},{"zi":5, "suma":10, "tip":"imbracaminte"},{"zi":3, "suma":100, "tip":"intretinere"},{"zi":30, "suma":478, "tip":"telefon"}]
    test=[{"zi":3, "suma":100, "tip":"intretinere"},{"zi":12, "suma":123, "tip":"altele"},{"zi":30, "suma":478, "tip":"intretinere"}]
    assert sortare_dupa_tip(test)==[{"zi":12, "suma":123, "tip":"altele"},{"zi":3, "suma":100, "tip":"intretinere"},{"zi":30, "suma":478, "tip":"intretinere"}]
    test=[{"zi":12, "suma":123, "tip":"altele"},{"zi":3, "suma":100, "tip":"intretinere"}]
    assert sortare_dupa_tip(test)==test

def test_sterge_cheltuieli_dupa_zi():
    test=[{"zi":30, "suma":100, "tip":"intretinere"},{"zi":12, "suma":123, "tip":"altele"},{"zi":30, "suma":478, "tip":"telefon"},{"zi":5, "suma":10, "tip":"imbracaminte"}]
    assert sterge_cheltuieli_dupa_zi([],25)==[]
    #assert sterge_cheltuieli_dupa_zi(test,12)!=[[30, 100, "intretinere"],[30, 478, "telefon"],[5, 10, "imbracaminte"]] #good assertion error
    #assert sterge_cheltuieli_dupa_zi(test,25)!=test #good assertion error
    assert sterge_cheltuieli_dupa_zi(test,25)==test
    assert sterge_cheltuieli_dupa_zi(test,30)==[{"zi":12, "suma":123, "tip":"altele"},{"zi":5, "suma":10, "tip":"imbracaminte"}]
    test=[{"zi":3, "suma":100, "tip":"intretinere"},{"zi":3, "suma":123, "tip":"altele"},{"zi":3, "suma":478, "tip":"telefon"},{"zi":3, "suma":10, "tip":"imbracaminte"}]
    assert sterge_cheltuieli_dupa_zi(test,3)==[]

def test_sterge_cheltuieli_din_perioada():
    test=[{"zi":30, "suma":100, "tip":"intretinere"},{"zi":12, "suma":123, "tip":"altele"},{"zi":30, "suma":478, "tip":"telefon"},{"zi":5, "suma":10, "tip":"imbracaminte"}]
    assert sterge_cheltuieli_din_perioada([],25, 30)==[]
    #assert sterge_cheltuieli_din_perioada(test,20, 30)==test #good assertion error
    #assert sterge_cheltuieli_din_perioada(test,12, 29)==test #good assertion error
    assert sterge_cheltuieli_din_perioada(test,21, 29)==test
    assert sterge_cheltuieli_din_perioada(test,3, 15)==[{"zi":30, "suma":100, "tip":"intretinere"},{"zi":30, "suma":478, "tip":"telefon"}]
    assert sterge_cheltuieli_din_perioada(test,1, 9)==[{"zi":30, "suma":100, "tip":"intretinere"},{"zi":12, "suma":123, "tip":"altele"},{"zi":30, "suma":478, "tip":"telefon"}]

def test_undo():
    test=[{"zi":3, "suma":100, "tip":"intretinere"},{"zi":12, "suma":123, "tip":"altele"},{"zi":30, "suma":478, "tip":"telefon"},{"zi":5, "suma":10, "tip":"imbracaminte"}]
    assert undo([],["citit"])==[]
    assert undo(test, ["citit", "citit", "citit","citit"])==test[0:3]
    test=[{"zi":3, "suma":100, "tip":"intretinere"},{"zi":12, "suma":123, "tip":"altele"},{"zi":30, "suma":478, "tip":"telefon"},{"zi":3, "suma":10, "tip":"intretinere"}]
    assert undo(test, ["citit", "citit", "citit","actualizat"])==test[0:3]
    