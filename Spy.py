num = int(input("Enter a Number:"))
s = 0
p = 1
temp = num
while temp > 0:
	digit = temp % 10
	s += digit
	p *= digit
	temp = temp // 10
if s == p:
	print("SPY")
else:
	print("Not SPY")