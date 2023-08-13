
p='.|.'
str="welcome"
row=int(input("enter no.or rows - " ))
mid=(row//2)+1
print("columns should be in multiple of 3 that of rows")
col=int(input("enter no.or columns - "))
n=row-mid
for i in range(1,n+1):     
   j=2*i-1
   print((p*j).center(col,"-"))
print(str.center(col,'-'))
for i in range(n-1,-1,-1):
   t=2*i+1
   print((p*t).center(col,'-'))

