# Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, 
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть 
# ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают разной 
# урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на 
# i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать 
# за один заход собирающий модуль, находясь перед некоторым кустом заданной во 
# входном файле грядки.
# Input: 4
# (значения сгенерированы случайным образом
# 4 2 3 1 )
# Output: 9

import random

print('Program to count the max berries quantity that could be gathered by module per 1 time')

list = []

while True:
    try:
        n = int(input('Input the shrub quantity: ')) # количество кустов
        if n > 3:
            for i in range(0, n):
                random_number = round(random.randint(0, 10))
                list.append(random_number)
            print(list)
            break
    except:
        print('Wrong input. Quantity should be more 3 to compare')

max_sum = list[0] + list[1] + list[2] 

for i in range(n - 1):
    p = list.pop()
    list.insert(0, p)
    sum = list[0] + list[1] + list[2]
    if sum > max_sum:
        max_sum = sum
    
print(f'The max berries quantity that could be gathered by module per 1 time: {max_sum}') 