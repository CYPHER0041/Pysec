import re
def convert(string):
    li=list(string.split("\n"))
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
    return pwd

def savepassword():
    print("Adding password to list")
    para=open("log.txt","r").read()
    li=convert(para)
    pwds=extractpassword(li)
    with open("passlist.txt",'a') as f:
        for item in pwds:
            f.write(item)
            f.write("\n")
        f.close()