# pgm10) Python Program to
# - check if a given number is in Fibonacci series.
# - Check the index position in Fibonacci series.

print("1. check if a given number is in Fibonacci series\n2. find the index position in Fibonacci series")


i, j,  = 0, 1
flag = False
count = 1
index, index1 = 0, 1
try:
    choice = int(input("Enter your choice : "))
    if choice == 1:
        num = int(input("Enter a number : "))
        for r in range(num + 1):
            if num == 0:
                flag = True
                break
            count = i + j
            i = j
            j = count
            if count == num:
                flag = True
                break

        if flag == True:
            print("NUmber is in fib series")
        else:
            print("Not in fib series")

    elif choice == 2:
        num = int(input("Enter a number : "))
        if num < 1:
            index += 1
            print("Index = ", index)

        else:
            while count < num:
                count = i + j
                index1 += 1
                i = j
                j = count
            print("Index = ", index1 + 1)

    else:
        print("Wrong Choice")


except ValueError:
    print("Invalid Value")
