alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'


def encrypt(plaintext, k):
    newWord = ""
    for i in plaintext:
       index2 = alphabet.index(i) 
       newLetter = alphabet[index2 + 26 - k]
       newWord = newWord + newLetter

    return newWord

print(encrypt(plaintext, k))
      


