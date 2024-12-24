import time
start = time.time()

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

x = random.sample(letters, k=nr_letters)
y = random.sample(numbers, k=nr_numbers)
z = random.sample(symbols, k=nr_symbols)
password = [x, y, z]

ps = ""
for i in password:
    for j in i:
        ps += j

final_password = ''.join(random.sample(ps,len(ps)))
print(final_password)



# import random
#
# u_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# l_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# combined_data = [l_letters, u_letters, numbers, symbols]
#
# print("Welcome to the PyPassword Generator!")
# nr_elements = int(input("How many elements would you like in your password?: "))
#
# password = ""
# for i in range(nr_elements):
#     y = random.choice(combined_data)
#     x = random.randint(0,len(y)-1)
#     password += y[x]
#
# print(f"Here is your password: {password}.")


start = time.time() - start
print(start)