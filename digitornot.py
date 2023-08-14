#Python program to check given character is digit or not.
c=input("enter a single character : ")
digit='0123456789'
count=0
for i in c:
  if i in digit:
    count=count+1
if count==len(c):
  print("It is a digit")
else:
  print("It is not a digit")
  
