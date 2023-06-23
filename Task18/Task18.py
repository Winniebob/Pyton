# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

def NumberCloseX () :
    N = int(input('Введите количество элементов в массиве: '))
    Numbers_Array = input('Введите элементы массива через пробел:').split()
    Array_n = list(map(int,Numbers_Array))
    if len(Array_n) != N or N ==0:
            print('Заданное количество элементов не соотвествует заданному в массиве')
    else:
            X = int(input('Введите число с которым необходимо сравнивать элементы списка:'))
            minNumbers = X - Array_n[0]
            indexArray = 0
            for i in range(1,N):
                    count = X - Array_n[i]
                    if count < X and count >0:
                        minNumbers = count
                        indexArray = i
            print(f'Число {Array_n[indexArray]} в списке наиболее бликзо по величение к числу {X}')

NumberCloseX()
                    
