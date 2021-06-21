def decrypt(string, shift):

  cipher = ''
  for char in string:
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97)

  return cipher
#check the above function
# O gs Zosuzne Ykck Umujk krHZXIZjls
ct= input("enter string: ")
s= int(input("enter shift number: "))
print("Original string: ", ct)
print("After decryption: ", decrypt(ct, s))