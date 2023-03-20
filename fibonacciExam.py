n = int(input("Enter number of terms : "))
a = 0
b = 1
c = a+b
print(a,end=" ")
for j in range(2,n+1):
    print(c,end=" ")
    c = a+b
    a,b = b,c
    