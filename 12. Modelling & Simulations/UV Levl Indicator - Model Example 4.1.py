print("Please enter a number between 0 and 24")
time= int(input("What time do you want to check the UV rays :"))

if (time <=6 and time >=0) or (time >=20 and time <=24):
    print("There are no uv rays as it is dark")
elif (time >6) and (time <20):
    if (time >=6 and time <9) or (time >=18 and time <20):
        print ("The uv level are strength low")
    elif (time >=9 and time <10) or (time >=17 and time <18):
        print ("The uv level are strength moderate")
    elif (time >=10 and time <11) or (time >=16 and time <17):
        print ("The uv level are strength high")
    elif (time >=11 and time <12) or (time >=15 and time <16):
        print ("The uv level are strength VERY HIGH")
    else:
        print("The uv level is EXTREME")
        
   