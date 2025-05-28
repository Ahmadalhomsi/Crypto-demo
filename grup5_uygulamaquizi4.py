# QUIZ 4

# Grup 5

# 210201140
# Ahmad Alhomsi

# 210201126
# Ebrar Mustafa AÇIKYOL

# 210201120
# Cem Korkmaz


import os
import random

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

import hashlib

def sha1_hash(text: str) -> str:
    # Encode the input string to bytes
    encoded_text = text.encode('utf-8')
    
    # Create a SHA-1 hash object and update it with the encoded text
    hash_object = hashlib.sha1(encoded_text)
    
    # Return the hexadecimal digest
    return hash_object.hexdigest()

# ------------
# main

def main():
    print("Quiz 4 - Grup 5")
    print("X saat giriniz:")
    x = int(input())
    # 2D array 160-bit
    a_havuzu = [None] * x
    for i in range(x):
        print("Metni Giriniz:")
        text = input()
        # hashing text with sha1
        hash_result = number_to_binary(hex_to_number(sha1_hash(text)),160)
        print(f"SHA-1 Hash: {hash_result}")
        print(len(hash_result))
        a_havuzu[i] = hash_result
        
    print("Havuzdaki degerler: ")
    for i in range(x):
        print(a_havuzu[i])
        
    # length of a_havuz
    print("Havuzdaki deger sayisi: ")
    print(len(a_havuzu))
    print("Havuzdaki degerlerin bit sayisi: ")
    print(len(a_havuzu[0]))
          

    # print("Aktarilacak bitler: ")
    # for bit in range(len(aktarilacak_bitler)):
    #     print(aktarilacak_bitler[bit])
    
    print("Y saat giriniz:")
    y = int(input())
    b_havuzu = [None] * (y+1)

    counter = 159
    for i in range(y+1):
        print("Metni Giriniz:")
        text = input()
        # hashing text sha1
        hash_result = number_to_binary(hex_to_number(sha1_hash(text)),160)
        print(f"SHA-1 Hash: {hash_result}")
        print(len(hash_result))
        
        a_havuzu[len(a_havuzu) - 1] = hash_result
        
        print("bit sayisi: ")
        bitSayisi = int(input())
        print("QQQQ:", i)
        bitSayisi2 = bitSayisi / 160
        bitSayisiInt = int(bitSayisi2)
        print(f"Bit sayisi bolum kismi: {bitSayisiInt}")
        kalan = bitSayisi2 - bitSayisiInt
        print(f"Bit sayisi kalan kismi: {kalan}")

        aktarilacak_bitler = []
        for j in range(bitSayisi):  
            aktarilacak_bitler.append(a_havuzu[0][counter])
            counter -= 1

        aktarilacak_bitler_str = ''.join(aktarilacak_bitler)
        print("Aktarilacak bitler string: ")
        print(aktarilacak_bitler_str)

        hash_result = number_to_binary(hex_to_number(sha1_hash(aktarilacak_bitler_str)), 160)
        print(f"SHA-1 Hash of aktarilacak_bitler: {hash_result}")

        print("b_havuzu degerleri: ")
        print(b_havuzu)

        hash_result = hash_result[::-1]
        b_havuzu[i] = hash_result  


    

if __name__ == "__main__":
    main()
