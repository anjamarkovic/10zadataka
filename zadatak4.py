"""Napisati metod boolean pripadaIntervalu (int a, int b, int x) koji vraća
true ako broj x pripada intervalu [a, b] i vraća false ako ne pripada."""
def pripada_intervalu(a,b,x) :
    if x>=a and x<=b :
        return True 
    else:
        return False
print(pripada_intervalu(1,4,6))