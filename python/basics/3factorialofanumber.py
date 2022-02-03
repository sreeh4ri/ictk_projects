# Day 2 :: Monday, 24-January-2022
# Program-3, name :: Factorial of a number

from math import factorial


def factori(number:int, use='teri'):
    if use == 'builtin':
        return factorial(number)
    else:
        return 1 if (number ==0 or number ==1) else number * factori(number-1)

number = int(input('Enter the number :: '))
print(f'Factorial of {number} is {0 if (number <0) else factori(number)}')
print(f'Factorial of {number} is {factori(number, "builtin")}')