num = int(input())
even = 0
odd = 0
while num > 0:
    digit = num % 10
    if digit%2 == 0:
        even += digit
    else:
        odd += digit
    num //= 10
print(even)
print(odd)