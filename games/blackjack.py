import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
a=input("do you want to play a blackjack game. y or n : ")


def play():
    c=[]
    u=[]
    c.append(cards[random.randint(0,12)])
    u.append(cards[random.randint(0,12)])
    u.append(cards[random.randint(0,12)])
    su=u[0]+u[1]
    sc=c[0]

    print(f'your cards are {u} and your total is = {su}')
    print(f'computer first card is {c}')
    if su==21:
        return "you won"
    
    a=input("type y to pick another card or n to pass : ")
    while a=="y":
        p=random.randint(0,12)
        u.append(cards[p])
        if p==0 and su+p>21:
            u[-1]=1
        su=0
        print(f'your cards are = {u}')
        for i in u:
            su+=i
            if su>21:
                return f"your total is = {su}\nyou went over\nyou lose"
            elif su==21:
                return f"your total is = {su}\nyou won"
        print(f'your total is = {su}')
        a=input("type y to pick another card or n to pass : ")

    while a=="n":
        p=random.randint(0,12)
        c.append(cards[p])
        if p==0 and sc+p>21:
            c[-1]=1
        sc=0
        print(f'computers cards are = {c}')
        for i in c:
            sc+=i
            if sc>21:
                return f"computers total is = {sc}\nopponent went over\nyou won"
            elif sc<21:
                if sc+10<=21:
                    a="n"
                else:
                    a=random.choice(["n","y"])
            elif sc==21:
                return f"computers total is = {sc}\nyou lost"
        print(f'computers total is = {sc}')

    print(f"your final deck is {u} = {su}\ncomputers final deck is {c} = {sc}")
    if su>sc:
        return "you won"
    elif su<sc:
        return "yoou lost"
    elif su==sc:
        return "draw"

while a=="y":
    print(play())
    a=input("do you want to play another blackjack game. y or n : ")
