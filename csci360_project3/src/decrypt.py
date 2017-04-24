from bit2text import *

def decrypt(key,ciphertext):

    if (len(key)!=len(ciphertext)):
        print ("Key length must be same as ciphertext")
        return 0
    plaintext=""
    for i in range(len(key)):
        plaintext+=str(int(key[i])^int(ciphertext[i]))

    return bit2text(plaintext)
