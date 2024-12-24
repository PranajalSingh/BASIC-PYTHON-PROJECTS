a=[0,0,0]
b=[0,0,0]
c=[0,0,0]
abc=[a,b,c]

print(f"{a}\n{b}\n{c}")
p=input("enter position")

abc[int(p[1])-1][int(p[1])-1]="X"

print(f"{a}\n{b}\n{c}")


##abc=[[0,0,0],[0,0,0],[0,0,0]]
##print(abc)
##abc[0][0]=1
##print(abc)
