# pgm2. Maximum of two numbers in Python

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

# using mutiple if statements
if num1 > num2:
    print(f'num1={num1} is greater than num2={num2}.')
elif num1 < num2:
    print(f'num1={num1} is smaller than num2={num2}.')
else:
    print(f'num1={num1} is equal to num2={num2}.')

# using Ternary operator statement
result = num1 if num1 > num2 else num2
print(f'Maximun number = {result}')
