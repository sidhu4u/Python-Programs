# pgm8) Python program to print
# - To check given number is Prime or Not
# - all Prime numbers in a given Interval
from math import ceil, floor

try:
    print("1. To Check given number Prime or Not\n2. To generate Range of Prime numbers")
    choice = int(input("Enter your choice : "))

    if choice == 1:
        interval = int(input("Enter the Number : "))
        flag = True
        for i in range(2, floor(interval / 2) + 1):
            d = ceil(interval % i)
            if d == 0:
                flag = False
        if flag == True:
            print("Prime Number")
        else:
            print("Not a prime Number")

    elif choice == 2:
        interval = int(input("Interval : "))
        for i in range(2, interval + 1):
            flag = True
            for j in range(2, floor(i / 2) + 1):
                d = ceil(i % j)
                if d == 0:
                    flag = False
            if flag == True:
                print(i, end=", ")

    else:
        print("Wrong Choice!")

except ValueError:
    print("Invalid Value.")
