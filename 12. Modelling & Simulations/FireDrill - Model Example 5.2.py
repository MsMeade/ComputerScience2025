B1Students = 0
B2Students = 0
B1Exits = 0
B2Exits = 0

print ("Welcome to the Fire Drill Model")
print ("Please provide the number of students in school today")
print("and we will provide the time that the school should be evacuated")
print("*****************************************************")
print("  ")
B1Exits = int(input("How many exits were accessible in buidling 1:"))
B1Students = int(input("How many students were in building 1 today: "))
B2Exits = int(input("How many exits were accessible in buidling 2:"))
B2Students = int(input("How many students were in building 2 today: "))

def Building1(B1Exits, B1Students):
    if B1Exits == 2:
        B1ExitTime = 60 + (B1Students * 5)
    else:
        B1ExitTime = 60 + (B1Students * 7)
        
    return B1ExitTime

def Building2(B2Exits, B2Students):
    if B2Exits == 3:
        B2ExitTime = 40 + (B2Students * 3)
    elif B2Exits == 2:
        B2ExitTime = 40 + (B2Students * 5)
    else:
        B2ExitTime = 40 + (B2Students * 7)
        
    return B2ExitTime


B1 = Building1(B1Exits, B1Students)
B2 = Building2(B2Exits, B2Students)    

minutes, seconds = divmod(B1, 60)
print(f"{B1}s is {minutes}m {seconds}s")  
print ("It took ", f" {minutes}m {seconds}s ", "to exit building 1")

minutes, seconds = divmod(B2, 60)
print(f"{B2}s is {minutes}m {seconds}s")  
print ("It took ", f" {minutes}m {seconds}s ", "to exit building 2")