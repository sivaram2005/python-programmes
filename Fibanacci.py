n=int(input("enter no of terms"))
a=0
b=1
print("fibanaci series:")
for i in range(n):
    print(a,end="")
    c=a+b
    a=b
    b=c
