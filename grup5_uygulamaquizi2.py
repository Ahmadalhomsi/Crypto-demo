# QUIZ 2

# Grup 5

# 210201140
# Ahmad Alhomsi

# 210201126
# Ebrar Mustafa AÇIKYOL

# 210201120
# Cem Korkmaz

# FSR

import os
import random

# AES

# AES S-box
s_box = [
    # 0     1    2    3    4    5    6    7    8    9    A    B    C    D    E    F
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
]

# Round constant
Rcon = [0x01]

def rot_word(word):
    return word[1:] + word[:1]

def sub_word(word):
    return [s_box[b] for b in word]

def xor_words(a, b):
    return [x ^ y for x, y in zip(a, b)]

def aes128_one_round_key_expansion(key):
    assert len(key) == 16  # 128-bit key
    w = [list(key[i:i+4]) for i in range(0, 16, 4)]  # 4 words

    for i in range(4, 8):
        temp = w[i-1]
        if i % 4 == 0:
            temp = xor_words(sub_word(rot_word(temp)), [Rcon[(i//4)-1], 0, 0, 0])
        w.append(xor_words(w[i-4], temp))

    round1_key = b''.join(bytes(word) for word in w[4:8])
    return round1_key




def number_to_binary(number: int, bit_number: int) -> str:
    b = format(number, "b")
    return b.zfill(bit_number)


def binary_to_number(binary_str: str) -> int:
    if not all(c in "01" for c in binary_str):
        raise ValueError("binary_str must contain only '0' or '1'")
    return int(binary_str, 2)


def hex_to_number(hex_str: str) -> int:
    s = hex_str.strip()
    if s.lower().startswith('0x'):
        s = s[2:]

    if not all(c in '0123456789abcdefABCDEF' for c in s):
        raise ValueError("hex_str must be a valid hexadecimal string")
    return int(s, 16)


def main():
    print("Quiz 2 - Grup 5")
    print("Enter your a:")
    # a = input() #
    a = "10101010101010101010010101010101010101010100001010110010101010010101001010100101001010010101001010101001010010010101100101001100"
    print("Enter your b:")
    b = "10101010101010101000111100011101010101010000101011001010101001010100101010010100101001010100101010100101001001010110010100110011"
    print("Enter your c1:")
    c1 = "2b7e151628aed2a6abf7158809cf4f3c"
    print("Enter your c2:")
    c2 = "2b7e151655aed2a6abf7158809cf4ffb"

    a_parts = []
    temp = ""
    for i in range(0, 128):
        temp = temp + a[i]
        print(i)
        if i % 8 == 0 and i != 0:
            # print(i)
            a_parts.append(temp)
            temp = ""

    a_parts.append(temp)

    print("A parts:")
    print(a_parts)

    b_parts = []
    temp = ""
    for i in range(0, 128):
        temp = temp + a[i]
        if i % 8 == 0 and i != 0:
            print("TEST")
            b_parts.append(temp)
            temp = ""

    b_parts.append(temp)

    print("B parts:")
    print(b_parts)

    temp1 = binary_to_number(a_parts[0]) ^ binary_to_number(a_parts[1])
    temp2 = ~binary_to_number(a_parts[8])
    temp3 = temp1 ^ temp2
    temp4 = temp3 ^ binary_to_number(a_parts[0])

    a_parts.insert(15, number_to_binary(temp4, 8)[1:8])
    print("New")
    print(a_parts)

    a0 = binary_to_number(a_parts[0])
    a_parts.pop(0)

    tempb1 = binary_to_number(b_parts[0]) ^ binary_to_number(b_parts[3])
    tempb2 = ~binary_to_number(b_parts[8])
    tempb3 = tempb1 ^ tempb2
    tempb4 = a0 ^ tempb3

    b_parts.insert(15, number_to_binary(tempb4, 8)[1:8])
    b_parts.pop(0)

    print(len(a_parts))
    print(len(b_parts))

    t1_temp = b_parts[8:16]
    t2_temp = a_parts[0:8]

    print("-----------------")

    print(t1_temp)
    print(t2_temp)

    t1 = ""
    t2 = ""

    t1 = t1_temp + t1_temp
    t2 = t2_temp + t2_temp

    print("+++++++++++++++++++++")

    print(t1)
    print(t2)

    # for i in range(0,8):

    r1 = "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"

    # modular_toplama = r1 + t1

    t1_total = ""
    t2_total = ""

    for i in range(0, 16):
        t1_total = t1_total + t1[i]
        t2_total = t2_total + t2[i]

    print("iiiiiiiiiiiiiiiiiiiii")
    print(t1_total)
    print(t2_total)

    # print("Before modular")
    # print(r1)
    # print(t1)

    modular_toplama_temp = binary_to_number(r1) + binary_to_number(t1_total)
    # print(modular_toplama_temp)

    modular_toplama = number_to_binary(modular_toplama_temp, 128)

    print("Modular toplama:")
    print(modular_toplama)
    
    # Example input key (16 bytes)
    cipher_key = bytes.fromhex(c1)
    round_key = aes128_one_round_key_expansion(cipher_key)
    print("Round 1 Key:", round_key.hex())
    r2 = round_key.hex()
    
    cipher_key = bytes.fromhex(r2)
    round_key = aes128_one_round_key_expansion(cipher_key)
    print("Round 2 Key:", round_key.hex())
    r3 = round_key.hex()
    
    x = binary_to_number(t2_total) ^ hex_to_number(r3)
    print("X:")
    print(x)
    
    modular_toplama2 = hex_to_number(r2) + x
    print("Modular Toplama2:")
    print(modular_toplama2)

    fsm = 19 ^ modular_toplama2
    print("FSM:")
    print(fsm)
    fsm2 = number_to_binary(fsm,128)
    print("FSM2:")
    print(fsm2)
    
    modular_toplama3 = number_to_binary(binary_to_number(fsm2) + binary_to_number(t1_total),128)
    print("MOdular 3")
    print(modular_toplama3)
    
    z = number_to_binary(hex_to_number(r2) ^ binary_to_number(modular_toplama3),128)
    print("Z:")
    print(z)


if __name__ == "__main__":
    main()
