days_in_month=[31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(y):
    if y%4==0 and y%100!=0 or y%400==0:
        return True
    else:
        return False

date1=input("enter starting date in DD-MM-YYYY format : ")
date2=input("enter ending date in DD-MM-YYYY format : ")
list1=date1.split("-")
list2=date2.split("-")
print(list1,list2)

year_left=int(list2[2])-int(list1[2])
#print(year_left)

month_left=(year_left*12+(int(list2[1])-int(list1[1])))%12
if int(list1[1])>int(list2[1]):
    year_left-=1
#print(month_left)

td=0
for y in range(int(list1[2])+1,int(list2[2])+1):
    if is_leap(y):
        days_in_month[1]=29
        td+=366
    else:
        days_in_month[1]=28
        td+=365

days_left=days_in_month[int(list1[1])-1]-int(list1[0])+int(list2[0])
if days_left>=days_in_month[int(list1[1])-1]:
    days_left-=days_in_month[int(list1[1])-1]
#print(days_left)

print(f'''{year_left} years {month_left} months and {days_left} days
or {year_left*12+month_left} months and {days_left} days''')
