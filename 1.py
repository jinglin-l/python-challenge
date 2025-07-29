input = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
input2 = "map"

def translate(input):
    output = ""
    for char in input:
        if char in (" ", ".", "(", ")"):
            output += char
        else:
            if char == "y" or char == "z":
                output += chr(ord(char) - 24)
            else:
                output += chr(ord(char) + 2)
    return output

print(translate(input))
print(translate(input2))    

