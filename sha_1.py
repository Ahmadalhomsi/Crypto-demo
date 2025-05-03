import struct

def left_rotate(value, bits):
    return ((value << bits) | (value >> (32 - bits))) & 0xFFFFFFFF

def simple_sha1(message):
    print("=== SIMPLIFIED SHA-1 ===")
    # Convert message to binary and pad
    message = bytearray(message, 'ascii')
    original_length = len(message) * 8
    message.append(0x80)  # add 1 bit (10000000)
    
    while (len(message) * 8 + 64) % 512 != 0:
        message.append(0x00)
    
    message += struct.pack('>Q', original_length)
    
    # Initial hash values
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0
    
    for chunk_offset in range(0, len(message), 64):
        chunk = message[chunk_offset:chunk_offset+64]
        
        # Break chunk into sixteen 32-bit big-endian words
        w = list(struct.unpack('>16L', chunk))
        
        # Extend the sixteen 32-bit words into eighty 32-bit words
        for i in range(16, 80):
            w.append(left_rotate(w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16], 1))
        
        # Initialize hash value for this chunk
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
        
        # Main loop
        for i in range(80):
            if 0 <= i <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6
            
            temp = (left_rotate(a, 5) + f + e + k + w[i]) & 0xFFFFFFFF
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp
        
        # Add this chunk's hash to result
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF
    
    # Produce the final hash value as a 160-bit number (40 hex digits)
    digest = '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)
    print(f"Digest: {digest}\n")

# Test the implementation
simple_sha1("abc")