import random
import string

chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]d
def encrypt():
    for char in plain_text:
        index = chars.index(char)
        cipher_text.append(key.index(index))
    print(cipher_text)


print("------ Encryption Terminal ------")
print("Enter your choice: ")
print("1 - Encrypt")
print("2 - Decrypt")
choice = input("Enter here: ")
if choice == "1":
    plain_text = input("Enter text: ")
    encrypt()
    