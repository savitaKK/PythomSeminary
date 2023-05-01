# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1
from random import randint
count_elements_array=int(input(" Введите кол-во элементов в массиве:  "))
number_to_search_for=int(input('Введите число для поиска:  '))

random_array = [randint(0, count_elements_array) for i in range(count_elements_array)]
print(random_array)
count = 0
for i in range(count_elements_array):
    if random_array[i] == number_to_search_for:
        count += 1
print(f'Число {number_to_search_for} встречается в списке А {count} раз.')