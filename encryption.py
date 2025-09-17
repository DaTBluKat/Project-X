import random
import string

chars = list(string.ascii_letters + string.digits + string.punctuation + " ")
key = chars.copy()
random.shuffle(key)  # Key is a shuffled version of chars

def encrypt(plain_text):
    cipher_text = []
    for char in key:
        print(char, end="")
    print()
    for char in plain_text:
        if char in chars:
            idx = chars.index(char)
            cipher_text.append(key[idx])
        else:
            cipher_text.append(char)
            
    return ''.join(cipher_text)

def decrypt(cipher_text):
    plain_text = []
    for char in cipher_text:
        if char in key:
            idx = key.index(char)
            plain_text.append(chars[idx])
        else:
            plain_text.append(char)
    return ''.join(plain_text)
    
while True:
    print("------ Encryption Terminal ------")
    print("Enter your choice: ")
    print("1 - Encrypt")
    print("2 - Decrypt")
    print("3 - Quit")
    choice = input("Enter here: ")
    
    if choice == "1":
        plain_text = input("Enter text: ")
        print("Encrypted:", encrypt(plain_text))
    elif choice == "2":
        cipher_text = input("Enter cipher text: ")
        key = input("Enter key: ")
        print("Decrypted:", decrypt(cipher_text))
    elif choice == "3":
        break;