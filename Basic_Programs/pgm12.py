# pgm12) Python Program for Sum of
# - n natural numbers
# - squares of n natural numbers
# - cube of n natural numbers

try:
    num = int(input("Enter Number : "))
    sum, square, cube = 0, 0, 0
    for n in range(num):
        print(n, end="+")
        if n+1 == num:
            print(num)
        sum += n
        square += (n ** 2)
        cube += (n ** 3)
    sum += num
    square += (num ** 2)
    cube += (num ** 3)

    print("Sum of Numbers = ", sum)
    print("Sum of Square = ", square)
    print("Sum of cube = ", cube)

except ValueError:
    print("Invalid Value!")
