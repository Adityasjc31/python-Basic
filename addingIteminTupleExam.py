tuplex = (4,6,7,3,2,1)
print(tuplex)
tuplex = tuplex + (9,)
print(tuplex)
tuplex = tuplex[:5] + (12,20,25) + tuplex[:5]
print(tuplex)

elem = int(input("Enter a number in tuple : "))
tuplex = tuplex + (elem,)
print(tuplex)