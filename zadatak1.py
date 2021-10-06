"""Napisati metod double promjena(double x, double a) koji vraća broj a*x, ako je
x nenegativan i a/x, ako je x negativan."""


def da_li_je_broj_negativan(a, x) :
    
    if x>=0 :
        return a*x
    else:
        return a/x
print(da_li_je_broj_negativan(4.9 , 4.5))