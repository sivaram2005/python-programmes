a=list(map(int,input("enter elements in list1:").split()))
k=int(input("enter key value:"))
n=len(a)
k=k%n
rotate=a[k:]+a[:k]
print(rotate)
