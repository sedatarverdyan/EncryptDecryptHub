# Author: Seda Tarverdyan | Copyright (c) 2024 | Use of this code requires keeping this copyright notice.
key_text = input("Write key text: ")

def key_generation():
    key_s = ""
    key_upper = key_text.upper()
    for i in key_upper:
        if i not in key_s and i != " ":
            key_s += i
           
    return key_s

key_start = key_generation()
print("Key Start:", key_start)

def key_generation_end():
    key_e = ""
    start = ord("A")
    for _ in range(26):  
        current = chr(start)
        if current not in key_start:
            key_e += current
        start += 1  
    return key_e    

key_end = key_generation_end()
print("Key End:", key_end)

key = key_start + key_end
print("Full Key:", key)

dictionary = {}
start = ord("A")
for i in range(26):
    current = chr(start)
    dictionary[current] = key[i]
    start += 1  

print(dictionary)

text = input('Write text you want to encrypt: ').upper()
print("Original Text:", text)

def encryption():
    encrypted_text = ""
    for i in text:
        if i.isalpha():
            encrypted_text += dictionary[i]  
        else:
            encrypted_text += i  
    return encrypted_text

encrypted = encryption()
print("Encypted:", encrypted)
def decryption():
    decrypted_text = ""
    for i in encrypted:
        if i.isalpha():
            for key, value in dictionary.items():
                if value == i:
                    decrypted_text+=key
        else:
            decrypted_text+=i
    return decrypted_text
decrypted = decryption()
print("Decrypted:", decrypted)  


# key = state engineering university of armenia