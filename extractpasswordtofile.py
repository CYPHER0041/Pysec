import re
#funtion to split the strings on spaces
def convert(string):
    li=list(string.split("\n"))
    return li
#function to extract words that satisfy the password validity
def extractpassword(li):
    pwd=[]
    for password in li:
        #password lenght
        if(len(password)<8):
            continue
        #password has alphabets
        elif not re.search("[a-z]", password):
            continue
        #password has captialized alphabets
        elif not re.search("[A-Z]", password):
            continue
        #password has numerics
        elif not re.search("[0-9]", password):
            continue
        #password has special characters
        elif not re.search("[_@$]", password):
            continue
        #password doesnt have space
        elif re.search("\s", password):
            continue
        #if satisfy call condtions then append to list
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
