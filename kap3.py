#3.1
male = ["Erik", "Lars", "Karl", "Anders", "Johan"]
female = ["Maria", "Anna", "Margareta", "Elisabeth", "Eva", "Tyra"]

numFem = len(female) - 1
numMale = len(male) - 1

print (male[0])
print (female[2])
print (female[numFem])
print (male[1])

a =(input("Ditt namn:"))
gender = int(input("Vilken av listorna vill du bli tillagd i? skriv 1 för man och 2 För kvinna"))
if gender == 1:
    male.append(a)
    genderName = "Male"
else: 
    female.append(a)
    genderName = "Female"
print("Namnet",a, "är tillagt i", genderName+"-listan")

#3.2
