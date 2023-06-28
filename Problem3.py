
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""


def prime(n1):
    primes=[]

    for i in range(2,n1//5):
        if n1%i == 0:
            control = False
            for j in range(2,i):
                if i%j == 0:
                    control = True
            if not control :
                primes.append(i)
    
    print(primes)


prime(5)


