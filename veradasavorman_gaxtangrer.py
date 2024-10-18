# Author: Seda Tarverdyan | Copyright (c) 2024 | Use of this code requires keeping this copyright notice.
key = int(input("Enter key number: "))
print(key)

def encrypting():
    a = input("Input your text: ")
    text = ''
    for i in a:
        if i == " ":
            continue
        else:
            text += i

    length = len(text)
    tox = -(-len(text) // key)  
    count_z = key - (len(text) % key) if len(text) % key != 0 else 0
    text = (text + count_z * "z").upper()  
    print("Processed Text:", text)

    matrix = []
    for i in range(0, len(text), key):
        row = list(text[i:i + key])  
        matrix.append(row)
    print("Matrix for Encryption:")
    for row in matrix:
        print(row)

    encrypt = ''
    for col in range(key):
        for row in matrix:
            if col < len(row):  
                encrypt += row[col]
    print("Encrypted Text:", encrypt)
    return encrypt  


def decrypting(encrypt):
    rows = -(-len(encrypt) // key)  
    decrypt_matrix = []
    for i in range(rows):
        row = [''] * key  
        decrypt_matrix.append(row)

    index = 0
    for col in range(key):
        for row in range(rows):
            if index < len(encrypt): 
                decrypt_matrix[row][col] = encrypt[index]
                index += 1

    print("Reconstructed Matrix for Decryption:")
    for row in decrypt_matrix:
        print(row)

    decrypt = ''
    for row in decrypt_matrix:
        decrypt += ''.join(row)

    
    print("Decrypted Text:", decrypt)


choice = input("Do you want to encrypt or decrypt the text? (e/d): ").lower()
if choice == 'e':
    encrypted_text = encrypting()
elif choice == 'd':
    encrypted_text = input("Enter the encrypted text for decryption: ")
    decrypting(encrypted_text)
else:
    print("Invalid choice. Please choose 'e' for encrypt or 'd' for decrypt.")


# Computer Systems and Informatics Department
# CTSAFTEMOETNOIPEMREDRCANPSMIMSRTUYSNADTZ