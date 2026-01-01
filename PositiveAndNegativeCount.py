arr=list(map(int,input("enter elements in list:").split()))
pos=0
neg=0
for i in arr:
    if i>0:
        pos=pos+1
    elif i<0:
        neg+=1
print("positive numbers in list:",pos)
print("negative numbers in list:",neg)
