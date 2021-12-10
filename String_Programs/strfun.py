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


def count_duplicate(ss):
    ss = ss.lower()
    ss = remove_punctuations(ss)
    ss = ss.split(" ")
    s = []
    cnt = []
    for i in ss:
        if i not in s:
            s.append(i)
    for i in s:
        cnt.append(ss.count(i))
    return s, cnt
