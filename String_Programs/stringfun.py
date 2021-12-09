from strfun import reverse, charremove, substring
# def reverse(s):
#     s = s[::-1]
#     return s


# def charremove(s, c):
#     s1 = ''
#     for i in range(len(s)):
#         if s[i] == c:
#             continue
#         s1 += s[i]
#     return s1


# def substring(s, substring):
#     return substring in s, s.count(substring)


def pgm1():
    s = input("Enter String :")
    if s == reverse(s):
        return f"String '{s}' is Palindrome."
    else:
        return f"String '{s}' is Not Palindrome."


def pgm2():
    s = input("Enter String :")
    return f'Reverse String = "{reverse(s)}"'


def pgm3():
    s = input("Enter String :")
    c = input("Enter removing Character : ")
    return f"after removing character '{c}' = '{charremove(s, c)}'"


def pgm4():
    s = input("Enter String :")
    subs = input("Enter Substring : ")
    sub = substring(s, subs)
    if sub[0]:
        return f"substring '{subs}' present {sub[1]} times in Given string."


def invalid():
    return "Invalid Choice!"


question_choice = {
    '1': pgm1,
    '2': pgm2,
    '3': pgm3,
    '4': pgm4


}


def choices(choice):
    return question_choice.get(choice, invalid)()
