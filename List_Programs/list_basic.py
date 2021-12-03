# 1. Python program to find length of list
# 2. Python program to check if element exists in list
# 3. Python program to find sum of elements in list
# 4. Python program to Multiply all numbers in the list
# 5. Python program to print even and odd numbers in a list


from list_functions import list_ele, number_list, list_len, ele_exist_list, sum_ele, mul_ele, even_odd_list

print("1.Python program to find length of list\n\
2.Python program to check if element exists in list\n\
3.Python program to find sum of elements in list\n\
4.Python program to Multiply all numbers in the list\n\
5.Python program to print even and odd numbers in a list")


list = []
try:
    choice = int(input("Choice : "))
    if choice == 1:
        # 1.Python program to find length of list
        print("Length of given List = ", list_len(list_ele()))

    elif choice == 2:
        # 2.Python program to check if element exists in list
        list = list_ele()
        ele = input("Search element = ")

        b = ele_exist_list(list, ele)
        if b:
            print(f"Element Present {b[1]} times at Position {b[0]}")
        else:
            print("Element Not Present")

    elif choice == 3:
        # 3.Python program to find sum of elements in list
        print("sum = ", sum_ele(number_list()))

    elif choice == 4:
        # 4.Python program to Multiply all numbers in the list
        print("Multiplication = ", mul_ele(number_list()))

    elif choice == 5:
        # 5.Python program to print even and odd numbers in a list
        res = even_odd_list(number_list())
        print("Even numbers in list = ", res[0])
        print("Odd numbers in list = ", res[1])

    else:
        print("Wrong Choice!")

except ValueError:
    print("Invalid Value.")
