print("---------------encode----------------\n")
def encode(text,shift):

  alphabets="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
  cipher_text=""
  for letter in text:
    position=alphabets.index(letter)
    new_position=position+shift
    cipher_text=cipher_text+alphabets[new_position]
  print(cipher_text)

text=input("Enter your message here : ")
shift=int(input("Enter shifting number : "))
encode(text,shift)


print("\n---------------decode----------------")
def decode(text1,shift1):

   alphabets="zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
   decoded=""
   for letter in text1:
      position=alphabets.index(letter)
      new_position=position-shift1
      decoded=decoded+alphabets[new_position]
   print(decoded)
   print("\n\n")

text1=input("\nEnter your encoded message here : ")
shift1=int(input("Enter shifting number : "))
decode(text1,shift1)
