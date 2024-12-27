name=input("what is your name : ")
print("Hello",name)

##print("your BMI is : ",float(input("enter your weight in kg : "))/float(input("enter your height in m : "))**2)

s=False
while s!=1:
    m = input("you have your height in measure of :- cm, m, inch or foot? : ")
    if m=="m" or m=="cm" or m=="foot" or m=="inch" :
        s=1
    else :
        print("you have entered a wrong measure for height.\nplease pick one of the given measures")


if m=="cm":
    h = float(input("enter your height in cm : "))
    h = h/100

elif m=="m":
    h = float(input("enter your height in m : "))

elif m=="inch":
    h = float(input("enter your height in inch : "))
    h = h*2.54/100

else:
    h = float(input("enter your height in foot : "))
    h = h*12*2.54/100

w = float(input("enter your weight in kg : "))
bmi=w//h**2
print("your BMI is  : ",bmi)

if bmi<=18.5:
    print("your BMI indicates that you are underweight")

elif 25>=bmi>18.5:
    print("your BMI indicates that you have a normal weight")

elif 30>=bmi>25:
    print("your BMI indicates that you are overerweight")

elif bmi>30:
    print("your BMI indicates tat you are obese")
