def encrypt(key, plaintext):
    if (len(key) != len(plaintext)):
        print("key must be the same length and plaintext")
        return
    ciphertext=""
    for i in range(len(key)):
        ciphertext+=str(int(key[i])^int(plaintext[i]))
    return ciphertext