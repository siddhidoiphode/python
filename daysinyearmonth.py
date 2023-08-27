days=int(input("Enter number of days : "))
years=days//365
rem=days-(years*365)
months=rem//30
rem=rem-(months*30)
weeks=rem//7
rem=rem-(weeks*7)
print("\n--There are--\n\n",years,"years",months,"months",weeks,"weeks,",rem,"days")
print("\n in given number of days")
