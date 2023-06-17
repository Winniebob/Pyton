from math import ceil

def SumNumbers():
    numbers = int(input())

    numbers3 = int(numbers%10)
    numbers2 = int(numbers/10%10)
    numbers1 = int(numbers/100)

  
    print(numbers1+numbers2+numbers3)


SumNumbers()