import json
from coder import get_alphabet, make_split, make_glue, decode, poly_decode

def read_table():
    table = {}
    with open('freq.txt') as f:
        code = f.read()

    for line in code.split('\n'):
        letter, freq = line.rstrip('%').split('\t')
        table[letter] = float(freq) / 100

    return table


def count(text, alphabet):
    result = {}
    N = 0

    for s in alphabet:
        result[s] = 0

    for s in text:
        if s in alphabet:
            N += 1
            result[s] += 1

    for k in result:
        result[k] /= N

    return result


def guess_key(text, table, alphabet):
    text_freq = count(text, alphabet)

    A = list(map(lambda x: x[0], sorted(text_freq.items(), key=lambda x: x[1])))
    B = list(map(lambda x: x[0], sorted(table.items(), key=lambda x: x[1])))

    return dict(zip(B, A))


def guess_keys(text, num, table, alphabet):
    parts = make_split(text, num)
    keys = [guess_key(part, table, alphabet) for part in parts]
    return keys

"""
with open('cipher.txt') as f:
    cipher = f.read()

table = read_table()
alphabet = get_alphabet()

key = guess_key(cipher, table, alphabet)
print("Key:", json.dumps(key))

print(decode(cipher, key))
"""

with open('poly_cipher.txt') as f:
    cipher = f.read()

table = read_table()
alphabet = get_alphabet()

keys = guess_keys(cipher, 3, table, alphabet)
print("Key:", json.dumps(keys))
print(poly_decode(cipher, keys))
