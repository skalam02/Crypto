import hashlib
from salt import *

#This program creates a password hash and checks user input to see if the password entered is correct.


def main():
    #takes password input and prepends random salt
    password=input("enter your password: ")
    thesalt=salt()
    saltypassword= thesalt+password
    print("your salty password is ",saltypassword)

    #create hash object and update with salty password
    hashbrown= hashlib.sha512()
    hashbrown.update(saltypassword.encode())

    #output salt and hash to passwords.txt
    output=open("passwords.txt",'w')
    output.write(thesalt+"\n"+hashbrown.hexdigest())
    output.close()

    #opens password file and retrieves salt and hash
    fileinput=open("passwords.txt",'r')
    retreivedsalt=fileinput.readline()
    retreivedsalt=retreivedsalt[:-1]
    retreivedhash=fileinput.readline()
    fileinput.close()

    #gets password from user, creates a hash and matches it against the stored hash
    askpassword=input("enter your password: ")
    askpassword=retreivedsalt+askpassword
    checkhash=hashlib.sha512()
    checkhash.update(askpassword.encode())
    secondhash=checkhash.hexdigest()
    if (secondhash==retreivedhash):
        print ("Access Granted")
    else:
        print ("Access Denied")

main()

