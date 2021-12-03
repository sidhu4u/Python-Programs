
def list_ele():
    list = []
    while True:
        n = input("Element(Press 'n' to Quit) = ")
        if n == 'N' or n == 'n':
            break
        list.append(n)
    print("Given List = ", list)
    return list


def number_list():
    n = 0
    list = []
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
    return list


def list_len(list):
    return len(list)


def ele_exist_list(list, ele):
    pos = []
    cnt = 0
    for e in range(len(list)):
        if list[e] == ele:
            pos.append(e+1)
            cnt += 1
    return pos, cnt


def sum_ele(list):
    sum = 0
    for x in list:
        sum += int(x)
    return sum


def mul_ele(list):
    mul = 1
    for x in list:
        mul *= int(x)
    return mul


def even_odd_list(list):
    e = []
    o = []
    for i in list:
        if i % 2 == 0:
            e.append(i)
        else:
            o.append(i)
    return e, o
