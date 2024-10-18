# Author: Seda Tarverdyan | Copyright (c) 2024 | Use of this code requires keeping this copyright notice.
text = input('Input some text: ').replace(" ", "").lower()
print(text)
total = len(text)

def tokos():
    dictionary = {}
   
    for i in text:

        if i.isalpha():
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1

    for i, count in dictionary.items():
        percentage = (count / total) * 100
        print(f" {i}  Count: {count} : {percentage:.2f}%")

tokos()