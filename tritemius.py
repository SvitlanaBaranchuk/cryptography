SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_char_index(char, alphabet):
    char_index = alphabet.find(char)
    return char_index


def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


def encryption_lineal():
    phrase = str(input("Enter your phrase:")).upper()
    result = []
    A = int(input("Enter A:"))
    B = int(input("Enter B:"))

    p = 0
    for char in phrase:
        x = get_char_index(char, SYMBOLS)
        K = A*p + B
        y = (x + K)%26 if x >= 0 else char
        result.append(SYMBOLS[y]) if is_int(y) else result.append(" ")
        p += 1
    return ''.join(result)


def decryption_lineal():
    e_phrase = str(input("Enter your encryption phrase:")).upper()
    d_phrase = str(input("Enter your decryption phrase:")).upper()
    B = get_char_index(d_phrase[0], SYMBOLS) - get_char_index(e_phrase[0],SYMBOLS)
    A = get_char_index(d_phrase[1], SYMBOLS) - get_char_index(e_phrase[1],
SYMBOLS) - B
    print("A - ", A)
    print("B - ", B)


def encryption_sq():
    phrase = str(input("Enter your phrase:")).upper()
    result = []
    A = int(input("Enter A:"))
    B = int(input("Enter B:"))
    C = int(input("Enter C:"))

    p = 0
    for char in phrase:
        x = get_char_index(char, SYMBOLS)
        K = A * p * p + B * p + C
        y = (x + K) % 26 if x >= 0 else char
        if is_int(y):
            result.append(SYMBOLS[y])
        else:
            result.append(char)
            p = p - 1
        p += 1
    return ''.join(result)


def decryption_sq():
    phrase = str(input("Enter your phrase:")).upper()
    result = []

    p = 0
    for A in range(1, 6):
        for B in range(1, 6):
            for C in range(1, 6):
                for char in phrase:
                    y = get_char_index(char, SYMBOLS)
                    K = (A * p * p + B * p + C) % 26
                    x = (y - K)%26 if y >= 0 else char

                    if is_int(x):
                        result.append(SYMBOLS[x])
                    else:
                        result.append(char)
                        p = p - 1
                    p += 1

                print(A, B, C, ''.join(result))
                result = []
                p = 0