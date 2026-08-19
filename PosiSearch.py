arr = [1,2,3,4,5,6,7,8]
posi = -1
target = int(input())
for i in range(len(arr)):
    if target == arr[i]:
        posi = i
        break
if posi != -1:
    print("The Position is",posi)
else:
    print("Item not found")