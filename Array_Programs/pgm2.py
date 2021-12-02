# 2.Python Program to find largest element in an array

try:
    array_size = int(input("Enter size of an Array : "))
    if array_size <= 0:
        print("Array size must have Positive value.")
    else:
        array_ele = []
        maximum = 0
        for ele in range(array_size):
            array_ele.append(int(input(f"Element {ele} : ")))
            if maximum < array_ele[ele]:
                maximum = array_ele[ele]

        print("Largest in Array : ", maximum)

except ValueError:
    print("Invalid Value")
