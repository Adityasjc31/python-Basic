# A company decides to give bonus to all its employees on Diwali. A 5% bonus on 
#     salary is given to the male worker and 10% bonus on salary to the female 
#     workers. WAP to enter the salary of the employee and gender of the employee. 
#     If the salary of the employee is less than Rs. 10,000 then the employee gets an 
#     extra 2% bonus on salary. Calculate the bonus that has to be given to the 
#     employee and display the salary that the employee will get.

salary = float(input("Enter salary of the employee : "))
gender = input("Enter gender of employee : ")
bonusper = 0
if gender == "male":
    bonusper = 5
elif gender == "female":
    bonusper = 10

if bonusper<10000 :
    bonusper = bonusper +2

bonus = (bonusper/100) * salary

increment = salary + bonus

print("Salary incremente by : ",bonus)
print("Final Salary : ",increment)