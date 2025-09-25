"""
-- Summary of this exrcise --

1. Take a phrase.
2. Convert each character into its ASCII code.
3. Apply XOR with a fixed number (57 in this case). This is the 4. encryption step.
5. Apply XOR with the same number again to decrypt.
6. Convert the ASCII codes back into characters.
7. Join the characters to rebuild the original phrase.
"""

phrase: str = "Nel mezzo del cammin di nostra vita"

# Step 1: Convert each character to its ASCII code
phrase_into_ascii = [ord(char) for char in phrase]

print(phrase)  # Original phrase
print(phrase_into_ascii)  # ASCII codes

# Step 2: Apply XOR with 57
xor_cifrated_phrase = [char ^ 57 for char in phrase_into_ascii]
print(xor_cifrated_phrase)  # XOR encrypted values

# Step 3: Decrypt with XOR again
decifrated = [num ^ 57 for num in xor_cifrated_phrase]
print(decifrated)  # Decrypted ASCII codes

# Step 4: Convert ASCII codes back to characters
decifrated_phrase = [chr(num) for num in decifrated]
print(decifrated_phrase)  # List of characters

# Step 5: Join the characters into a string
correct_decifrated_phrase = "".join(decifrated_phrase)
print(correct_decifrated_phrase)  # Final decrypted phrase
