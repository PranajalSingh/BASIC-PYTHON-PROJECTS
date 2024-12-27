#reverse of a string

n = input("your name : ")

l=len(n)
s=""
while l>0:
    s=s+n[l-1]
    l=l-1
print(s)

#reverse of a string shortcut

print(n[::-1])


#reverse of as number by coverting into string

n = int(input("enter number : "))

c=str(n)
m=int(c[::-1])
print(m)

#reverse of a number without converting into string

s=0
while n>0:
    a=n%10
    s=s*10+a
    n=n//10
print(s)
