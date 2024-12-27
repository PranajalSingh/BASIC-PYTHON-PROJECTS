#program to calculate split including tip(in amount)
print("each person needs to pay : ",(int(input("total bill : "))+int(input("how much tip you want to give : ")))/int(input("no. of people : ")))

#program to calculate split including tip(in percentage)
total = int(input("total bill is : "))
tip = int(input("percentage of tip you want to give? 10, 12 or 15? : "))
n = int(input("no. of people : "))

print("each person needs to pay ", (total+tip/100*total)/n)
