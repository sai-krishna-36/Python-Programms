int1 = int(input("Enter a Number:"))
flag = False
if int1 == 1:
	print("1 is a prime number")
elif int1 > 1:
	for i in range(2, int1):
		if (int1 % i) == 0:
			flag = True
			break
if flag :
	print("Its is not a Prime Number")
else:
	print("it is a Prime Number")