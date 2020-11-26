#урок 4 задание 1_

from sys import argv

name, time, salary, bonus = argv
try:
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    res = time * salary + bonus
    print(f'заработная плата сотрудника  {res}')
except ValueError:
    print('Not a number')

#урок 4 задание 2_1

my_list = [46, 35, 98, 1, 146, 93, 7, 18]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')

# урок 4 задание 3_1
print(f'Числа от 20 до 240 кратные 20 или 21 - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')

#урок 4 задание 4_1

my_list = [1, 4, 4, 2, 3, 2, 8, 10, 8, 5]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_new_list)

#урок 4 задание 5_1

from functools import reduce
def my_func(el_p, el):
    return el_p * el
print(f'Список четных значений {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат перемножения всех элементов списка {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')

#урок 4 задание 6_1

# from itertools import count
# for el in count(int(input('Введите стартовое число '))):
#     print(el) #беконечный цикл
# from itertools import cycle
# my_list = [True, 'qwerty', 123, None, [1, 2, 3]]
# for el in cycle(my_list):
#     print(el) # беконечный цикл!

#урок 4 задание 7_1

from itertools import count
from math import factorial

def fibo_gen():
    for el in count(1):
        yield factorial(el)

gen = fibo_gen()
x = 0
for i in gen:
    if x < 15:
        print(i)
        x += 1
    else:
        break
