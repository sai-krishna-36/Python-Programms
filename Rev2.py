#Str = input("Enter a String:").lower()
#Rev = ""
#for ch in Str:
#	Rev = ch + Rev
#if Str == Rev :
#	print("Its Pallindrome")
#else:
#	print("Its not a Pallindrome")


s1 = input("Enter a Number:")
s = ""
i = len(s1) -1
while i >= 0:
	s = s + s1[i]
	i = i - 1
print(s)
