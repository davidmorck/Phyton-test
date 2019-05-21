numAnv = int(input("Ange multiplikationstabell> "))

numEx = 0
numMax = 3

while numEx < numMax:
    numMult = numEx + 1
    print(numMult * numAnv)
    numEx += 1
    if (numMax == numMult):
        anvSvar = input("Fortsätt?> ").lower()
        if (anvSvar == "ja"):
            numMax += 3
            continue
