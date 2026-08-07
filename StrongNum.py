num = int(input("Enter a Number:"))
temp = num
total = 0
while temp > 0:
	digit = temp % 10
	fact = 1
	for i in range(1,digit+1):
		fact *= i
	total += fact
	temp = temp // 10
if num == total:
	print("OK")
else:
	print("Not OK")