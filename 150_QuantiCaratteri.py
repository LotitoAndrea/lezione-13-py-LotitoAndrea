stringa = input("inserisci una stringa: ")
carattereDaCercare = input("inserisci un carattere: ")
caratteri = 0
for i in range(len(stringa)):
    if stringa[i] == carattereDaCercare:
        caratteri += 1
print("Il carattere", carattereDaCercare, "è presente", caratteri, "volte")