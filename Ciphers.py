# This file includes functions to encipher and decipher messages using the Ceaser shift, Keyword shift and Vigenere ciphers
# The cipher functions take a key and the plaintext and return the ciphertext (all uppercase) and the cipher_decode functions take the key and ciphertext and return the plaintext (all lowercase)

# Ceasar shift
# Each letter of the message is shifted along k places in the alphabet
def ceaser(k, message):
    messageList = list(message)
    final = []
    for char in messageList:
        asciiVal = ord(char.lower())
        if 97 <= asciiVal <= 122:
            final.append(chr((asciiVal + k - 97) % 26 + 65))
        else:
            final.append(char)
    return ''.join(final)

# Ceasar shift decode
def ceaser_decode(k, message):
    messageList = list(message)
    final = []
    for char in messageList:
        asciiVal = ord(char.lower())
        if 97 <= asciiVal <= 122:
            final.append(chr((asciiVal - k - 97) % 26 + 97))
        else:
            final.append(char)
    return ''.join(final)



# Keyword shift
# Letters of the alphabet are paired with those in a new keyAlphabet which is created by listing the letters of the keyword followed by the remaining letters of the alphabet in order
def keyword(keyword, message):
    keyAlphabet = []
    for char in list(keyword):
        if ord(char.lower()) not in keyAlphabet:
            keyAlphabet.append(ord(char.lower()))
    for i in range(97, 123):
        if i not in keyAlphabet:
            keyAlphabet.append(i)
    final = []
    for char in list(message):
        asciiVal = ord(char.lower())
        if 97 <= asciiVal <= 122:
            final.append( chr( keyAlphabet[ asciiVal - 97 ] - 32) )
        else:
            final.append(char)
    return ''.join(final)

# Keyword shift decode
def keyword_decode(keyword, message):
    keyAlphabet = []
    for char in list(keyword):
        if ord(char.lower()) not in keyAlphabet:
            keyAlphabet.append(ord(char.lower()))
    for i in range(97, 123):
        if i not in keyAlphabet:
            keyAlphabet.append(i)
    final = []
    for char in list(message):
        asciiVal = ord(char.lower())
        if 97 <= asciiVal <= 122:
            final.append( chr( keyAlphabet.index( asciiVal ) + 97) )
        else:
            final.append(char)
    return ''.join(final)



# Vigenere cipher
# This cipher pairs the letters of the message with those of the keyword (repeated to be the same length as the message) and sums their positions in the alphabet to generate the ciphertext
def vigenere(keyword, message):
    charList = [ord(char.lower()) - 97 for char in list(message)]
    for num in charList:
        if not 0 <= num <= 26:
            charList.remove(num)
    keyAlphabet = [ord(list(keyword)[i % len(keyword)]) - 97 for i in range(len(charList))]
    final = []
    i = 0
    for char in list(message):
        asciiVal = ord(char.lower())
        if 97 <= asciiVal <= 122:
            final.append( chr( ( (charList[i] + keyAlphabet[i] ) % 26) + 65) )
            i += 1
        else:
            final.append(char)
    return ''.join(final)

# Vigenere cipher decode
def vigenere_decode(keyword, message):
    charList = [ord(char.lower()) - 97 for char in list(message)]
    for num in charList:
        if not 0 <= num <= 26:
            charList.remove(num)
    keyAlphabet = [ord(list(keyword)[i % len(keyword)]) - 97 for i in range(len(charList))]
    final = []
    i = 0
    for char in list(message):
        asciiVal = ord(char.lower())
        if 97 <= asciiVal <= 122:
            final.append( chr( ( (charList[i] - keyAlphabet[i] ) % 26) + 97) )
            i += 1
        else:
            final.append(char)
    return ''.join(final)

