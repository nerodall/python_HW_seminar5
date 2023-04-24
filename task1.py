# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8


def power_def(number: int, power_number: int) -> int:
    if power_number == 0:
        return 1
    return number * power_def(number,power_number-1)


number = int(input('Введите число которое нужно возвести в степень: '))
power_number = int(input('Введите степень: '))
result = power_def(number, power_number)

print(f'{number} в степени {power_number} = {result}')

