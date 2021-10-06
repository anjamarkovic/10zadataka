"""Napisati metod int zbirIzIntervala(int a, int b) koji vraća zbir svih cijelih
brojeva iz intervala [a,b]"""

def zbir_intervala (a,b) :
    
    s=0
    for i in range(a,b+1) :
        s=s+i

    print(s) 
zbir_intervala(1,5)
