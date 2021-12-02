# pgm9) Python Program for n-th Fibonacci number

limit = int(input("Enter Range : "))

# Method 1
print("Method 1")
i, j = 0, 1
print(i, j, end=" ")
for r in range(2, limit):
    add = i + j
    print(add, end=" ")
    i = j
    j = add

print("\n--------------")

# Method 2
print("Method 2")
i, j = 0, 1
for r1 in range(limit):
    print(i, end=" ")
    add = i + j
    i = j
    j = add
