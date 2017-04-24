#decrypts a cipher
def decrypt(key,ciphertext):

    skey = sorted(key)
    r, c, index = 0,0,0
    sorted_ciphertext, plaintext = "",""
    height = math.ceil(len(ciphertext)/len(key))
    matrix = [["X" for x in range(len(key))] for y in range(height)]
    transposed = [["X" for x in range(len(key))] for y in range(height)]

    #fills a matrix with ciphertext
    while (r < height):
        while (c < len(key)):
            if (index == len(ciphertext)):
                break
            matrix[r][c] = ciphertext[index]
            index = index + 1
            c = c + 1
        r = r + 1
        c = 0

    #reverse transposes the transposed matrix
    c = 0
    for letter in key:
        r = 0
        into = skey.index(letter)
        while (r < height):
            transposed[r][c] = matrix[r][into]
            r = r + 1
        c = c + 1

    #extracts ciphertext from matrix and converts to plaintext
    for list in transposed:
        for char in list:
            sorted_ciphertext+=char
    for i in range(int(len(sorted_ciphertext)/2)):
        jump=i*2
        if sorted_ciphertext[jump:jump+2] in reversesquare:
            plaintext+=reversesquare[sorted_ciphertext[jump:jump+2]]

    return plaintext