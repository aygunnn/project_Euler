
"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def diffrence():
    sayılar_kareler_toplamı = 0
    sayılar_toplamı = 0

    for i in range(101):
        sayılar_kareler_toplamı = i**2 + sayılar_kareler_toplamı
        sayılar_toplamı += i

    print(sayılar_toplamı**2)
    print(sayılar_kareler_toplamı)
    print("fark =",sayılar_toplamı**2 - sayılar_kareler_toplamı)

diffrence()


