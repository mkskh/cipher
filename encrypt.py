text = input('Enter a text that you want to encrypt: ')
key = int(input('Enter a key for encrypt: '))

result = ''

for letter in text:
    if letter == ' ':
        result += ' '
    elif letter.isupper():
        enc_letter_up = chr((int(ord(letter)) + key - 65) % 26 + 65)
        result += str(enc_letter_up)
    else:
        enc_letter_lo = chr((int(ord(letter)) + key - 97) % 26 + 97)
        result += str(enc_letter_lo)

print(result)