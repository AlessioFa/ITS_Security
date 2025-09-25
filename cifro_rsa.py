# Modulo RSA in esadecimale
n = """
00be93ab15c6aacbd87217be979929dc93a3f5e3f28bd7184cadc475b28ddef07539aec6be4d526191d7e06a49fad82b752bf4a60d7b645583149caa
b044bcec8139e7ca0a16533b750ea257ee30beb09c1df8e398c6904ec4f74bd9809940c7b3f35f2130565869e525990b31cd5b9fc58341a234177f62
2742b88f01e01da54e150940ca4f9fe5bd6935e456396fd9ec3a52881962578b6880876e39ecc72f07e36fa7db70276224fe8ff5db8a95d895f5b239
c2bf412db9c835524b46f53d2d4f40e133bbc4c3e12c4514d444888aa78545bafd0efc1cf4f52938af12c9cf618881da65a6cdc8b60f0cd682c59baf0
7a1eee677bb0beb4b04bd886f744e08c03
"""

# Rimuovo spazi e newline
modulo_hex = n.replace("\n", "").replace(" ", "")

# Converto da esadecimale a intero
modulus_int = int(modulo_hex, 16)

# Esponente pubblico
e = 3

# Messaggio da cifrare
m = "Ciao, come va...?"

# Converto la stringa in numero intero
mi = int(M.encode('utf-8').hex(), 16)

# Cifratura RSA: C = M^e mod n
c = pow(mi, e, modulus_int)

# Stampa il risultato
print(c)