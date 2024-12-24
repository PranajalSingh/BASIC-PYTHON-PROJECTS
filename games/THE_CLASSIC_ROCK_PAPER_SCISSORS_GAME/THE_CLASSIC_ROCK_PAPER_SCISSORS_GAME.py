import random
n=random.randint(0,2)
l=["rock","paper","scissors"]
c=l[n]

u=input("choose rock, paper or scissors : ")
u=u.lower()

#rock
r="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
p="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
s="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("you choosed")
if u == "rock":
    print(r)
elif u == "paper":
    print(p)
else:
    print(s)

print("computer choosed")
if c == "rock":
    print(r)
elif c == "paper":
    print(p)
else:
    print(s)


if (c=="rock" and u=="paper") or (c=="paper" and u=="scissors") or (c=="scissors" and u=="rock"):
    print("you won")
elif u==c:
    print("tie")
else:
    print("you lost")
