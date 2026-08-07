arr = [5, 11, 25, 3, 18]
arr2 = [i for i in arr if i > 10]
mini = arr2[0]
maxi = arr2[0]
for num in arr2:
    if num < mini:
        mini = num
    elif num > maxi:
        maxi = num
print(maxi-mini)