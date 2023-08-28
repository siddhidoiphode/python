n=int(input(" enter number: "))
lis=[]
for i in range(1,n+1):
  if (n%i==0):
    flag=0
    for j in range(1,n+1):
      if(i%j==0):
        flag=flag+1
    if(flag==2):
        lis.append(i)
print(lis)
