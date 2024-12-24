# program to calculate pizza order bill

s = input("would you like to take S , M or L size :")
p = input("need pepperoni? Y or N : ")
c = input("need extra cheese? Y or N : ")

t=0
if s == "S" or s =="s":
    t+=15
    if p == "Y" or p == "y":
        t+=2
    if c == Y or c == "y":
        t+=1

elif s == "M" or s =="m":
    t+=20
    if p == "Y" or p == "y":
        t+=3
    if c == "Y" or c == "y":
        t+=1

elif s == "L" or s =="l":
    t+=25
    if p == "Y" or p == "y":
        t+=3
    if c == "Y" or c == "y":
        t+=1

print(f"your total bill is {t}")
