
def text2bit(text):
    bitstring = ""
    for letter in text:
        bitstream = str(bin(ord(letter)))
        bitstream = bitstream[2:]
        while (len(bitstream) != 8):
            bitstream = "0" + bitstream
        bitstring+=bitstream
    return bitstring