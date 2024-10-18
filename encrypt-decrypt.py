# Author: Seda Tarverdyan | Copyright (c) 2024 | Use of this code requires keeping this copyright notice.
key = int(input("Enter a key: "))
print(key)
key = key % 26

check = input('Would you like to decrypt:(yes/no) ')
encrypt = ''
string = input("Enter the text: ")
print(string)
for i in string:
    if ord('A') <= ord(i) <= ord('Z'):
        encrypt += chr((ord(i) + key - ord('A')) % 26 + ord('A'))
    elif ord('a') <= ord(i) <= ord('z'):
        encrypt += chr((ord(i) + key - ord('a')) % 26 + ord('a'))
print('Encrypted:',encrypt)
if check=='yes':
    decrypt = ''
    for i in encrypt:
        if ord('A') <= ord(i) <= ord('Z'):
            decrypt += chr((ord(i) + 26 - key - ord('A'))% 26 + ord('A'))
        elif ord('a') <= ord(i) <= ord('z'):
            decrypt += chr((ord(i) + 26 - key - ord('a'))% 26 + ord('a'))    
print('Decrypted:', decrypt)
