busFee = 0 
numStudents = 0

print ("Welcome to the Bus Hire Model")
print ("Please provide the cost of the bus and the number of students travelling :")
print("The school will pay the first €100")
print("The remainder of the bus cost will be split between the students")
print("*****************************************************")
print("  ")
busFee= float(input("Please enter the cost of the bus :"))
numStudents = int(input("Please enter the number of students travelling"))
                
ratePerStudent = round(((busFee - 100)/numStudents),2)
print("The rate per student is €", ratePerStudent)