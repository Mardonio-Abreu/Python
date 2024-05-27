alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'


def encrypt(plaintext, k):
    newWord = ""
    for i in plaintext:
       index2 = alphabet.index(i) 
       newLetter = alphabet[index2 + 26 - k]
       newWord = newWord + newLetter

    return newWord

plaintext = "kyvtrmrcipnzccrkkrtbwifdkyvefikynvjkrkeffe"

for k in range(0, 26):
    print(encrypt(plaintext, k), k)
      


