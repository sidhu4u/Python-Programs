# 1.	Python program to find length of list
# 2.	Python program to check if element exists in list


from list_functions import list_len, ele_exist_list, sum_ele

print("1.Python program to find length of list\n\
2.Python program to check if element exists in list\n\
3.Python program to find sum of elements in list")


list = []
try:
    choice = int(input("Choice : "))
    if choice == 1:
        # 1.Python program to find length of list
        while True:
            n = input("Element(Press 'n' to Quit) = ")
            if n == 'N' or n == 'n':
                break
            list.append(n)
        print("Given List = ", list)

        print("Length of given List = ", list_len(list))

    elif choice == 2:
        # 2.Python program to check if element exists in list
        while True:
            n = input("Element(Press 'n' to Quit) = ")
            if n == 'N' or n == 'n':
                break
            list.append(n)
        print("Given List = ", list)
        ele = input("Element = ")

        b = ele_exist_list(list, ele)
        if b:
            print(f"Element Present {b[1]} times at Position {b[0]}")
        else:
            print("Element Not Present")

    elif choice == 3:
        # 3.Python program to find sum of elements in list
        sum = 0
        n = 0
        while True:
            try:
                n = int(input("Element(Press '0' to Quit) = "))
            except ValueError:
                print("please enter number to conti...")
            else:
                if n == 0:
                    break
                list.append(n)

        print("\nGiven List = ", list)
        print("sum = ", sum_ele(list))

    else:
        print("Wrong Choice!")

except ValueError:
    print("Invalid Value.")
