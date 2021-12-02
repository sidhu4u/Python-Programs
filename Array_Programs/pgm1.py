# 1.Python Program to find sum of array

try:
    array_size = int(input("Enter size of an Array : "))
    if array_size <= 0:
        print("Array size must have Positive value.")
    else:
        array_ele = []
        sum = 0
        for ele in range(array_size):
            array_ele.append(int(input(f"Element {ele} : ")))
            sum += array_ele[ele]

        print("Sum of Array elements : ", sum)

except ValueError:
    print("Invalid Value")
