# pgm3. Python Program for factorial of a number

num = int(input("Enter the number : "))
n = num
res = 1
while n > 1:
    if n == 0:
        res = '1'
    else:
        res *= n
        n -= 1

print(f'Factorial of {num}! = {res}')
