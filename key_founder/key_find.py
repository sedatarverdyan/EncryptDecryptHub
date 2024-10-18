# Author: Seda Tarverdyan | Copyright (c) 2024 | Use of this code requires keeping this copyright notice.
word = 'xMzvH'
key = 1
word=word.lower()
file = open('key_founder/words_alpha.txt', 'r')


def decrypt_word(word, key):
    decrypt = ''
    for i in word:
        if 'A' <= i <= 'Z':
            decrypt += chr((ord(i) - ord('A') - key + 26) % 26 + ord('A'))
        elif 'a' <= i <= 'z':
            decrypt += chr((ord(i) - ord('a') - key + 26) % 26 + ord('a'))
        else:
            decrypt += i  
    return decrypt


matches = []


while key <= 25:
    decrypted_word = decrypt_word(word, key)
    file.seek(0)  # Ամեն անգամ ֆայլը կարդում է սկզբից 
    for line in file:
        dictionary_word = line.strip() 
        if decrypted_word == dictionary_word:
           matches.append((decrypted_word, key))  
    
    key += 1  

if matches:
    for match, key in matches:
        print(f"Decrypted word is : {match}, and the key is  {key}")
else:
    print("we didnt find the word")

file.close()
