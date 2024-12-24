def cal(a,n,b):
    if n=="+":
        s=a+b
    elif n=="-":
        s=a-b
    elif n=="*":
        s=a*b
    elif n=="/":
        s=a/b
    print(s)
    k=int(input(f"enter 1 to continue with {s} or 0 to take new values : "))
    while k==1:
        n=input("enter operation : ")
        b=int(input("ennter next value : "))
        if n=="+":
            s+=b
        elif n=="-":
            s-=b
        elif n=="*":
            s*=b
        elif n=="/":
            s/=b
        print(s)
        k=int(input(f"enter 1 to continue with {s} or 0 to take new values : "))

while True:
    a=float(input("enter first number : "))
    n=input("""enter operation :
    +
    -
    *
    /
    """)
    b=float(input("enter second number : "))
    s=0
    cal(a,n,b)

        
