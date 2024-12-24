l1=[1,2,3,4,5,6,7,8,9]
s=0
l2=[i for i in l1 if i%2==0]
print(l2)


for i in l1:
    if i%2==0:
        s+=i
print(s)
