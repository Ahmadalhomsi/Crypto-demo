import struct

def right_rotate(value, bits):
    return ((value >> bits) | (value << (32 - bits))) & 0xFFFFFFFF

def simple_sha256(message):
    print("=== SIMPLIFIED SHA-256 ===")
    # Convert message to binary and pad
    message = bytearray(message, 'ascii')
    original_length = len(message) * 8
    message.append(0x80)  # add 1 bit (10000000)

    while (len(message) * 8 + 64) % 512 != 0:
        message.append(0x00)

    message += struct.pack('>Q', original_length)

    # Initial hash values (first 8 primes' square roots)
    h = [
        0x6a09e667, 0xbb67ae85,
        0x3c6ef372, 0xa54ff53a,
        0x510e527f, 0x9b05688c,
        0x1f83d9ab, 0x5be0cd19
    ]

    # Round constants (first 32 bits of primes' cube roots)
    k = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf,
        0xe9b5dba5, 0x3956c25b, 0x59f111f1,
        0x923f82a4, 0xab1c5ed5
    ]

    for chunk_offset in range(0, len(message), 64):
        w = list(struct.unpack('>16L', message[chunk_offset:chunk_offset+64]))
        w += [0] * (64 - 16)

        for i in range(16, 64):
            s0 = right_rotate(w[i-15], 7) ^ right_rotate(w[i-15], 18) ^ (w[i-15] >> 3)
            s1 = right_rotate(w[i-2], 17) ^ right_rotate(w[i-2], 19) ^ (w[i-2] >> 10)
            w[i] = (w[i-16] + s0 + w[i-7] + s1) & 0xFFFFFFFF

        a, b, c, d, e, f, g, h_temp = h

        for i in range(8):  # simplified: only 8 rounds
            S1 = right_rotate(e, 6) ^ right_rotate(e, 11) ^ right_rotate(e, 25)
            ch = (e & f) ^ ((~e) & g)
            temp1 = (h_temp + S1 + ch + k[i] + w[i]) & 0xFFFFFFFF
            S0 = right_rotate(a, 2) ^ right_rotate(a, 13) ^ right_rotate(a, 22)
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = (S0 + maj) & 0xFFFFFFFF

            h_temp = g
            g = f
            f = e
            e = (d + temp1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & 0xFFFFFFFF

        h = [(x + y) & 0xFFFFFFFF for x, y in zip(h, [a, b, c, d, e, f, g, h_temp])]

    digest = ''.join(f'{value:08x}' for value in h)
    print(f"Digest: {digest}\n")

simple_sha256("abc")
