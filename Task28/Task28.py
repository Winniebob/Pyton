#Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum(numberA, numberB):
    if numberA==0:
        return numberB;
    else :
        return sum(numberA-1, numberB+1 )
numberA = int(input("Введите число A: "))
numberB = int(input("Введите число B: "))
print("Результат сложения равен равен:", sum(numberA, numberB))