s=list(map(int,input("enter numbers").split()))
largest=s[0]
for n in s:
  if n>largest:
    largest=n
print("largest number:",largest)
