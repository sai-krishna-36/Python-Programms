arr = [2,2,1]
count = {}
for i in arr:
    count[i]=count.get(i,0)+1
for i in arr:
    if count[i] == 1:
        print(i)
        break