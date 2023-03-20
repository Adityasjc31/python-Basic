ar = [5,6,7,2,3,1,0,9]
for x in range(len(ar)):
    index = x
    for y in range(x+1,len(ar)):
        if ar[index] > ar[y]:
            index = y
    temp = ar[x]
    ar[x] = ar[index]
    ar[index] = temp

print(ar)