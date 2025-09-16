name = input("Please enter your name: ")
yearOfBirth = int(input("Please enter your year of birth:"))

currentAge = (2025-yearOfBirth)
futureAge = (currentAge+25)
percentLived = (currentAge/100)*100
percentLeft = 100 - percentLived

print("By my calculations,", name,"you are:", currentAge,"years old")
print("In 25 year you will be:", futureAge, "years old, wow that is old...")
print("You have lived approximately", percentLived, "% of your life")
print("You have approximately", percentLeft,"% left!")
print("Go live your life,",name,"!")