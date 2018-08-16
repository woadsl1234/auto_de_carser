#!/usr/bin/env python3

from a1_support import is_word_english
import string

__author__ = "ckj123"

# Write your functions here
low_ascall = string.ascii_lowercase

def encrypt(text, offset):
    res = ''
    for i in text:
        index = low_ascall.find(i)
        if index > -1 :
            res += low_ascall[(index + offset)%26] 
        else:
            res += i
    return res

def decrypt(text, offset):
    res = ''
    for i in text:
        index = low_ascall.find(i)
        if index > -1 :
            res += low_ascall[(index - offset)%26] 
        else:
            res += i
    return res

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
        _in = input('''Please choose an option [e/d/a/q]:\ne) Encrypt some text\nd) Decrypt some text\na) Automatically decrypt English text\nq) Quit\n''')

        if _in == 'e':
            x = input("Please enter some text to encrypt: ")
            y = input("Please enter a shift offset (1-25): ")
            try:
                y = int(y)
            except:
                print("please check offset")
            if y == 0:
                print("The encrypted text is: ")
                for i in range(1,26):
                    print('%2d: ' %i,encrypt(x, i))
                print('')
            else:
                print("The encrypted text is: ", encrypt(x, y), '\n')


        elif _in == 'd':
            x = input("Please enter some text to decrypt: ")
            y = input("Please enter a shift offset (1-25): ")
            try:
                y = int(y)
            except:
                print("please check offset")
            if y == 0:
                print("The decrypted text is: ")
                for i in range(1,26):
                    print('%2d: ' %i,decrypt(x, i))
                print('')
                
            else:
                print('The decrypted text is: ',decrypt(x, y), '\n')

        elif _in == 'a':
            x = input("Please enter some encrypted text: ")
            x = x.strip()
            res = ﬁnd_encryption_offsets(x)
            if len(res) == 0:
                print("No valid encryption offset", '\n')
            elif len(res) == 1:
                print("Encryption offset: ", res[0])
                print("Decrypted message: ", decrypt(x, res[0]))
            else:
                print("Multiple encryption offsets: ", end = ", ")
                for i in res :
                    print(i, end=' ')
                print('')
            
        elif _in == 'q':
            print("Bye!")
            break
        else:
            print("Invalid command")
    

if __name__ == '__main__':
    main()

