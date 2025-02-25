import random

nome = input("inserisci il tuo nome: ")
cognome = input("inserisci il tuo cognome: ")
numeriRandom = ""
for i in range(2):
    numeriRandom += str(random.randint(0, 9))
password = nome + numeriRandom + cognome
print("La tua password è:", password)