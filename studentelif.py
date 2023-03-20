# WAP in python to enter the marks of a student in 4 subjects. Then calculate the
#     total and aggregate and also display the grade obtained by the student. If the
#     student scores an aggregate >= 75%, then the grade is distinction.
#         If aggregate is 60>= and <75, then grade = 1st division
#         If aggregate is 50>= and <60, then grade = 2nd division
#         If aggregate is 40>= and <50, then grade = 3rd division
#         else grade is fail.

std = {}

for x in range(1,5):
    key = input("Enter subject name : ")
    str = "Enter marks in " + key + " : "
    value = int(input(str))
    std.update({key : value})

marks = std.values()
total=0

for m in marks:
    total += m

print("Total : ",total)
aggerate = (total/400) * 100
if aggerate>=75:
    print("1st Division")
elif aggerate>=60 and aggerate<75:
    print("2nd Division")
elif aggerate>=50 and aggerate<60:
    print("3rd Divison")
elif aggerate>=40 and aggerate<50:
    print("4th Divison")
else:
    print("Fail")