a=list(map(int,input("enter elements:").split()))
n=len(a)
for i in range(n):
  for j in range(n-i-1):
    if a[j]<a[j+1]:
      a[j],a[j+1]=a[j+1],a[j]
print(a)
key=int(input("enter key:"))
low=0
high=len(a)-1
found=False
while low<high:
    mid=(low+high)/2
    if a[mid]==key:
        found=True
        break
    elif a[mid]<key:
        low=mid+1
    else:
        high=mid-1
if found:
    print("element found")
else:
    print("element not found")
