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
search=input("Enter name to find contact number -")
for i in range(ele):
  if search==name[i]:
    flag=flag+1
if flag==1:
   print("--Found--\n")
   print("Name:",search," number:",num[i])
else:
  print(" --Not found--")
