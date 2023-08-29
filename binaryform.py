n=int(input(" enter number: "))
lis=[]
while(n!=0):
  lis.append(n%2)
  n=n//2
lis.reverse()
print(lis)
