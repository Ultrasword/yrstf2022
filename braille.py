reference = {
    'a': [1, 0, 0, 0, 0, 0],
    'b': [1, 1, 0, 0, 0, 0],
    'c': [1, 0, 0, 1, 0, 0],
    'd': [1, 0, 0, 1, 1, 0],
    'e': [1, 0, 0, 0, 1, 0],
    'f': [1, 1, 0, 1, 0, 0],
    'g': [1, 1, 0, 1, 1, 0],
    'h': [1, 1, 0, 0, 1, 0],
    'i': [0, 1, 0, 1, 0, 0],
    'j': [0, 1, 0, 1, 1, 0],

    'k': [1, 0, 1, 0, 0, 0],
    'l': [1, 1, 1, 0, 0, 0],
    'm': [1, 0, 1, 1, 0, 0],
    'n': [1, 0, 1, 1, 1, 0],
    'o': [1, 0, 1, 0, 1, 0],
    'p': [1, 1, 1, 1, 0, 0],
    'q': [1, 1, 1, 1, 1, 0],
    'r': [1, 1, 1, 0, 1, 0],
    's': [0, 1, 1, 1, 0, 0],
    't': [0, 1, 1, 1, 1, 0],

    'u': [1, 0, 1, 0, 0, 1],
    'v': [1, 1, 1, 0, 0, 1],
    'w': [0, 1, 0, 1, 1, 1],
    'x': [1, 0, 1, 1, 0, 1],
    'y': [1, 0, 1, 1, 1, 1],
    'z': [1, 0, 1, 0, 1, 1],

    '1': [1, 0, 0, 0, 0, 0],
    '2': [1, 1, 0, 0, 0, 0],
    '3': [1, 0, 0, 1, 0, 0],
    '4': [1, 0, 0, 1, 1, 0],
    '5': [1, 0, 0, 0, 1, 0],
    '6': [1, 1, 0, 1, 0, 0],
    '7': [1, 1, 0, 1, 1, 0],
    '8': [1, 1, 0, 0, 1, 0],
    '9': [0, 1, 0, 1, 0, 0],
    '0': [0, 1, 0, 1, 1, 0],

    " ": [0, 0, 0, 0, 0, 0]
}

ALLOWED_CHARS = "abcdefghijklmnopqrstuvwxyz1234567890 "

def print_braille(input_chars: str) -> None:
    for char in input_chars:
        braille = reference[char]
        print(str(braille[0]) + " " + str(braille[3]))
        print(str(braille[1]) + " " + str(braille[4]))
        print(str(braille[2]) + " " + str(braille[5]))
        print(" ")

def clean_string(input_string: str) -> str:
    lowered = input_string.lower()
    split_string = [*lowered]
    for pk, char in enumerate(split_string):
        if char not in ALLOWED_CHARS:
            split_string.pop(pk)
    print(split_string)
    return "".join(split_string)

print_braille(clean_string(input("text: ")))