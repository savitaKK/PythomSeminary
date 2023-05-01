# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#  *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint
count_elements_array=int(input(" Введите кол-во элементов в массиве:  "))
number_x=int(input('Введите число для поиска ближайшего элемента:  '))

random_array = [randint(0, count_elements_array) for i in range(count_elements_array)]
print(random_array)
pos=[abs(random_array[i]-number_x) for i in range(len(random_array))]
print(random_array[pos.index(min(pos))])

