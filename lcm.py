a,b=input(" ").split()
a=int(a)
b=int(b)
if(a>b):
  great=a
else:
  great=b
flag=0
while(flag==0):
  if(great%a==0 and great%b==0):
    flag=1
    lcm=great
  great=great+1
print(lcm)
