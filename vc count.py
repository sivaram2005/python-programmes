s=input("enter a string")
vowels=0
consonants=0
for ch in s:
 if ch.isalpha():
  if ch in "aeiouAEIOU":
   vowels=vowels+1
  else:
   consonants=consonants+1
print("vowels count:",vowels)
print("consonants count:",consonants)
