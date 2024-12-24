import re

def is_valid_email(email_id):
    uname = email_id.split("@")[0]
    uid = email_id.split("@")[1]
    email_regex = r'^<+[a-zA-Z0-9_.%+-]+@[a-zA-Z]+.[a-zA-Z]+>+$'

    if re.match(email_regex, email_id) and uid.count(".") == 1:
        if ("-" != uname[1] and "-" != uname[-1] and "_" != uname[1] and
                len(email_id) <= 63 and "." != uname[1] and
                len(uid.split(".")[1]) <=4):
            return True
    else:
        return False

def mail(name, email_id):
    print(f'{name} {email_id}')

n = int(input())
for i in range(0, n):
    data = input()
    x = 0
    for j in data:
        if j in ["&", '"', "'", "!", ";", ":", "/"]:  # ["!",":"]:
            x += 1
    if data.count("@") == 1 and data.count(" ") == 1 and x == 0:
        data = data.split(" ")
        if is_valid_email(data[1]):
            mail(data[0], data[1])
