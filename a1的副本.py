#!/usr/bin/env python3

from a1_support import is_word_english
import string


def change(c,i,en = 'en'):
    # c = c.lower()
    num = int(ord(c))
    if num >= 97 and num <= 122:
        if en =='en':
            num = 97 + ((num - 97) + int(i)) % 26
        else:
            num = 97 + ((num - 97) - int(i)) % 26
    return chr(num)

def encrypt(text, offset):
    string_new = ''
    for s in text:
        string_new += change(s, offset)
    # print(string_new)
    return string_new

def decrypt(text, offset):
    string_new = ''
    for s in text:
        string_new += change(s, offset, en = 0)
    # print(string_new)
    return string_new

def ﬁnd_encryption_offsets(encrypted_text):
    res = []
    word = encrypted_text.split(' ')
    l = len(word)
    if l > 1:
        for i in range(1,26):
            flag = 1
            for j in word:
                if is_word_english(decrypt(j, i)) == False:
                    flag = 0
                    break
            if flag == 1:
                res.append(i)
    else:
        for i in range(1,26):
            j = word[0]
            if is_word_english(decrypt(j, i)) == True:
                res.append(i)

    return tuple(res) 

def main():
    # Add your main code here
    while(True):
        z = input('''Please choose an option [e/d/a/q]:\ne) Encrypt some text\nd) Decrypt some text\na) Automatically decrypt English text\nq) Quit\n''')

        if z == 'e':
            x = input("Please enter some text to encrypt: ")
            y = input("Please enter a shift offset (1-25): ")
            if y == 0:
                print("The encrypted text is: ")
                for i in range(1,26):
                    print('%2d: ' %i,encrypt(x, i))
                print('')
            else:
                print("The encrypted text is: ", encrypt(x, y), '\n')


        elif z == 'd':
            x = input("Please enter some text to decrypt: ")
            y = input("Please enter a shift offset (1-25): ")
            if y == 0:
                print("The decrypted text is: ")
                for i in range(1,26):
                    print('%2d: ' %i,decrypt(x, i))
                print('')
                
            else:
                print('The decrypted text is: ',decrypt(x, y), '\n')

        elif z == 'a':
            x = input("Please enter some encrypted text: ")
            x = x.strip()
            res = ﬁnd_encryption_offsets(x)
            if len(res) == 0:
                print("No valid encryption offset", '\n')
            elif len(res) == 1:
                print("Encryption offset: ", res[0])
                print("Decrypted message: ", decrypt(x, res[0]))
            else:
                print("Multiple encryption offsets: ", end = " ")
                for i in res :
                    print(i, end=' ')
                print('')
            
        elif z == 'q':
            print("Bye!")
            break
        else:
            print("Invalid command")
    

if __name__ == '__main__':
    main()

