from math import ceil


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
