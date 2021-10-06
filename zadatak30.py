"""Prirodan broj n je Armstrongov ako je jednak zbiru kubova svojih cifara. Npr. 371 je
Armstrongov. Napisati metod boolean isArmstrong(int n) koji
za dati broj"""
def broj_cifara(n) :
    """funkcija izracunava koliko cifara ima broj n"""
    broj=0
    while True :
        broj=broj + 1
        n=n//10
        if n==0 :
            break
    return broj

def zbir_nekog_stepena_cifara(n,k) :
    """funkcija stepenuje cifre broja n na k-ti stepen i vraca njihov zbir"""

    zbir=0
    while True :
        zbir=zbir + (n%10) ** k
        n=n//10
        if n==0 :
            break
    return zbir

def is_Amstrong(n):
    if zbir_nekog_stepena_cifara(n,broj_cifara(n)) == n:
        return True
    else:
        return False
print(is_Amstrong(371))