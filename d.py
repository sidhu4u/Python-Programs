# b = input("String :")
# s = ''
# for i in range(1, len(b)+1):
#     s += b[len(b)-i]
# if s == b:
#     print("palindrome")
# else:
#     print("Not palindrome")

# # function which return reverse of a string

def isPalindrome(s):
    s == s[::-2]
    print(s)


# Driver code
s = "malayalam1"
ans = isPalindrome(s)

if ans:
    print(ans)
else:
    print("No")
