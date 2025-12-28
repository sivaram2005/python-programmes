arr=[10,78,-89,8,0]
largest=float('-inf')
second=float('-inf')
for i in arr:
    if i>largest:
        second=largest
        largest=i
    elif i>second and i!=largest:
        second=i
if second==float('-inf'):
    print("not exists")
else:
    print("second largest number is :",second)
