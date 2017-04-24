#!/usr/bin/env python
#Stylianos Kalamaras
#Group 10
#Project 1
#CSCI 360
#Professor A. Wood

import math

# Create a dictionary
def create_dictionary():
    pt_alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # First, create a dictionary
    alph = {}
    # Create the dictionary from the string above
    # to avoid having to write the whole thing out.
    for letter in pt_alph:
        alph[letter] = 0
    return alph


# This function counts the number of each letter in
# a string and stores the values in a dictionary.
# INPUT: String and empty Dictionary
# OUTPUT: Dictionary
def letter_count(text, alph):
    for letter in text: # iterate through each character in the string
        if letter in alph: # If the letter is in the alphabet
            alph[letter] += 1 # Increment the associated entry in dictionary

    return alph # Return the updated alphabet.

#probability_dist takes sum of letter frequencies, and divides each letter frequncy by the total
# sum and stores back into the dictionary to give a percentage of the total
def probability_dist(dict):
    charsum=0
    for key in dict:
        charsum += dict[key]
    for key in dict:
        dict[key] = (dict[key]/charsum)
    return dict
#calculates the bhattacharya distance between two probability distributtions
def batt_dist(d1,d2):
    dist=0
    for number in range(26):
        dist= dist + (math.sqrt((d1[number])*(d2[number])))
    dist= -math.log(dist)
    return dist

#returns a list, in decreasing order of the letter probability distribution of a text file
def mkdist(name):
    fin = open(name, 'r')
    text = fin.read()
    text = text.upper()
    fin.close()
    alph = create_dictionary()
    alph = letter_count(text,alph)
    alph = probability_dist(alph)
    sortedalph = sorted(alph.values(), reverse = True)
    return sortedalph
#takes two text files as input and returns the bhattacharya distance
# between the probability distribution of the letter frequencies
def part3(name1,name2):
    alph = mkdist(name1)
    alph2 = mkdist(name2)
    dist = batt_dist(alph,alph2)
    return dist

# The main function.
def main():
    cipher = {'G': 'E',
              'K': 'T',
              'W': 'A',
              'U': 'N',
              'M': 'H',
              'A': 'O',
              'R': 'I',
              'B': 'S',
              'D': 'R',
              'J': 'D',
              'I': 'L',
              'L': 'U',
              'H': 'W',
              'V': 'C',
              'N': 'G',
              'Q': 'P',
              'C': 'M',
              'O': 'B',
              'P': 'F',
              'T': 'V',
              'Y': 'K',
              'S': 'Y',
              'E': 'J',
              'Z': 'X',
              'X': 'Q',
              'F': 'Z'}

    fin = open("file1.txt", "r")
    fout = open("decrypted.txt", "w")

    line = fin.readline()

    while(line!=""):
        for word in line:
            for char in word:
                if char in cipher:
                    fout.write(cipher[char])
                else:
                    fout.write(" ")
        fout.write("\n")
        line=fin.readline()
    fout.close()
    fin.close()

    bhatt_dist1 = part3("file2.txt","sample.txt")
    bhatt_dist2 = part3("file1.txt","sample.txt")

    fout = open("report.txt","w")
    fout.write("Bhatt distance between file1.txt and sample.txt is {}\n".format((bhatt_dist2)))
    fout.write("Bhatt distance between file2.txt and sample.txt is {}\n".format(bhatt_dist1))
    fout.write("The distance between file1 and sample shows that it is\n"
               "indeed the frequency of the english language, and the\n"
               "distance between file2 and sample shows that it is not\n"
               "the frequency of the english language. To decrypt file1.txt\n"
               "a key dict was created that mapped the most frequent letters\n"
               "of file1 to the most frequent letters of sample. This key dict\n"
               "was used to decrypt file1. This obviously did not decrypt\n"
               "file1 at the first pass, so the text was re-examined and\n"
               "keys were adjusted accordingly until the key was found\n")
    fout.close()
# Call the main function
main()