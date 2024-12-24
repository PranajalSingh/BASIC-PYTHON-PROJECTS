w=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
   'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def encrypt(n):
    nl=[]
    ns=""
    
    for i in range(0,len(n)):
        nl.append(n[i])
        k=w.index(n[i])
        if ed==1:
            nl[i]=w[k+a]
        if ed==0:
            nl[i]=w[k-a]
    for i in nl:
        ns=ns+i
    print(ns)   

yn="yes"
while yn=="yes":
    ed=int(input("enter 1 for encode or 0 for decode : "))
    a=int(input("enter no. of shifts : "))
    encrypt(input("enter message : "))
    yn=input("type yes to do again or no to end : ").lower()
