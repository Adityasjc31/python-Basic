str  = input("Enter a string : ")
c1 = str[0]
c2 = str[len(str)-1]

new_str = c2 + str[1:len(str)-1] + c1

print(new_str)