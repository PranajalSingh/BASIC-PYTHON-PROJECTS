import random
a=random.randint(1,100)
level=input("you want to play on which level easy, medium or hard : ")
guess=10
if level=="medium":
    guess=7
elif level=="hard":
    guess=5

while True:
    n=int(input("guess a number between 1 to 100 : "))
    if n==a:
        print("you won")
        break
    elif n<a:
        print("low")
        guess-=1
    elif n>a:
        print("high")
        guess-=1
    if guess==0:
        print("you lost")
        break
