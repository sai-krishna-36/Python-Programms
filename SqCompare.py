arr = [2, -3, 4]
arr2 = [i*i for i in arr]
print(arr2)
small = arr2[0]
big = arr2[0]
for num in arr2:
    if num > big:
        big = num
    elif num < small:
        small = num
print(big-small)