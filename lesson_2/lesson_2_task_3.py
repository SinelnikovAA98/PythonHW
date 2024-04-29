from math import ceil

def square(n):
    mult = n * n
    if mult !=0:
        print(f"Площадь квадрата = {n} * {n} = {ceil(mult)}")
square(5.7)