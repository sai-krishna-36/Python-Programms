# num = int(input("Enter a Number: "))
# if num == 1:
#     print("1 is a prime")
# elif num > 1:
#     for i in range(2,num):
#         if num% i == 0:
#             print("This is not a prime Number")
#             break
#     else:
#         print(num, "is a prime Number12")

upto = int(input("Enter valid Number: "))
num = 2
count = 0
while count < upto:
    prime = True
    for i in range(2,num):
        if num%i == 0:
            prime = False
            break
    if prime:
        print(num)
        count += 1
    num += 1