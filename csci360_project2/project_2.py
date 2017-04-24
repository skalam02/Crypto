#Stylianos Kalamaras
#Project Two
#03/08/17
#Professor: Alexander Wood

import math
keysquare = {'Q':'AA', 'C':'AD', '3':'AF', 'T':'AG', '6':'AV', 'W':'AX',
             'M':'DA', 'O':'DD', 'E':'DF', 'H':'DG', 'N':'DV', 'L':'DX',
             '8':'FA', 'A':'FD', '4':'FF', '2':'FG', '1':'FV', 'I':'FX',
             'G':'GA', 'B':'GD', '5':'GF', 'Z':'GG', 'R':'GV', '7':'GX',
             'S':'VA', 'X':'VD', '9':'VF', 'V':'VG', 'U':'VV', 'P':'VX',
             '0':'XA', 'K':'XD', 'J':'XF', 'F':'XG', 'D':'XV', 'Y':'XX'}

reversesquare = {'AA':'Q', 'AD':'C', 'AF':'3', 'AG':'T', 'AV':'6', 'AX':'W',
             'DA':'M', 'DD':'O', 'DF':'E', 'DG':'H', 'DV':'N', 'DX':'L',
             'FA':'8', 'FD':'A', 'FF':'4', 'FG':'2', 'FV':'1', 'FX':'I',
             'GA':'G', 'GD':'B', 'GF':'5', 'GG':'Z', 'GV':'R', 'GX':'7',
             'VA':'S', 'VD':'X', 'VF':'9', 'VG':'V', 'VV':'U', 'VX':'P',
             'XA':'0', 'XD':'K', 'XF':'J', 'XG':'F', 'XV':'D', 'XX':'Y'}

def keyGen():
    flag = True
    while (flag):
        flag=False
        code = input("Enter a Key: ")
        code=code.upper()
        i=0
        while (i<len(code)):
            j=i+1
            while (j<len(code) and flag == False):
                if (code[i]==code[j]):
                    flag = True
                    print("Bad Key!")

                j=j+1
            i=i+1
    return code

#encrypts plaintext
def Encrypt1():
    plaintext = input("Enter a string to encrypt: ")
    plaintext = plaintext.upper()
    ciphertext=""
    for letter in plaintext:
        if letter in keysquare:
            ciphertext+=keysquare[letter]
    return ciphertext

#returns matrix with configured list of ciphertext
def Encrypt2_Setup(key,ciphertext):
    width = len(key)
    height = math.ceil(len(ciphertext)/width)
    matrix= [["X" for x in range(width)] for y in range(height)]
    r=0
    c=0
    index=0
    while (r<height):
        while(c<width):
            if(index==len(ciphertext)):
                break
            matrix[r][c]=ciphertext[index]
            index=index+1
            c=c+1
        r=r+1
        c=0
    return matrix

#transposes a matrix
def Encrypt2_Transpose(key,matrix):
    width = len(key)
    height = len(matrix)
    skey = sorted(key)
    transposed=[["X" for x in range(width)] for y in range(height)]
    c = 0
    for letter in skey:
        into= key.index(letter)
        r=0
        while(r<height):
            transposed[r][c]=matrix[r][into]
            r=r+1
        c=c+1
    ciphertext=""
    for list in transposed:
        for char in list:
            ciphertext+=char
    return ciphertext



def main():
    thekey = keyGen()
    print(thekey)
    ciphertext = Encrypt1()
    e_matrix = Encrypt2_Setup(thekey,ciphertext)
    f_ciphertext = Encrypt2_Transpose(thekey,e_matrix)
    print("Ciphertext is: "+ f_ciphertext)

main()