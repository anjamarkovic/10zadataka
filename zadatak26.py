""" Napisati metod boolean jeProst(int n) koji za dati broj n provjerava da li je prost, i
ako jeste, vraća true, a ako nije, vraća false. """
def je_prost(n) :
    if n==1 :
        return False
    for i in range (2,n) :
        if(n%i==0) :
            return False
    return True
print(je_prost(19))
