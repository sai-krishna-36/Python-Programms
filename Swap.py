# lipo = [3, -1, 7, -5, 10, 2]
# ramo = lipo[0]
# ramu = lipo[0]
# for num in lipo:
#     if num > 0:
#         if num > ramo:
#             ramo = num
#         elif num < ramu:
#             ramu = num
# diffy = ramo - ramu
# print(diffy)

# lipo2 = [-10, -3, 5, 9]
# posi = [ abs(i) for i in lipo2]
# m = posi[0]
# n = posi[0]
# for num in posi:
#     if num > m:
#         m = num
#     elif num < n:
#         n = num
# d = m -n
# print(d)

# arr = [1, 8, 2, 12, 5, 4]
# m = None
# n = None
# for num in arr:
#     if num % 2 == 0:
#         if m is None or num > m:
#             m = num
#         if n is None or num < n:
#             n = num
# d = m - n
# print(d)

# arr = [4, 4, 9, 1, 9, 2]
# arr2 =[]
# min1 = arr[0]
# max1 = arr[0]
# for num in arr:
#     if num not in arr2:
#         arr2.append(num)
# print(arr2)
# for num in arr2:
#     if num < min1:
#         min1 = num
#     elif num > max1:
#         max1 = num
# d = max1-min1
# print(d)

# arr = [5, 2, 9, 8, 1, 6]
# max1 = None
# min1 = None
# for num in arr:
#     if num%2 != 0:
#         if max1 is None or num > max1:
#             max1 = num
#     if num%2 == 0:
#         if min1 is None or num < min1:
#             min1 = num
# if max1 is not None and min1 is not None:
#     print(max1-min1)

arr = [5, 2, 9, 8, 1, 6]
mini = min(arr)
maxi = max(arr)
small = None
big = None
for num in arr:
    if num == mini or num == maxi:
        continue
    if small is None or num < small:
        small = num
    if big is None or num > big:
        big = num
if small is not None and big is not None:
    print(big - small)

