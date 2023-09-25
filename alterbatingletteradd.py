str1=input("Enter first string: ")
str2=input("Enter second string: ")
l1=len(str1)
l2=len(str2)
if l1>=l2 :
  for i in range(0,l2):
    new=new+str1[i]+str2[i]
else:
  for i in range(0,l1):
    new=new+str1[i]+str2[i]   
print(new)
if l1>l2 :
  sub=l1-l2
if l2>l1 :
  sub=l2-l1 
print(sub)
