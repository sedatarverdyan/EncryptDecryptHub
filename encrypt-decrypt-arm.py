# Author: Seda Tarverdyan | Copyright (c) 2024 | Use of this code requires keeping this copyright notice.
key = int(input("Enter a key: "))
print(key)
key = key % 39  
check = input('Would you like to decrypt:(yes/no) ')
encrypt = ''
string = input("Enter the text: ")
print(string)


for i in string:
    if ord('Ա') <= ord(i) <= ord('Ֆ'):
        encrypt += chr((ord(i) + key - ord('Ա')) % 39 + ord('Ա'))
    elif ord('ա') <= ord(i) <= ord('ֆ'):
        encrypt += chr((ord(i) + key - ord('ա')) % 39 + ord('ա'))
    elif ord(i) == 1415:  # "և"
        encrypt += i  
print('Encrypted:', encrypt)


if check == 'yes':
    decrypt = ''
    for i in encrypt:
        if ord('Ա') <= ord(i) <= ord('Ֆ'):
            decrypt += chr((ord(i) + 39 - key - ord('Ա')) % 39 + ord('Ա'))
        elif ord('ա') <= ord(i) <= ord('ֆ'):
            decrypt += chr((ord(i) + 39 - key - ord('ա')) % 39 + ord('ա'))
        elif ord(i) == 1415:  
            decrypt += i  
    print('Decrypted:', decrypt)
