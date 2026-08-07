str1 = input("Enter a String:")
clean = ""
for ch in str1:
	if ch != " ":
		clean += ch
rev =""
for i in clean:
	rev = i + rev
if clean.lower() == rev.lower():
	print("It is a Pallindrome")
else:
	print("Not a Pallindrome")