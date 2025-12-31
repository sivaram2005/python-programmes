arr=[25,78,98,67,55]
n=len(arr)
for i in range(n):
  for j in range(n-i-1):
    if a[j]<a[j+1]:
      a[j],a[j+1]=a[j+1],a[j]
print(arr)
