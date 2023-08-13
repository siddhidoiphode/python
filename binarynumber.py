n=int(input("enter a number : "))
s=str(n)
l=len(s)
flag=0
for i in range(0,l):
  if int(s[i])==0 or int(s[i])==1:
     flag=flag+1
if flag==l:
   print("it is binary")
else:
   print("it is not binary")
  
