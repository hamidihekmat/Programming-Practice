# 'secret message'

alpha = "abcdefghijklmnopqrstuvwxyz"


def encrypt(clearText):
    cyphertext = ""
    for char in clearText:
        if char in alpha:
            newpos = (alpha.find(char) + 14) % 26
            cyphertext += alpha[newpos]
        else:
            cyphertext += char
    return cyphertext


def decrypt(cyphertext):
    cleartext = ""
    for char in cyphertext:
        if char in alpha:
            newpos = (alpha.find(char) - 14) % 26
        else:
            cleartext += char
    return cleartext


cleartext = input('Clear text: ')

print(decrypt(cleartext))
