# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются 
# в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.
# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)
# Output: 11 6
# 6 12

import random

print('Program to find the same elements in lists.')

n = int(input('Input the elements quantity of the first set: '))
m = int(input('Input the elements quantity of the second set: '))

def create_list(x):

    list = []

    for i in range(x):
        random_number = random.randint(1, 20)
        list.append(random_number)

    return list

list1 = create_list(n)  
list2 = create_list(m)

print(list1)
print(list2)

set1 = set(list1)
set2 = set(list2)
same_elements = list(set1.intersection(set2))
same_elements.sort()

if same_elements == []:
    print('There are no any same elements in two sets')
else:
    print(f'The same elements in both sets are: {same_elements}')