str1=str(input("enter string: "))
oc=str(input("enter letter to be counted occurance.:"))
flag=0

for i in str1 :
  if i==oc :
    flag=flag+1

print("no of times it is occuired= ",flag)
