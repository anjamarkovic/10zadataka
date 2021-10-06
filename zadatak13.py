"""Napisati metod long fakt(long n) koji vraća n! (n! = 1*2*...*n). """
def long_fakt(n) :
    if n==0 :
        return 1
    else :
        return n * long_fakt(n-1)
print(long_fakt(3))       