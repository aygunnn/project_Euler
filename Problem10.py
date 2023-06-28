

def prime_check(x):

    control = True
    for i in range(2, int((x)**0.5 +1)):
        if x % i == 0:
            control = False
            break
    return control


def summ_primes(num):

    summ = 0
    for i in range(2,num):
        if prime_check(i):
            summ += i
    return summ

print(summ_primes(2000000))