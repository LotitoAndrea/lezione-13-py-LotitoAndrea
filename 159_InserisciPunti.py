stringa = input("inserisci una stringa: ")
for i in range(len(stringa)):
    for j in range(i):
        print("", end=".")
    print(stringa[i], end="")