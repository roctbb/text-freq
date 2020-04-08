import random
import json

def get_alphabet():
    start = ord('a')
    end = ord('z')

    alphabet = ''

    for i in range(start, end + 1):
        alphabet += chr(i)

    return alphabet

def generate_key(alphabet):

    target_alphabet = list(alphabet)
    random.shuffle(target_alphabet)

    return dict(zip(list(alphabet), target_alphabet))


def encode(text, key):
    result = ''

    for s in text.lower():
        if s in key.keys():
            result += key[s]
        else:
            result += s

    return result

def make_split(text, num):
    parts = [""] * num

    for i in range(len(text)):
        parts[ i % num ] += text[i]

    return parts

def make_glue(parts):
    result = ""

    i = 0
    while True:
        part = parts[i % len(parts)]

        if part == "":
            break

        result += part[0]
        parts[i % len(parts)] = part[1:]

        i += 1

    return result

def poly_encode(text, keys):
    parts = make_split(text, len(keys))

    for i in range(len(keys)):
        parts[i] = encode(parts[i], keys[i])

    return make_glue(parts)

def poly_decode(text, keys):
    parts = make_split(text, len(keys))

    for i in range(len(keys)):
        parts[i] = decode(parts[i], keys[i])

    return make_glue(parts)


def decode(text, key):
    reversed_key = {v: k for k, v in key.items()}
    result = ''

    for s in text.lower():
        if s in reversed_key.keys():
            result += reversed_key[s]
        else:
            result += s

    return result


alphabet = get_alphabet()
"""
with open('open_text.txt') as f:
    text = f.read()

key = generate_key(alphabet)
print("Key:", json.dumps(key))

cipher = encode(text, key)
with open('cipher.txt', 'w') as f:
    f.write(cipher)
"""

with open('open_text.txt') as f:
    text = f.read()

keys = [generate_key(alphabet) for i in range(3)]
cipher = poly_encode(text, keys)

with open('poly_cipher.txt', 'w') as f:
    f.write(cipher)




