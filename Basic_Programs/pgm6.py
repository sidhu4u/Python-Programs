# pgm6. Python Program to check Armstrong Number
from math import floor
num = int(input("Number please : "))
rev_num = num
sum = 0

while num != 0:
    rem = floor(num % 10)
    sum += (rem ** 3)
    num = floor(num / 10)

if rev_num == sum:
    print(f'{rev_num} is an Armstrong number.')
else:
    print(f'{rev_num} is not an Armstrong number.')
