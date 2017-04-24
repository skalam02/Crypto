from encrypt import *
from decrypt import *
from keygen import *
from text2bit import *
from bit2text import *

def application():

    answer=input("Would you like to encrypt or decrypt? ")

    if answer == "encrypt":
        plaintext=input("What would you like to encrypt: ")
        binpt=text2bit(plaintext)
        key=keygen(len(binpt))
        ciphertext=encrypt(key,binpt)
        newct=bit2text(ciphertext)
        print("Your ciphertext is:",newct)


    if (answer == "decrypt"):
        ct=input("Enter Ciphertext to be decrypted:")
        ctkey=input("Enter decryption key:")
        binct=text2bit(ct)
        plaintext=decrypt(ctkey,binct)
        print("Your plaintext is: ",plaintext)
