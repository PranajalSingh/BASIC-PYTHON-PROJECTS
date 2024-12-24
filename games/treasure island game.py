#program to make a treasure island game

start = input("enter START to enter in the island : ")
start = start.lower()

while start != "start":
    start = input("enter START to enter in the island : ")
    start = start.lower()

lives = int(input("how many lives you want : "))

print(f'''
welcome to the jungle summoner

your mission is to find the treasure which is hidden somewhere in this island\nwhich is full of dangers.

you have got {lives} lives

all you have to do is to pick one of two given options
for picking first option enter 1
for picking second option enter 0
for each wrong choice you will lose a live.
if you lost all of your lives you will lose the game

so you have successfully reached the island''')

print("\na bear is running towards you.")
bear = int(input("fight or hide : "))
while bear==1:
    lives-=1
    if lives==0:
        print("you lost")
        break
    print(f"you lost a live and left with {lives} more lives\n")
    bear = int(input("fight or hide : "))

if lives!=0:
    print("\na huge river came between your path.")
    river = int(input("wait or swim : "))
    while river==1:
        lives-=1
        if lives==0:
            print("you lost")
            break
        print(f"you lost a live and left with {lives} more lives\n")
        river = int(input("wait or swim : "))
    
if lives!=0:
    print("\na volcano exploded nearby.")
    volcano = int(input("climb on a tree or run away : "))
    while river==1:
        lives-=1
        if lives==0:
            print("you lost")
            break
        print(f"you lost a live and left with {lives} more lives\n")
        volcano = int(input("climb on a tree or run away : "))

if lives!=0:
    print("\nyou reached in front of a mysterious cave.")
    cave = int(input("enter or not : "))
    while cave==0:
        lives-=1
        if lives==0:
            print("you lost")
            break
        print(f"you lost a live and left with {lives} more lives\n")
        cave = int(input("enter or not : "))
        
if lives!=0:
    print("\nyou have finally found the treasure chest.")
    chest = int(input("go ahead and touch it or throw a stone at it : "))
    while chest==1:
        lives-=1
        if lives==0:
            print("you lost")
            break
        print(f"you lost a live and left with {lives} more lives\n")
        chest = int(input("go ahead and touch it or throw a stone at it : "))

if lives!=0:
    print("you won")
