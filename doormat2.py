n,m=map(int,input("").split())
j=1
till=n//2
str_wel="WELCOME"
while (j<n-1):
  print(('-'*(till*3))+(".|."*j)+('-'*(till*3)))
  till-=1
  j+=2
#print(('-'*-w)+"WELCOME"+('-'*n))
print(str_wel.center(m,'-'))
till=1
j=n-2
#print(till,j)
while (j>=1):
  print(('-'*(till*3))+(".|."*j)+('-'*(till*3)))
  till+=1
  j-=2
