def generateKey(cipher_text, key):
    key = list(key)
    if len(cipher_text) == len(key):
        return(key)
    else:
        for i in range(len(cipher_text) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

def plainText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
        ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))


cipher_text = input("Enter the cipher text: ")
keyword = input("Enter the Key: ")
key = generateKey(cipher_text, keyword)
print("Decrypted Text :",  plainText(cipher_text, key))