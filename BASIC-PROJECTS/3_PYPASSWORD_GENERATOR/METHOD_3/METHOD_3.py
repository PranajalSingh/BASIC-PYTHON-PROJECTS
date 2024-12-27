#Password Generator Project
import random
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
s = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nl= int(input("How many letters would you like in your password?\n")) 
ns = int(input(f"How many symbols would you like?\n"))
nn = int(input(f"How many numbers would you like?\n"))

p=[]
st=""
for i in range(1,nl+1):
    p.append(random.choice(l))

for i in range(1,ns+1):
    p.append(random.choice(n))

for i in range(1,nn+1):
    p.append(random.choice(s))

print(p)

for i in range(1,len(p)+1):
    ran=random.choice(p)
    p.remove(ran)
    st+=ran
print(st)
