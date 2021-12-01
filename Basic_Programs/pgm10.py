# pgm10) Python Program to check if a given number is Fibonacci number.

num = int(input("Enter a number : "))

i, j,  = 0, 1
flag = False

for r in range(num + 1):
    if num == 0:
        flag = True
        break
    add = i + j
    i = j
    j = add
    if add == num:
        flag = True


if flag == True:
    print("In fib series")
else:
    print("Not in fib series")
