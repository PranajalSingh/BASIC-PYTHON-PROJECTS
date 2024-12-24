
import random
names=[{"name":"a",
        "followers":100,
        "profession":"w"},
       {"name":"b",
        "followers":200,
        "profession":"x"},
       {"name":"c",
        "followers":300,
        "profession":"y"},
       {"name":"d",
        "followers":400,
        "profession":"z"},
       ]

a=random.choice(names)
k=True
score=0
while k==True:
    b=random.choice(names)
    if a!=b:
        print(f"a = {a["name"]}, a {a["profession"]}")
        print(f"b = {b["name"]}, a {b["profession"]}")
        n=input("who has more followers a or b? : ")
        if a["followers"]>b["followers"] and n=="a":
            score+=1
            a=b
            print(f'correct! your score is {score}')
        elif a["followers"]<b["followers"] and n=="b":
            score+=1
            a=b
            print(f'correct! your score is {score}')
        else:
            print(f'wrong! your total score is {score}')
            c=input("type y to play another game and n to close : ")
            if c!="y":
                k=False