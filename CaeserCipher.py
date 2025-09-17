def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Example
msg = "Hello World!"
enc = caesar_encrypt(msg, 3)
dec = caesar_decrypt(enc, 3)

print("Encrypted:", enc)
print("Decrypted:", dec)
