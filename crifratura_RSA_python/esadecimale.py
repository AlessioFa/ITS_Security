# -----------------------------
# Parametri RSA
# -----------------------------

# Modulo RSA (n) in esadecimale, generato con il comando openssl rsa -in FAprivkey.pem -noout -text
modulo_esadecimale = "00b56495d00d5a0e68f2493219cc2c34c42c164b05d68c7c1fdba751677a58e61b9efa55de523041bc4b959c501b0aa92fd40a990ee6a0d75e88b0411afd04ee867c687eb2e34c158f2e8182c76401b4408ed6dff8a4c8546e058d769371bb1f7c351a6dc5d8cea9a0929dcb1471604dd4336a5ed854a0920b1c7bc1f490d1132c0b0acad7e2fb4a4661342d046b9e96339985a0b855609f846b4b3d06ace923549accddb0f0e171bb7dafbd764ce82f0857f915c17717d180f0a6b9ddd88ab3f499f2cdd906f81d28874f82d7126c8b1e56de1851b397423b38de50f45b141969fe9ef028a8c6cc7da9101cacfc47277d088d0e561b70bcafd5d5a93b2a63ef03"

# Conversione del modulo in intero
modulo = int(modulo_esadecimale, 16)
print(f"Questo è il modulo: {modulo}")

# Messaggio da cifrare
messaggio_testo = "Che bello Python!"

# Conversione del messaggio in intero usando codifica UTF-8 e rappresentazione esadecimale
messaggio_intero = int(messaggio_testo.encode("utf-8").hex(), 16)

# Esponente pubblico per la cifratura (tipicamente 3 o 65537)
esponente_pubblico = 3

# -----------------------------
# Cifratura RSA
# -----------------------------

# Cifratura: c = m^e mod n
messaggio_cifrato = pow(messaggio_intero, esponente_pubblico, modulo)

print("Messaggio cifrato:", messaggio_cifrato)

# -----------------------------
# Chiave privata RSA
# -----------------------------

# Esponente privato (d) in esadecimale, generato con openssl
esponente_privato_esadecimale = "1e3b6e4d578f0266d30c33044cb208cb5cae61d64e6cbf5aa49be2e694642659efd463a50db2b59f61ee44b80481c6dd4e01c42d267023e516c80ad9d4d627c114bc151dd08cae4287c0407690aaf36017ce7aa970cc0e1256423e6de849da94b38467a0f977c6f0186fa1d8bd900cf8b33c65240e1ac301da14a0536d782ddc645a128e0be5784dcf69c848689ed940a1ed820fb6e0ea7db9d2395344800a01eb42752cef680fb92b5fde98eb2879d1851dcd4a8e17e15e1d991c75eeddfd7a567614216b9e95c09851303304edd7039b01afcf1b59e54f915948eb3d163ee337e3a1db0358dca7bf3c123da130190efc07e3777893ed0a443a502e62c42a07"

# Conversione dell'esponente privato in intero
esponente_privato = int(esponente_privato_esadecimale, 16)

# -----------------------------
# Decifratura RSA
# -----------------------------

# Decifratura: m = c^d mod n
messaggio_decifrato_intero = pow(messaggio_cifrato, esponente_privato, modulo)
print("Messaggio decifrato (intero):", messaggio_decifrato_intero)

# Conversione dell'intero decifrato in byte
lunghezza_byte = (messaggio_decifrato_intero.bit_length() + 7) // 8
messaggio_decifrato_bytes = messaggio_decifrato_intero.to_bytes(lunghezza_byte, 'big')

# Conversione da byte a stringa UTF-8
messaggio_originale = messaggio_decifrato_bytes.decode('utf-8')

print("Messaggio originale:", messaggio_originale)





#openssl genrsa -out FApubkey.pem -3 2048
##openssl genrsa -out FAprivkey.pem -3 2048