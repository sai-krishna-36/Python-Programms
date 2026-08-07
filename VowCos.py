Str1 = input("Enter a String:").lower()
vowels = "aeiou"
v = ""
c = ""
for ch in Str1:
	if ch.isalpha():
		if ch in vowels:
			v += ch
		else:
			c += ch
print(v)
print(c)
