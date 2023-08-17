ele=int(input("Enter number of students in list: \n"))
roll=[]
name=[]
marks=[]
for i in range(ele):
  n=input("Enter name of roll no  : ")
  name.append(n)
  m=float(input("Enter marks of roll no : "))
  marks.append(m)
  r=i+1
  roll.append(r)
print("what do you wnat to do?")
print("1) View ")
print("2) Modify")
print("3) Add student")
print("4) Delete\n")
cho=int(input("Enter your choice: "))
if cho==1:
  nr=int(input("Enter roll number: "))
  print("Details:\n")
  print("Name:",name[nr-1])
  print("Marks:",marks[nr-1])
elif cho==2:
  nr=int(input("Enter roll number: "))
  name[nr-1]=input("Modify name: ")
  marks[nr-1]=float(input("Modify marks: ") )                  
elif cho==3:
    nr=ele+1
    roll.append(nr)
    name[nr-1]=input("Enter name: ")
    marks[nr-1]=float(input("Enter marks: "))
elif cho==4:
   nr=int(input("Enter roll number: "))
   roll.pop(nr-1)
   name.pop(nr-1)                
   marks.pop(nr-1)
else:
  print("enter valid entity")
