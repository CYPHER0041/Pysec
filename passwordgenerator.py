import hashlib
result="null"
#convert plaintext into sha1
def encrypt():
    print("Password Encryption")
    print("Enter the password to be encrypted:")
    str=input()
    global result
    result=hashlib.sha1(str.encode()).hexdigest()
    print(result)

#brute force password check by comparing hash 
def decrypt():
    print("Enter the guess:")
    guess_str=input()
    cmp_result=hashlib.sha1(guess_str.encode()).hexdigest()
    print(cmp_result)
    if cmp_result==result:
        print("Password Found")

encrypt()
decrypt()


