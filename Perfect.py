num = int(input("Enter a Number:"))
total = 0
for i in range(1,num//2+1):
	if num%i == 0:
		total += i
if total == num:
	print("Perfect")
else:
	print("Not Perfect")