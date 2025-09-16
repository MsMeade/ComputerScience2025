print ("Welcome to the Fire Drill Model")
print ("Please provide the number of students in school today")
print("and we will provide the time that the school should be evacuated")
print("*****************************************************")
print("  ")
B1Exits = int(input("How many exits were accessible in buidling 1:"))
B1Students = int(input("How many students were in building 1 today: "))
B2Exits = int(input("How many exits were accessible in buidling 2:"))
B2Students = int(input("How many students were in building 2 today: "))


if B1Exits == 2:
    B1ExitTime = 60 + (B1Students * 5)
else:
    B1ExitTime = 60 + (B1Students * 7)

print("The time taken for students to evacuate building 1 should be:", B1ExitTime)
B1ExitTimeMins = int(B1ExitTime//60)
B1ExitTimeSec = int(B1ExitTime - (B1ExitTimeMins*60))
print("This is", B1ExitTimeMins, "minutes and",B1ExitTimeSec, "seconds") 

if B2Exits == 3:
    B2ExitTime = 40 + (B2Students * 3)
elif B2Exits == 2:
    B2ExitTime = 40 + (B2Students * 5)
else:
    B2ExitTime = 40 + (B2Students * 7)

print("The time taken for students to evacuate building 2 should be:", B2ExitTime)
B2ExitTimeMins = int(B2ExitTime//60)
B2ExitTimeSec = int(B2ExitTime - (B2ExitTimeMins*60))
print("This is", B2ExitTimeMins, "minutes and",B2ExitTimeSec, "seconds") 

