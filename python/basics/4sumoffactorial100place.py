# Day 3 :: Thursday, 03-February-2022
# Program-4, name :: To find the number at which factorail sum stabilizes for 1s, 10th and 100th place
from math import factorial


stableplace = 10
n=1
stabilizer_numbers = []
while stableplace<10000:
    if(factorial(n)%stableplace == 0):
        stabilizer_numbers.append(n)
        stableplace*=10
    n+=1
print(f"3 numbers at which 1s, 10th and 100th place stabilizes = {stabilizer_numbers}")
