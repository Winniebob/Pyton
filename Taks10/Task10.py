from math import ceil

#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернут

def ReshkaOrel ():
     n = int(input())
     orel = 0
     reshka = 0
     for i in range(n):
        x = int(input())
        if(x == 0):
            orel+=1
        else:
            reshka+=1
     if reshka>orel:
        print(orel)
     else:
         print(reshka)

ReshkaOrel ()