text = 'No hxu nuc gxk eua'     # This is 'Hi bro how are you'



for key in range(1, 27):
    result = ''
    for letter in text:
        if letter == ' ':
            result += ' '
        elif letter.isupper():
            enc_letter = chr((int(ord(letter)) - key - 65) % 26 + 65)
            result += str(enc_letter)
        elif letter.islower():
            enc_letter = chr((int(ord(letter)) - key - 97) % 26 + 97)
            result += str(enc_letter)
        elif letter.isdigit():
            enc_letter = chr((int(ord(letter)) - key - 48) % 10 + 48)
            result += str(enc_letter)
        else:
            result += str(letter)
    print('Hacking key', str(key) + ':', result)