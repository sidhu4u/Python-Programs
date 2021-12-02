# 3.Python Program for array rotation

try:
    array_size = int(input("Enter size of an Array : "))
    if array_size <= 0:
        print("Array size must have Positive value.")
    else:
        array_ele = []
        for ele in range(array_size):
            array_ele.append(int(input(f"Element {ele} : ")))
        print("Given Array : ", array_ele)

        steps = st = int(input("Enter the steps to ratate : "))
        pos = ["Right", "Left"]
        if steps > 0:
            while steps > 0:
                p = array_ele.pop(0)
                a = array_ele.append(p)
                steps -= 1
                pos1 = pos[0]
        else:
            while steps < 0:
                p = array_ele.pop()
                a = array_ele.insert(0, p)
                steps += 1
                pos1 = pos[1]

        print(f"Array after Rotation {st} steps to {pos1} : ", array_ele)

except ValueError:
    print("Invalid Value")
