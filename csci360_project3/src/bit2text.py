def bit2text(bitstring):
    index = 8
    i = 0
    text = ""
    while (index <= len(bitstring)):
        cut=bitstring[i:index]
        text+=chr(int(cut, 2))
        i = index
        index += 8
    return text