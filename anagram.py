# str1=str(input("enter string1: "))
# str2=str(input("enter string2: "))
# l1=len(str1)
# l2=len(str2)
# m1=0
# m2=0

# for i in str1:
#   if i in str2:
#     m1=m1+1

# for i in str2:
#   if i in str1:
#     m2=m2+1

# if m1==l2 and m2==l1 :
#   print("it is anagram")


# Get input strings
str1 = input("Enter string1: ")
str2 = input("Enter string2: ")

# Check if the two strings are anagrams by sorting
if sorted(str1) == sorted(str2):
    print("It is an anagram")
else:
    print("It is not an anagram")
