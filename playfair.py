# Author: Seda Tarverdyan | Copyright (c) 2024 | Use of this code requires keeping this copyright notice.
key_text = input("Write key text: ")
matrix = []

def key_generation():
    key_s = ""
    key_upper = key_text.upper()
    for i in key_upper:
        if i not in key_s and i != " ":  
            key_s += i
            matrix.append(i)
    return key_s

key_start = key_generation()
print("Key Start:", key_start)

def key_generation_end():
    key_e = ""
    start = ord("A")
    for _ in range(26):  
        current = chr(start)
        if current not in key_start and current != 'J': 
            key_e += current
            matrix.append(current)
        start += 1
    return key_e    

key_end = key_generation_end()
print("Key End:", key_end)

key = (key_start + key_end)
print("Full Key:", key)

playfair_matrix = [matrix[i:i + 5] for i in range(0, 25, 5)]

print("Playfair Matrix:")
for row in playfair_matrix:
    print(" ".join(row))


#
def text_maker():
    text_first = input("Write your text: ")
    space_positions = [i for i, char in enumerate(text_first) if char == ' ']  
    text_first = text_first.upper().replace("J", "I").replace(" ", "")  
    
    text = ''
    i = 0
    while i < len(text_first):
        char1 = text_first[i]
        char2 = text_first[i + 1] if i + 1 < len(text_first) else "Z"  
        if char1 == char2: 
            text += char1 + 'Z'
            i += 1
        else:
            text += char1 + char2
            i += 2

    return text, space_positions

text, space_positions = text_maker()
print("Prepared Text:", text)



def find_position(letter, matrix):
    for i, row in enumerate(matrix):
        if letter in row:
            return i, row.index(letter)

def encrypt_pair(char1, char2, matrix):
    row1, col1 = find_position(char1, matrix)
    row2, col2 = find_position(char2, matrix)

    if row1 == row2:  # Same row
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:  # Same column
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:  
        return matrix[row1][col2] + matrix[row2][col1]

def encrypt(text, matrix):
    encrypted = ""
    for i in range(0, len(text), 2):
        encrypted += encrypt_pair(text[i], text[i + 1], matrix)
    return encrypted

encrypted = encrypt(text, playfair_matrix)
print("Encrypted Text:", encrypted)


def decrypt_pair(char1, char2, matrix):
    row1, col1 = find_position(char1, matrix)
    row2, col2 = find_position(char2, matrix)

    if row1 == row2:  # Same row
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:  # Same column
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:  
        return matrix[row1][col2] + matrix[row2][col1]

def decrypt(encrypted, matrix):
    decrypted = ""
    for i in range(0, len(encrypted), 2):
        decrypted += decrypt_pair(encrypted[i], encrypted[i + 1], matrix)
    return decrypted

decrypted_text = decrypt(encrypted, playfair_matrix)

def reinsert_spaces(decrypted, space_positions):
    for pos in space_positions:
        decrypted = decrypted[:pos] + ' ' + decrypted[pos:]
    return decrypted

decrypted_text_with_spaces = reinsert_spaces(decrypted_text, space_positions)
print("Decrypted Text:", decrypted_text_with_spaces)
# key = state engineering university of armenia