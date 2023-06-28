
import math

def trianguler_number(div):

    step = 1

    while True :

        num = step*(step+1)//2
        divisors = 1

        for i in range(1,int(math.sqrt(num)+1)):
            if num % i == 0:
                divisors += 1

        if divisors*2 > div:
            print(num)
            break

        step += 1


trianguler_number(500)
