s=input("enter a string")
vowels="AEIOUaeiou"
count=0
for i in s:
 if i in vowels:
  count=count+1
print("vowels count in given string:",count)
