# li=[]
# n=int(input("Enter number of elements in list: "))
# for i in range(n):
#    ele= int(input())
#    li.append(ele)
# print(" \n")
# for i in range (len(li)):
#   for j in range(i+1,len(li)):
#     if li[i]+li[j]==15:
#       print(li[i],li[j])
   
s=list(map(int,input().split()))
for i in range(len(s)):
  for j in range(len(s)):
    if s[i]+s[j]==25:
      print  (s[i],s[j])
