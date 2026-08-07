a = [1, 5, 9]
b = [2, 6, 3]
arr = a+b
m = arr[0]
n = arr[0]
for num in arr:
    if num > m:
        m = num
    elif num < n:
        n = num
print(m-n)