codice1 = "AFCDDR-CF-2020"
codice2 = "SEDTYR-XC-2019"
controllaCodice = codice1[10:], codice2[10:]
print(controllaCodice)
for codice in controllaCodice:
    if codice == "2020":
        print("Il codice è valido")
    else:
        print("Il codice non è valido")