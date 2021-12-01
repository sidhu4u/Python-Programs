# pgm6. Python Program to check Armstrong Number

from math import floor


def check_armstrong():
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


def geretate_aramstrong():
    limit = int(input("Enter the Limit : "))
    print("Armstrong Numbers\n------------------")

    for l in range(limit):
        rev_num = l
        sum = 0
        while l != 0:
            rem = floor(l % 10)
            sum += (rem ** 3)
            l = floor(l / 10)
        if rev_num == sum:
            print(sum)


print("1. To check the given number is Armstrong or Not.(press- 1)")
print("2. To generate Armstrong numbers to the given limit. (press- 2")
choice = int(input("Choice : "))
if choice == 1:
    check_armstrong()
else:
    geretate_aramstrong()
