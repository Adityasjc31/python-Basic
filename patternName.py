name = input("Enter a name : ")
length = len(name)
i = -1
space = 0
z = int(length/2)
right = int(length/2 + 1)
for x in range(length, int(length/2), -1):
    for y in range(1, z+1):
        print(name[y-1], end="")

    q = length if x >= (length-1) else length+space
    if x <= (length-1):
        space = space + 1
        
    for y in range(x, q):
        print(end=" ")

    for y in range(right, (length + 1)):
        print(name[y-1], end="")
    print()
    z = z - 1
    if x<=(length-1):
        right = right + 1
