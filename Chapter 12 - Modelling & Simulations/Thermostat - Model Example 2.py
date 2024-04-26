actual = int(input("Enter the current temperature: "))
target = int(input("Enter your target temperature: "))

if actual < target:
    tempOnorOff = 1
else:
    tempOnorOff = 0

print(tempOnorOff)
    

#current temp is 22, target is 20, so heat should go off      
#current temp is 18 degrees, so heat should go on