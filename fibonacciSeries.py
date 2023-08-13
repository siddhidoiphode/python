first=0
second=1
next=0
n=10

print("series is\n")
print(first)
print(second)
for i in range(1,n-1,1):
  next=first+second
  first=second
  second=next
  print(next)
