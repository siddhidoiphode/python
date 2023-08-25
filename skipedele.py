
ans=[]
elem=[]
size=int(input("enter size of array: "))
for i in range(0,size):
  if(i==size):
    break;
  print("""
    Do you want to enter element?
    1) yes
    2) skip
       """)
  opt=int(input(" Enter your option: "))

  if(opt==1):
    print(" Enter element: ")
    ele=int(input(" "))     
    elem.append(ele)
  elif(opt==2):
    an=i+1
    ans.append(an)
  else:
    print("enter valid option")
set(ans)
print("\n\n  skipped elements are of position: ")
print(ans)
    
