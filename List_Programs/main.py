# 1. Python program to find length of list
# 2. Python program to check if element exists in list
# 3. Python program to find sum of elements in list
# 4. Python program to Multiply all numbers in the list
# 5. Python program to print even and odd numbers in a list
# 6. Python program to print positive and negative numbers in a list
# 7. Remove multiple elements from a list in Python
# 8. Python program to print duplicates from a list of integers
# 9. Break a list into chunks of size N in
# 10. Generating Number-Table by giving starting and ending values.

import questions
from list_functions import list_ele, number_list, list_len, ele_exist_list, sum_ele, mul_ele, even_odd_list, pos_neg_list, rem_multiple_ele, remove_dup_list, break_list, number_table

questions
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
        if b[1] != 0:
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

    elif choice == 6:
        # 6.Python program to print positive and negative numbers in a list
        res = pos_neg_list(number_list())
        print("Positive numbers in list = ", res[0])
        print("Negative numbers in list = ", res[1])

    elif choice == 7:
        # 7.Remove multiple elements from a list in Python
        list = list_ele()
        n = int(input("How many ele tobe removed (number only) : "))
        pos = input(
            "Enter position Front(F) or Middle(M) or Rear-end(E) : ").lower()
        f_r = {
            'f': "Front",
            'm': "Middle",
            'e': "Rear-end"
        }
        print(f"After removing elements at the {f_r[pos]} of list :\n",
              rem_multiple_ele(list, n, pos))

    elif choice == 8:
        # 8. Python program to print duplicates from a list of integers
        print("Removing duplicates = ", remove_dup_list(list_ele()))

    elif choice == 9:
        # 9. Break a list into chunks of size N in Python
        list = list_ele()
        n = int(input("size of first list tobe break (number only) : "))
        print("After Breaking lists = ", break_list(list, n))

    elif choice == 10:
        # 10. Generating Number-Table by giving starting and ending values.
        print("Generating the 'Number-table' by given starting and ending value")
        Range1 = abs(int(input("Enter the starting(lower bound) number : ")))
        Range2 = abs(int(input("Enter the ending(upper bound) number : ")))
        for table in number_table(Range1, Range2):
            print(table)

    else:
        print("Wrong Choice!")

except ValueError:
    print("Invalid Value.")
