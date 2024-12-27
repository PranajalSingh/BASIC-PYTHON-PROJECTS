import random

u_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
l_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
combined_data = [l_letters, u_letters, numbers, symbols]

print("Welcome to the PyPassword Generator!")
nr_elements = int(input("How many elements would you like in your password?: "))

password = ""
for i in range(nr_elements):
    y = random.choice(combined_data)
    x = random.randint(0,len(y)-1)
    password += y[x]

print(f"Here is your password: {password}.")