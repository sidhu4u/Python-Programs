# pgm7) Python Program to find area of a different shapes.

from area import go


while True:
    print("1. Area of Circle\n2. Area of Rectangle\n3. Area of Triangle\n4. Area of Square\n5. Area of Rhombus")
    choice = input("Choice : ")
    print(go(choice))
    repeat = input("Do you want to continue... (press 'Y' Or 'N')").lower()
    if repeat == 'n':
        break
