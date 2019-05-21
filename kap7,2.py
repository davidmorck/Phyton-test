import random

randVar = random.randint(0,100)
numGiss = 0
correct = False

print("~~~HÖGRE-LÄGRESPELET~~~")
print("Välkommen till högre-lägrespelet")
print("Datorn kommer slumpa en siffra mellan 0-100 och du ska försöka gissa rätt på så få gissningar som möjligt.")
print("----------------------------------------------------------------------------------------------------------")
while (correct == False):
    anvVar = int(input("Din gissning: "))
    numGiss += 1
    if (anvVar == randVar):
        print("Grattis, du gissade rätt. Svaret var", randVar, ".")
        print("Det tog dig", numGiss, "gissningar.")
        correct = True
        break

    if (anvVar<randVar):
        print("Talet är högre, försök igen.")
        print()
    if (anvVar>randVar):
        print("Talet är lägre, försök igen.")
        print()




