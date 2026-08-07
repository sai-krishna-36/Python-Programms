list = [1,32,43,65,38,12,54,76,23,89]
max1 = float('-inf')
max2 = float('-inf')
for num in list:
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2 and num != max1:
        max2 = num
print("The second largest number is:", max2)