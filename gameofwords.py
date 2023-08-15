print("\n\n")
print("Player 1 : KEVIN")
print("Player 2 : STUART")
print("\n")
r=int(input("enter number of rounds: "))
vowel="aeiouAEIOU"
scok=0
scos=0
kev=[]
st=[]
print("\nEnter words for KEVIN: " )
for i in range(r):
  k=input(" ")
  kev.append(k)
print("\nEnter words for STUART:" )
for i in range(r):
   s=input(" ")
   st.append(s)
for i in kev:
  if i[0] in vowel:
     scok=scok+1
for i in st:
  if i[0] in vowel:
     scos=scos+1
print("points of kevin : ",scok)
print("points of stuart: ",scos)
print("\n")
if scok>scos:
  print("************* KEVIN is winner **************")
elif scok<scos:
  print("************** STUART is winner **************")
elif scok==scos:
  if scok==0 and scos==0:
    print("---------------------It will be a draw------------------------")
  else:
    print("-------------------It's a tie-------------------")
