# Diffie-Hellman key exchange example

"""
-- Summary of this exercise --

This program demonstrates the Diffie-Hellman key exchange.

1. Two participants, Alice and Bob, choose their private secret numbers.
2. They calculate public keys using a public prime number and a generator.
3. They exchange public keys.
4. Each participant calculates a shared secret key using the other’s public key and their own private secret.
5. The shared key is the same for both, without sending the private numbers.
"""

p = 23  # public prime number
g = 5   # public base (generator)

# Each participant chooses a secret number
a = int(input("Enter Alice's secret (a): "))
b = int(input("Enter Bob's secret (b): "))

# Compute public keys
A = (g ** a) % p
B = (g ** b) % p

# Compute the shared secret key
alice_key = (B ** a) % p
bob_key = (A ** b) % p

# Show results
print("Alice's public key:", A)
print("Bob's public key:", B)
print("Key calculated by Alice:", alice_key)
print("Key calculated by Bob:", bob_key)
print("Shared key:", alice_key if alice_key == bob_key else "Error")
