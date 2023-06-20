 #Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

from math import ceil

def Degrees():
    numbers = int(input())
    i = 0
    while 2**i <= numbers:
        print(2 **i)
        i+=1
Degrees()