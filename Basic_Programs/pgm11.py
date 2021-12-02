
# pgm11) Program to print
# - ASCII Value of a character
# - Range of ASCII charater and its values

print("1. ASCII Value of a character\n2. Range of ASCII charater and its values")

try:
    choice = int(input("Enter Choice :"))

    if choice == 1:
        ch = input("Enter Character : ")
        print(f"ASCII character of '{ch}' = ", ord(ch))
    elif choice == 2:
        r = int(input("Enter the Range : "))
        for i in range(r):
            print(f"'{chr(i)}'={ord(chr(i))}", end=" ,")
    else:
        print("Wrong Choice")
except ValueError:
    print("Invalid Value")
