import struct


def sha1(message):
    #initialize variable 32 bits each
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    original_byte_len=len(message)
    original_bit_len=original_byte_len*8
    #adding 128 bits in the last
    message+=b'\x80'
    while((len(message)+8)%64!=0):
        message+=b'\x00'
    # Append the original message length in bits as a 64-bit big-endian integer
    
    message+=struct.pack('>Q',original_bit_len)

    for i in range(0,len(message),64):
        block=message[i:i+64]
        words=[struct.unpack('>I',block[j:j+4])[0] for j in range(0,64,4)]
        for j in range(16,80):
            words.append(((words[j-3]^words[j-8]^words[j-14]^words[j-16])<<1)|((words[j-3]^words[j-8]^words[j-14]^words[j-16])>>31))
        a,b,c,d,e=h0,h1,h2,h3,h4
        #80 rounds
        for j in range(80):
            #first 20 rounds
            if j<=19:
                f=(b&c)|((~b)&d)
                k=0x5A827999
            #next 20 rounds
            elif 20<=j<=39:
                f=b^c^d
                k=0x6ED9EBA1
            elif 40<=j<=59:
                f=(b&c)|(b&d)|(c&d)
                k=0x8F1BBCDC
            elif 60<=j<=79:
                f=b^c^d
                k=0xCA62C1D6
            temp=((a<<5)|(a>>27))+f+e+k+words[j]&0xFFFFFFFF
            e,d,c,b,a=d,c,(b<<30)|(b>>2),a,temp

        #update the values  
        h0=(h0+a)&0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF
    hash_value=(h0<<128)|(h1<<96)|(h2<<64)|(h3<<32)|h4

    return '{:040x}'.format(hash_value)
    #return format(hash_value, '040b')
message = b"Hello, world!"
hashed_message = sha1(message)
print("SHA-1:", hashed_message)
            