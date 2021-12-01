# pgm9) Python Program for n-th Fibonacci number

limit = int(input("Enter Range : "))
i, j = 0, 1
print(i, j, end=" ")
for r in range(limit):
    add = i + j
    print(add, end=" ")
    i = j
    j = add
