""" This block is defined such that the orginal file gets encrypted to .aes and the original file is deleted. When entering the
pass phrase, if the wrong phrase is entered, the encrypted file is deleted and if the correct phrase is entered, the original 
file is restored while the encrypted file is deleted."""

import sys
import pyAesCrypt
import pyautogui as pa
from secure_delete import secure_delete
from steg import RevealData

#checks for keyphrase that we have entered
def checkKeyphrase(filePath,encryptPass,keyphrase):
    guess=input("Enter the keyphrase: ")
    if guess == keyphrase:
        DecryptFile(filePath,encryptPass) #decrypts the aes file
    else:
        DeleteFile(filePath) #deletes the aes file


def EncryptFile(filePath, encryptPass,keyphrase):
    pyAesCrypt.encryptFile(filePath, (filePath+'.aes'), encryptPass) # encrypt to aes, default buffer is 64k
    print("File Encrypted")
    secure_delete.secure_random_seed_init()
    secure_delete.secure_delete(filePath) # deletes the original plaintext file leaving only encrypted aes
    checkKeyphrase(filePath,encryptPass,keyphrase)

def DecryptFile(filePath,encryptPass):
        pyAesCrypt.decryptFile((filePath+".aes"),filePath,encryptPass)
        secure_delete.secure_random_seed_init(); 
        secure_delete.secure_delete((filePath+".aes")) #deletes the encrypted file after decrypting
        print("File decrypted")
        RevealData()
        sys.exit("Completed")

def DeleteFile(filePath):
    print("Incorrect phrase...deleting file")
    secure_delete.secure_random_seed_init() #delete file if keyphrase fails
    secure_delete.secure_delete((filePath+".aes"))
    exit()

def setup():
    keyphrase=input("Enter the keyphrase: ") #keyphrase to trigger delete or decrypt actions
    filePath=input("Filename to encrypt: ") #name and type of file
    encryptPass=input("Password to encrypt file: ") #password to encrypt the file
    EncryptFile(filePath,encryptPass,keyphrase)