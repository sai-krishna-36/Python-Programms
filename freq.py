arr = [1,2,3,2,3,4,6,2,5,7,8,7,3,4,5,7,9]
target = int(input())
count = 0
for num in arr :
    if num == target:
        count += 1
print(f"{target} appeared {count} times in the list")