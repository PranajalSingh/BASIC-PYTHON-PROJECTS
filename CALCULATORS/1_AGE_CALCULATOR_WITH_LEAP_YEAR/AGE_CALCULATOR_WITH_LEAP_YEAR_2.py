#saving list of no. of days in each months
days_in_month=[31,28,31,30,31,30,31,31,30,31,30,31,31,28,31,30,31,30,31,31,30,31,30,31]

#taking input and converting it into a list as integers
date1=input("enter starting date in DD-MM-YYYY format : ")
date2=input("enter ending date in DD-MM-YYYY format : ")
list1=date1.split("-")
list2=date2.split("-")

for i in range(0,len(list1)):
    list1[i]=int(list1[i])
    list2[i]=int(list2[i])
print(list1,list2)

#####################################################

n=0
year_left=list2[2]-list1[2]
if list1[1]>list2[1]:
    year_left-=1
    n=1
    
month_left=((year_left+n)*12+(list2[1]-list1[1]))%12
if list1[0]>list2[0]:
    month_left-=1

td=0
for y in range(list1[2]+1,list2[2]+1-n): ##
    if y%4==0 and y%100!=0 or y%400==0:
        days_in_month[1]=29
        days_in_month[13]=29
        td+=366
    else:
        days_in_month[1]=28
        days_in_month[13]=28
        td+=365


days_left=days_in_month[list1[1]-1]-list1[0]+list2[0]
if days_left>=days_in_month[list1[1]-1]:
    days_left-=days_in_month[list1[1]-1]


for i in range(list1[1],list1[1]+month_left): ##
    td+=days_in_month[i]
td+=days_left

#####################################################

print(f"{year_left} years {month_left} months and {days_left} days")
print(f"{year_left*12+month_left} months and {days_left} days")
print(f"{td//7} weeks snd {td%7} days")
print(f"{td} days")
print(f"{td*24} hours")
print(f"{td*24*60} minutes")
print(f"{td*24*60*60} seconds")
