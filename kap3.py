male = ["Erik", "Lars", "Karl", "Anders", "Johan"]
female = ["Maria", "Anna", "Margareta", "Elisabeth", "Eva", "Tyra"]

numFem = len(female) - 1 #ger en siffra på hur många namn som finns i female respektiva male
numMale = len(male) - 1 

print (male[0])
print (female[2])
print (female[numFem])
print (male[1])

del male [1+2]
del female [0]

male.sort()
female.sort()

namn =(input("Ditt namn:"))
gender = int(input("Vilken av listorna vill du bli tillagd i? skriv 1 för man och 2 För kvinna"))
if gender == 1:
    male.append(namn)
    genderName = "Male"
else: 
    female.append(namn)
    genderName = "Female"
print("Namnet",namn, "är tillagt i", genderName+"-listan")

male.sort()
female.sort()

print("Fullständiga namnlistor:")
print(male)
print(female)

delName = input("vilket namn vill du ta bort från listan?")
if delName == 0:
    print("inget namn borttaget")
elif delName in male:
    male.remove(delName)
    print (delName, "har blivit borttaget från listan Male")
elif delName in female:
    female.remove(delName)
    print (delName, "har blivit borttaget från listan Female")
else: print("Namnet du angav finns inte i någon av listorna")