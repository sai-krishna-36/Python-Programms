arr = [10, 2, 8, 1, 7, 20]
first = arr[0]
last = arr[-1]
big = None
small = None
for num in arr:
    if num == first or num == last:
        continue
    if big is None or num > big:
        big = num
    if small is None or num < small:
        small = num
if big is not None and small is not None:
    print(big-small)