time = int(input("What is the hour? (Enter a value between 0 and 24): "))
if time>=0 and time<6:
    print("the UV rating is: none")
elif time >=6 and time <9:
    print("UV rating is: low")
elif time >=9 and time <10:
    print("UV rating is: moderate")
elif time >=10 and time <11:
    print("UV rating is: high")
elif time >=11 and time <12:
    print("UV rating is: very high")
elif time >=12 and time <15:
    print("UV rating is: extreme")
elif time>=20 and time<24:
    print("the UV rating is: none")
elif time >=18 and time <20:
    print("UV rating is: low")
elif time >=17 and time <18:
    print("UV rating is: moderate")
elif time >=16 and time <17:
    print("UV rating is: high")
elif time >=15 and time <16:
    print("UV rating is: very high")
else:
    print("Invalid time entered")