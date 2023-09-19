n=int(input("Enter any number: "))
lis=[]
sum=0
for i in range(1,n):
  if(n%i==0):
    sum=sum+i
print(sum)
print(n)
if(sum==n):
  print(" It is perfect number")
else:
   print(" It is not perfect number")
