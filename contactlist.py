ele=int(input("Enter number of contacts in list: \n"))
name=[]
num=[]
flag=0
print("\n")
for i in range(ele):
  n=input("Enter name: ")
  no=int(input("Enter number: "))
  print("\n")
  name.append(n)
  num.append(no)
  
search=input("Enter name to find contact number -\n")

for i in range(ele):
  if search==name[i]:
   flag=flag+1
   print("\nName:",search," number:",num[i])

if flag==1:
   print("--Found--\n")
else:
  print(" --Not found--")


