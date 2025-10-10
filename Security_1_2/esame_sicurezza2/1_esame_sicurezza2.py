"""
Crittografia

Sia dato il messaggio cifrato (convertito in numero intero in base 10): 
204751668535
Il messaggio cifrato è stato ottenuto cifrando il messaggio originale con algoritmo RSA senza padding con n=514948966453 e esponente pubblico (e) pari a 3
Provare a decifrare il messaggio cifrato
NB: il messaggio originale è una parola di cinque lettere maiuscole e minuscole.
NB: Quando il problema sembra arduo, allora un approccio brutale potrebbe essere quello vincente.
"""

# messaggio cifrato
c: int = 204751668535

# modulo RSA utilizzato per cifrare il testo originale
n: int = 514948966453

# esponente pubblico
e: int = 3

# cerco un fattore primo di n provando tutti i numeri da due fino a n ** 0.5
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        p = i

        break

# calcolo il fattore primo q
q = n // p


print(f"Fattore primo p: {p}")
print(f"Fattore primo q: {q}")


# calcolo phi
phi = (p - 1) * (q - 1)

# calcolo della chiave privata per decifrare il messaggio
d = pow(e, -1, phi)

# ottengo m come numero intero
m = pow(c, d, n)


# funzione per trasformare un numero intero in byte
def intero_in_byte(num):
    # calcolo quanti byte servono per rappresentare il numero
    lunghezza = (num.bit_length() + 7) // 8

    # converto il numero in una sequenza di byte
    return num.to_bytes(lunghezza, 'big')


m_in_bytes = intero_in_byte(m)

# converto i byte in stringa
messaggio_decifrato = m_in_bytes.decode('utf-8')

print(f"Messaggio originale: {messaggio_decifrato}")
