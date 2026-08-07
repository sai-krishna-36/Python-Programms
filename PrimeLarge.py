Prime = []
for num in range(50,2000):
	if num > 1:
		for i in range(2,num):
			if num % i == 0:
				break
		else:
			Prime.append(num)
print("minimum", min(Prime))
print("minimum", max(Prime))