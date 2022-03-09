SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_char_index(char, alphabet):
    char_index = alphabet.find(char)
    return char_index


def is_int(ph):
    try:
        int(ph)
        return True
    except ValueError:
        return False


def encryption_caesar():
    phrase = str(input("Enter your phrase:")).upper()
    k = int(input("Enter K (from 1 to 25):"))

    r_letters = SYMBOLS[k:] + SYMBOLS[:k]
    result = []

    for char in phrase:
        index = get_char_index(char, SYMBOLS)
        encrypted_char = r_letters[index] if index >= 0 else char
        result.append(encrypted_char)
    return ''.join(result)
