arr = [25, 78, 98, 67, 55]
key = 98
found = False
for i in arr:
    if i == key:
        found = True
        break
if found:
    print("value found")
else:
    print("value not found")
