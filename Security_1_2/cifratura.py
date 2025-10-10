# conversione 
m = "Ciao"
mi = int(m.encode("utf-8").hex(), 16)
print(mi)

# convertiamo ogni carattere in esadecimale usando la funzione ord()
# ord() restituisce il codice ASCII di un carattere
hex_string = "".join([hex(ord(c))[2:] for c in my_string])

# Stampa il risultato
print("Stringa originale:", my_string)
print("Stringa in esadecimale:", hex_string)

