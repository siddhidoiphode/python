#**********12.  first and last digit  addition (python)  *************

n=input()
l=len(n)
num=int(n)
last=num%10
div="1"
for i in range(1,l):
  div=div+"0"
divn=int(div)
first=num//divn
print("first=",first)
print("last",last)
print(" sum of first and last dight = ",first+last)

