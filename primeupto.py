num = 2
count = 0
while count < 75:
    prime = True
    for i in range(2,num):
        if num%i == 0:
            prime = False
            break
    if prime:
        print(num)
        count += 1
    num += 1