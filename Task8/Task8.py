from math import ceil
#Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками 
#(то есть разломить шоколадку на два прямоугольника)..

def chocolateBar():
    n = int(input())
    k = int(input())
    m = int(input())
   

    if m<k*m and int( (m%k==0) or (m%n==0)):
        print("yes")
    else:
        print("no")


chocolateBar()