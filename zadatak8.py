"""Napisati metod int zbirCifara(int n) koji vraća zbir cifara broja n"""
def zbir_cifara(n) :
    if n<10 :
        return n
    else:
        return n%10 + zbir_cifara(n//10)
print(zbir_cifara(123456))