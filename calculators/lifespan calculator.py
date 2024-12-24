#program to calculate days, weeks, months and years left in life assuming your total life span is 90 years

print("enter your date of birth in DD MM YY format")
bd = int(input("DD "))
bm =int(input("MM "))
by = int(input("YY "))

print("enter current date in DD MM YY format")
cd = int(input("DD "))
cm =int(input("MM "))
cy = int(input("YY "))

td = int(input("no. of years you expect to live : "))*365

dl = td-(cy-by)*365-(cm-bm)*52-(cd-bd)
dl += dl/365/4


print("no. of days left for you is",round(dl))

print("no. of weeks left for you is",round(dl/7),"weeks and ",round(dl%7),  "days")

print("no. of months left for you is",round(dl/(365/12)),"months, ",round((dl%(365/12))/7),"weeks and ",round((dl%(365/12))%7),"days")

print(f"no. of years left for you is {round(dl/365)} years, {round((dl%365)/30)} months, {round(((dl%365)%30)/7)} weeks and {round(((dl%365)%30)%7)} days")
#f-string allows us to put variables in a string using {}
