# Write a python program to check whether a year is leap year or not.
year = int(input("Enter year : "))
if ( year%400 == 0) or (( year%4 == 0 ) and ( year%100 != 0)):
    print("Leap year")
else:
    print("Not a leap year")