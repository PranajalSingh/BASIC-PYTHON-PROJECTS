#ride fee calculator

h = int(input("what is your height in cm : "))
t=0
if h>120:
    age = int(input("what is your age : "))
    if age<12:
        t+=5
    elif 12<age<18:
        t+=7
    else:
        t+=12
    photos = input("do you want photos. Y or N")
    if photos == "Y":
        t+=3
    print(f"your total bill is ${t}")
else:
    print("sorry you can't get a ride")
