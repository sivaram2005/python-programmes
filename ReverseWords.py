s=input("enter sentence:").split()
print("before:",s)
for ch in s:
    print(ch[::-1],end="")

