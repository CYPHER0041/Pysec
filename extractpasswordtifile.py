import re
def convert(string):
    li=list(string.split(" "))
    return li
def extractpassword(li):
    pwd=[]
    for password in li:
        if(len(password)<8):
            continue
        elif not re.search("[a-z]", password):
            continue
        elif not re.search("[A-Z]", password):
            continue
        elif not re.search("[0-9]", password):
            continue
        elif not re.search("[_@$]", password):
            continue
        elif re.search("\s", password):
            continue
        else:
            pwd.append(password)
            continue
    return pwd
para=input("Enter The Paragraph: ")
li=convert(para)
print(convert(para))
print(extractpassword(li))
pwds=extractpassword(li)
with open('password.txt','w') as f:
    for item in pwds:
        f.write("%s\n"%item)