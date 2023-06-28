"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""
def is_divisible(num):
    for i in range(1,21):
        if num % i != 0:
            return False
    return True


number = 1

while True :

    if is_divisible(number):
        break   

    number += 1
    
print(number)




