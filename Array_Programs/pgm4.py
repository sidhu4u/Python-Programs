# 4.Python Program to Split the array and add the first part to the end
from math import floor

try:
    array_size = int(input("Enter size of an Array : "))
    if array_size <= 0:
        print("Array size must have Positive value.")
    else:
        array_ele = []
        split_Array = []
        for ele in range(array_size):
            array_ele.append(int(input(f"Element {ele} : ")))
        print("Given Array : ", array_ele)

        for s in range(floor(len(array_ele)/2)):
            split_Array.append(array_ele[s])
        print("split Array = ", split_Array)
        array_ele.extend(split_Array)
        print("Splited Array added end of original array:\n", array_ele)

except ValueError:
    print("Invalid Value")
