arr = [2,3,5,6,7,4]
target = int(input())
posi = -1
for i in range(len(arr)):
    if arr[i] == target:
        posi = i
        break
if posi != -1:
    print(posi)
else:
    print("Element not found")
