#program to take inputs and concatinate them with strings and other inputs

print("Hello", input("what is your name : "),"!")
print("name generated is : ",input("city name : "),input("pet name : "))


#avoiding null values

name=input("what is your name : ")
while len(name)==0:
    name=input("what is your name : ")
print("Hello",name,"!")
city=input("city name : ")
while len(city)==0:
    city=input("city name : ")
pet=input("pet name : ")
while len(pet)==0:
    pet=input("pet name : ")
print("name generated is : ",city,pet)

print("program terminated")

