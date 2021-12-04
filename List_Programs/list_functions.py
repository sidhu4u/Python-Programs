from math import ceil


def list_ele():
    list = []
    print("Enter the elements into List...")
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
    print("Enter the elements into List...")
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


def pos_neg_list(list):
    p = []
    n = []
    for i in list:
        if i > 0:
            p.append(i)
        else:
            n.append(i)
    return p, n


def rem_multiple_ele(list, n, pos):
    if pos == 'e':
        while n != 0:
            list.pop()
            n -= 1
        return list
    elif pos == 'm':
        while n != 0:
            d = ceil(len(list)/2)
            list.pop(d - 1)  # remove(d)
            n -= 1
        return list
    else:
        while n != 0:
            list.pop(n - 1)  # remove(n)
            n -= 1
        return list


def remove_dup_list(list):
    d = []
    for x in list:
        if x not in d:
            d.append(x)
    return d


def break_list(list, n):
    br_li = []
    while n != 0:
        br_li.append(list.pop(0))
        n -= 1
    return [br_li, list]
