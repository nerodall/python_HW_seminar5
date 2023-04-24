# # Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций
#  допускаются только +1 и -1. Также нельзя использовать циклы.

# # *Пример:*

# # 2 2
# #     4


def sum_number(first_number, second_number):
    if second_number - 1 == 0:
        return first_number+1
    return sum_number(first_number+1, second_number-1)


first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
print(f'сумма чисел = {sum_number(first_number,second_number)}')