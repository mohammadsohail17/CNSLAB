import struct
import math

def md5(message):
    # Initialize variables
    a0 = 0x67452301
    b0 = 0xEFCDAB89
    c0 = 0x98BADCFE
    d0 = 0x10325476

    # Constants for MD5
    s = [ 7, 12, 17, 22, 5, 9, 14, 20, 4, 11, 16, 23, 6, 10, 15, 21 ]

    # Initialize variables for each round
    A, B, C, D = a0, b0, c0, d0

    # Helper functions
    def F(X, Y, Z):
        return (X & Y) | (~X & Z)

    def G(X, Y, Z):
        return (X & Z) | (Y & ~Z)

    def H(X, Y, Z):
        return X ^ Y ^ Z

    def I(X, Y, Z):
        return Y ^ (X | ~Z)

    # Function to perform a left circular shift
    def left_rotate(x, c):
        return (x << c) | (x >> (32 - c))

    # Padding the message
    original_byte_len = len(message)
    original_bit_len = original_byte_len * 8
    message += b'\x80'
    while (len(message) + 8) % 64 != 0:
        message += b'\x00'
    message += struct.pack('<Q', original_bit_len)

    # Process in 512-bit blocks
    for i in range(0, len(message), 64):
        block = message[i:i + 64]
        words = [struct.unpack('<I', block[j:j+4])[0] for j in range(0, 64, 4)]

        # Initialize hash value for this block
        A1, B1, C1, D1 = A, B, C, D

        # Main loop
        for j in range(64):
            if 0 <= j <= 15:
                F_result = F(B1, C1, D1)
                g = j
            elif 16 <= j <= 31:
                F_result = G(B1, C1, D1)
                g = (5 * j + 1) % 16
            elif 32 <= j <= 47:
                F_result = H(B1, C1, D1)
                g = (3 * j + 5) % 16
            elif 48 <= j <= 63:
                F_result = I(B1, C1, D1)
                g = (7 * j) % 16

            F_result = (F_result + A1 + words[g] + int(math.pow(2, 32) * abs(math.sin(j + 1)))) & 0xFFFFFFFF
            A1, B1, C1, D1 = D1, (B1 + left_rotate(F_result, s[j % 4])) & 0xFFFFFFFF, B1, C1

        # Update overall hash value
        A = (A + A1) & 0xFFFFFFFF
        B = (B + B1) & 0xFFFFFFFF
        C = (C + C1) & 0xFFFFFFFF
        D = (D + D1) & 0xFFFFFFFF

    # Combine the hash parts into a single hash value
    hash_value = (A << 96) | (B << 64) | (C << 32) | D

    # Return the hex representation of the hash value
    return '{:032x}'.format(hash_value)

# Example usage
message = b"Hello, world!"
hashed_message = md5(message)
print("MD5:", hashed_message)