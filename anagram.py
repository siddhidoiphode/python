str1=str(input("enter string1: "))
str2=str(input("enter string2: "))
l1=len(str1)
l2=len(str2)
m1=0
m2=0

for i in str1:
  if i in str2:
    m1=m1+1

for i in str2:
  if i in str1:
    m2=m2+1

if m1==l2 and m2==l1 :
  print("it is anagram")
