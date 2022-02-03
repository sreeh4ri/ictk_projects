# Day 1 :: Thursday, 20-January-2022
# Program-2, name :: Maximum of 2 numbers

def my_max(a:float, b:float, use ='Teri'):
    if use == 'func':
        return max(a, b)
    else:
        # Terinary Operator
        return (a if a>=b else b)

num1 = float(input('Enter 1st number :: '))
num2 = float(input('Enter 2nd number :: '))
print(f'Maximuum of {num1} and {num2} is {my_max(num1, num2)}')

