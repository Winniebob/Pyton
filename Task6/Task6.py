from math import ceil
#Вы пользуетесь общественным транспортом?
#Вероятно, вы расплачивались за проезд и получали билет с номером. 
#Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех..
#Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

def LuckyTicket():
    Ticket = int(input())
    NumberOne = int(Ticket/100000)
    NumberSecond = int(Ticket/10000%10)
    NumberThree = int(Ticket/1000%10)
    LeftNumbers = int(NumberOne+NumberSecond+NumberThree)
    NumberFour = int(Ticket/100%10)
    NumberFive = int(Ticket/10%10)
    NumberSix = int(Ticket%10)
    RightNumber = int(NumberFour+NumberFive+NumberSix)
    if(LeftNumbers==RightNumber):
        print("yes")
    else:
        print("no")


LuckyTicket()