from sympy import randprime


def generate_prime():
    start =2**255
    end= 2**256

    prime= randprime(start,end)
    return prime 

