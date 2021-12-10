from math import ceil
import string


def reverse(s):
    s = s[::-1]
    return s


def charremove(s, c):
    s1 = ''
    for i in range(len(s)):
        if s[i] == c:
            continue
        s1 += s[i]
    return s1


def substring(s, substring):
    return substring in s, s.count(substring)


def padding(s, val, sym):
    l = ceil(val/2)
    r = val - l
    return f"{sym*l}{s}{sym*r}"


def remove_punctuations(s):
    j = 0
    sub = ''
    for i in s:
        if i not in string.punctuation:
            sub += i
            j += 1
    return sub

# def remove_duplicate(s):
#     uni = []
#     for i in s.split(" "):
#         if i not in uni:  # in (uni.lower() and uni.upper()):
#             uni.append(i)  # += i + " "
#     uni = ' '.join(uni)
#     print(' '.join(uni))
#     # unique = ''
#     # for i in uni.split(" "):
#     #     if i not in i.capitalize() and i not in unique:
#     #         unique += i + " "
#     # print(unique)
#     return uni
