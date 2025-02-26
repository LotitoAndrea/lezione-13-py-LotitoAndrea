stringa1 = input("inserisci una stringa: ").lower()
vocali = "aeiou"
stringa2 = stringa1
for vocale in vocali:
    stringa2 = stringa2.replace(vocale, "*")
print("La stringa originale è:", stringa1)
print("La stringa modificata è:", stringa2)