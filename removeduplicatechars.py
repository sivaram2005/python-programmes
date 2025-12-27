s=input("enter a string:")
result=""
for ch in s:
  if ch not in result:
    result=result+ch
print("after removing duplicates:",result)
