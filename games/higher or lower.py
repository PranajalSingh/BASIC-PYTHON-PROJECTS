
import random
#names={'a':100,'b':120,'c':109,'d':200,'s':210}
names=["a","b","c","d","e"]
f=[100,200,300,400,500]
x=random.randint(0,len(names)-1)
k=True
score=0
while k==True:
    a=names[x]
    y=random.randint(0,len(names)-1)
    b=names[y]
    if a!=b:
        print(f"a = {a}")
        print(f"b = {b}")
        n=input("who has more followers a or b? : ")
        if f[x]>f[y] and n=="a":
            score+=1
            x=y
            print(f'correct! your score is {score}')
        elif f[x]<f[y] and n=="b":
            score+=1
            x=y
            print(f'correct! your score is {score}')
        else:
            print(f'wrong! your total score is {score}')
            c=input("type y to play another game and n to close : ")
            if c!="y":
                k=False