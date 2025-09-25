import sys
import random 

"""
-- Summary of this exercise --

1. Import the libraries.
2. Check that the user has given a file to modify.
3. Read the whole file into memory.
4. Choose a random position (a byte).
5. Choose a random bit inside that byte.
6. Use XOR to flip the value of that bit.
7. Rebuild the file with the modified byte.
8. Overwrite the file.
9. Print a message with the details of the change.
"""

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <file name>")
    sys.exit(1)

# devo leggere tutto il file
data = None

with open(sys.argv[1], "rb") as f:
    data = f.read()

# prendo un byte casuale del file
pos = random.randint(0, len(data) -1)

# prendo un bit casuale del byte

bit = random.randint(0,7)

# ora devo cambiare il valore del bit <bit> di data[pos] (uso lo xor)
# in sostanza devo costruire un byte di tutti 0 e un solo 1 nel posto giusto 

byte = data[pos]

byte = byte ^ (1 << bit) # ho rovesciato il bit bit - esimo del byte 

data = data[:pos] + bytes([byte]) + data[pos+1:]

with open(sys.argv[1], "wb") as f:
    f.write(data)

print(f"Modicato il bit {bit} al posto {pos} nel file {sys.arg[1]}")
