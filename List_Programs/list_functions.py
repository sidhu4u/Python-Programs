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
