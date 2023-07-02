#Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def power(number, degree):
    if (degree == 1):
        return (number)
    if (degree != 1):
        return (number * power(number, degree - 1))
number = int(input("Введите число A: "))
degree = int(input("Введите его степень B: "))
print("Результат возведения в степень равен:", power(number, degree))