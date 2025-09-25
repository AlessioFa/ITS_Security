from Crypto.Cipher import AES
import base64

"""
-- Summary of this exercise --

This program demonstrates AES encryption and decryption in ECB mode.

1. AES is a symmetric encryption algorithm: the same key is used for encrypting and decrypting.
2. The text and key are padded to be multiples of 16 bytes.
3. Encryption: convert text to bytes, encrypt with AES, then encode in Base64.
4. Decryption: decode Base64, decrypt with AES, then remove padding.
5. Optional brute-force section demonstrates testing combinations to find a key.
"""

"""
-- Virtual Environment Setup --

I created a virtual environment (venv) inside the project folder to isolate this project.
All required libraries, like PyCryptodome, are installed inside this environment.
This ensures that the code runs correctly without conflicting with other Python projects.
The virtual environment is ignored by Git, so it won't be uploaded to GitHub.
"""


# Function to pad the message to be multiple of 16 bytes
def pad(text):
    while len(text) % 16 != 0:
        text += " "
    return text


# Encryption
def encrypt(plain_text, key):
    cipher = AES.new(pad(key).encode("utf-8"), AES.MODE_ECB)
    encrypted_text = cipher.encrypt(pad(plain_text).encode("utf-8"))

    return base64.b64encode(encrypted_text).decode("utf-8")


# Decryption
def decrypt(encrypted_text, key):
    cipher = AES.new(pad(key).encode("utf-8"), AES.MODE_ECB)
    decrypted_text = cipher.decrypt(base64.b64decode(encrypted_text)).decode("utf-8").strip()

    return decrypted_text


# ------------------------
# Example usage
# ------------------------
key = "ThisIsASecretKey"  # 16 characters
plain_text = "0"

encrypted_text = encrypt(plain_text, key)
decrypted_text = decrypt(encrypted_text, key)

print("Originale: ", plain_text)
print("Cifrato  : ", encrypted_text)
print("Decifrato: ", decrypted_text)

# ------------------------
# Optional brute-force section
# ------------------------
# Uncomment the section below to try brute-force decryption
"""
enc = "OgJuOYJZT0FDb47DBOkNg=="
for p1 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
    for p2 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for p3 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            for p4 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                key_try = p1 + p2 + p3 + p4 + "IsASecretKey"
                try:
                    dec = decrypt(enc, key_try)
                    print("La chiave è:", key_try, "e la stringa è:", dec)
                except:
                    continue
"""
