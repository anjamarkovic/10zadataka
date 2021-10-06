"""Napisati metod double stepen(double x, int n) koji vraća xn
. Ne koristiti metod
pow iz klase Math. """
def stepen(x,n) :
    if n==0 :
        return 1
    else:
            return x * stepen(x , n-1)
print(stepen(2,3))