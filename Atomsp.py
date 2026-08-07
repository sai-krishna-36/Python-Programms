num = int(input("Enter a Number: "))
Sq = num * num
digit = len(str(num))
if Sq % (10 ** digit) == num:
	print("Yes")
else:
	print("No")