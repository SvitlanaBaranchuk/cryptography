SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def vigenere_encrypt():
    phrase = input("Enter phrase: ").upper()
    phrase = ''.join(phrase.split())
    key = input("Enter key: ").upper()
    result = ''

    for i in range(len(phrase)):
        letter_index = SYMBOLS.index(phrase[i])  # позиція літери з фрази у SYMBOLS
        key_index = SYMBOLS.index(key[i % len(key)])  # позиція літери з ключа у SYMBOLS

        value = (letter_index + key_index) % len(SYMBOLS)

        result += SYMBOLS[value]

    return result


def vigenere_decrypt():
    phrase = input("Enter phrase: ").upper()
    phrase = ''.join(phrase.split())
    key = input("Enter key: ").upper()
    result = ''

    for i in range(len(phrase)):
        letter_index = SYMBOLS.index(phrase[i])
        key_index = SYMBOLS.index(key[i % len(key)])

        value = (letter_index - key_index) % len(SYMBOLS)

        result += SYMBOLS[value]

    return result


print(vigenere_encrypt())



