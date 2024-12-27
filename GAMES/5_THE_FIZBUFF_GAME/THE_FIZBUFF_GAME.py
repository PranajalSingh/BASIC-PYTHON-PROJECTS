for i in range(1,101):
    if i%3==0 and i%5==0:
        print("fizbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)

# list3=[]
# list5=[]
# for i in range(3,101,3):
#     list3.append(i)
# for i in range(5,101,5):
#     list5.append(i)
#
# for i in range(1,101):
#     if i in list3 and i in list5:
#         print("fizbuzz")
#     elif i in list3:
#         print("fizz")
#     elif i in list5:
#         print("buzz")
#     else:
#         print(i)