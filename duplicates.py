list=[1,3,4,5,6,7,9,6,7,3]
duplicates=[]
for i in list:
    if list.count(i)>1 and i not in duplicates:
        duplicates.append(i)
print("duplicates:",duplicates)
