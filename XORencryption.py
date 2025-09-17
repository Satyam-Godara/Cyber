def xor_encrypt_decrypt(text, key):
    return ''.join(chr(ord(c) ^ key) for c in text)

msg = "CyberSec123"
key = 5
enc = xor_encrypt_decrypt(msg, key)
dec = xor_encrypt_decrypt(enc, key)

print("Encrypted:", enc.encode())  # show bytes
print("Decrypted:", dec)
