import random

names=input("names seperated by a comma(,) : ")
print(names)
names=names.split(",")
a=random.randint(0,len(names)-1)
print(names[a])
print(names)
