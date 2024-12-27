a=input("your name : ")+input("your love's name : ")
a= a.lower()

n=(a.count("t")+a.count("r")+a.count("u")+ a.count("e"))*10+a.count("l")+a.count("o")+a.count("v")+ a.count("e")

print(n)


if n>90 or n<10:
    print(f"your score is {n}, you go together like coke and mentos.")
elif 40<n<50:
    print(f"your score is {n}, you are all right together.")
else:
    print(f"your score is {n}.")
