numList=[3,5,-7,2,-1,6]
print("This is my uncleaned list ", numList)

#iterate through each item in the list
#if it is negative, remove it

for item in numList:
  if item<0:
    numList.remove(item)

print("The negative numbers hav ebeen removed. This is my new cleaned list ",numList)
