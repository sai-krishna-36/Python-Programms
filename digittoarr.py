num = 593178
temp = num
arr=[]
while temp > 0:
    digit = temp%10
    arr.append(digit)
    temp = temp // 10
print(arr)
small = arr[0]
big = arr[0]
for num in arr:
    if num < small:
        small = num
    elif num > big:
        big = num
print(big-small)