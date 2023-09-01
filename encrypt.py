text = input('Enter a text that you want to encrypt: ')
key = int(input('Enter a key for encrypt: '))

result = ''

for letter in text:
    if letter == ' ':
        result += ' '
    elif letter.isupper():
        enc_letter = chr((int(ord(letter)) + key - 65) % 26 + 65)
        result += str(enc_letter)
    elif letter.islower():
        enc_letter = chr((int(ord(letter)) + key - 97) % 26 + 97)
        result += str(enc_letter)
    elif letter.isdigit():
        enc_letter = chr((int(ord(letter)) + key - 48) % 10 + 48)
        result += str(enc_letter)
    else:
        result += str(letter)

print(result)