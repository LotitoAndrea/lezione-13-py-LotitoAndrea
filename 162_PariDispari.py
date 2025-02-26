stringa = input("Inserisci una stringa: ")
for i in range(len(stringa)):
    if i % 2 == 0:
        print(stringa[i], end=" ")
    else:
        print("", end="")
print("\n")
for i in range(len(stringa)):
    if i % 2 != 0:
        print(stringa[i], end=" ")
    else:
        print("", end="")