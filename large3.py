# Write a python program to find the largest of three numbers.
a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))
c = int(input("Enter value of c : "))

if a>b:
    if a>c:
        print("Largest among all is A")
    elif c>b:
        print("Largest among all is C")
else :
    if b>c:
        print("Larges amon all is B")
    elif c>a:
        print("Largest among all is C")