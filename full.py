import struct

# SHA-1 implementation from scratch
def sha1(message: bytes) -> bytes:
    def left_rotate(n, b):
        return ((n << b) | (n >> (32 - b))) & 0xffffffff

    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    original_len_in_bits = len(message) * 8
    message += b'\x80'
    while (len(message) * 8) % 512 != 448:
        message += b'\x00'
    message += struct.pack('>Q', original_len_in_bits)

    for i in range(0, len(message), 64):
        w = list(struct.unpack('>16L', message[i:i+64]))
        for j in range(16, 80):
            w.append(left_rotate(w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16], 1))

        a, b, c, d, e = h0, h1, h2, h3, h4

        for j in range(80):
            if 0 <= j <= 19:
                f = (b & c) | (~b & d)
                k = 0x5A827999
            elif 20 <= j <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= j <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (left_rotate(a, 5) + f + e + k + w[j]) & 0xffffffff
            a, b, c, d, e = temp, a, left_rotate(b, 30), c, d

        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff

    return struct.pack('>5L', h0, h1, h2, h3, h4)

# Convert SHA-1 hash (bytes) to an integer
def sha1_to_int(data: bytes) -> int:
    hash_bytes = sha1(data)
    return int.from_bytes(hash_bytes, byteorder='big')

# Simulation parameters
BIT_LENGTH = 160
MAX_POOL_VALUE = 2 ** BIT_LENGTH - 1
target_threshold = MAX_POOL_VALUE // 2  # e.g., half full
pool_value = 0
counter = 0

print("Simulating Crypto Pool using SHA-1 faucet...\n")

# Faucet: keep adding until the pool reaches threshold
while pool_value < target_threshold:
    input_data = f"faucet-{counter}".encode()
    hash_val = sha1_to_int(input_data)
    pool_value += hash_val
    pool_value = min(pool_value, MAX_POOL_VALUE)
    print(f"Step {counter}: Hash = {hash_val}, Pool = {pool_value}")
    counter += 1

print(f"\n✅ Pool reached target in {counter} SHA-1 additions.")
