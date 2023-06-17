from math import ceil
#Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
#Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
#а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?


def Сranes():
    AllCranes = int(input())
    Peta = int(AllCranes/6)
    SergeiCranes = int(AllCranes/6)
    Katya = int(AllCranes/6*4)
    print (Peta,Katya,SergeiCranes)

    
Сranes()  
