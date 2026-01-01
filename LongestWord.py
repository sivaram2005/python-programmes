s=input("enter a sentence:").split()
longest=s[0]
for w in s:
    if len(w)>len(longest):
        longest=w
print("longest word is:",longest)
