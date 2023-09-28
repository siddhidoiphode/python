i=1
j=2
k=2
n=3
lis=[]
for a in range(i+1):
  for b in range(j+1):
    for c in range(k+1):
       if(a+b+c!=n):
          lis.append([i,j,k])
print(lis)
