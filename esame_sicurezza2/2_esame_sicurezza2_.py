from Crypto.Util.number import inverse

"""
Premessa: nell'RSA, per calcolare con python l'esponente privato nota la chave pubblica e noti i due numeri primi p e q, si utilizza la sequente funzione
d = inverse(e, phi) dove ph = (p-1)*(q-1).

Sia dato n (pari a p*q) = 51151902024533551
e siano
e (esponente pubblico) = 3
C=10002041662569686 il messaggio cifrato (l'originale è una parola di sette caratteri alfanumerici)
Decifrare il messaggio
NB: un attacco forza bruta su 7 caratteri ha un costo computazionale pari a 62^6 = 56.800.235.584 (infattibile in python)
NB: ma n=p*q e quindi se riuscissi a trovare i due numeri primi che fattorizzano n, allora potrei applicare euclide inverso (la funzione inverse) per trovare la chiave privata...
"""
# messaggio crifrato
c = 10002041662569686

# modulo RSA utilizzato per cifrare il messaggio originale 
n = 51151902024533551

# esponente pubblico
e = 3

# cerco un fattore primo di n 
for i in range(2, int(n ** 0.5)+1):
    if n % i == 0:
        p = i

        break

# calcolo il fattore primo di q
q = n // p

print(f"Fattore primo p: {p}")
print(f"Fattore primo q: {q}\n")

# calcolo di phi
phi = (p-1)*(q-1)

# calcolo la chiave privata d come inverso di e modulo phi
d = inverse(e, phi)
print(f"Chiave privata d: {d}\n")


# funzione per trasformare un numero intero in byte
def intero_in_byte(num):
    # calcolo quanti byte servono per rappresentare il numero
    lunghezza = (num.bit_length() + 7) // 8
    # converto il numero in una sequenza di byte
    return num.to_bytes(lunghezza, 'big')


# calcolo m come numero intero
m = pow(c, d, n)

# converto il numero in byte
m_bytes = intero_in_byte(m) 

# converto i byte in stringa
messaggio_decifrato = m_bytes.decode('utf-8')

print(f"Messaggio decifrato: {messaggio_decifrato}")
