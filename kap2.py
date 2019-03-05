import math
#2.1
citat ="datatyper har inbyggda metoder "

print ( citat.upper() )

#2.2
dataIn = float(input("Skriv in ett decimaltal:"))

print("talet avrundas till: ")
print(round(dataIn))

#2.3
print("Hej! Vad heter du?")
för = input("Förnamn:")
efter = input("Efternamn:")
print("Hej",för,efter)

#2.4
ålder = int(input("Hur gammal är du? "))
skillnad = 18-ålder
if ålder > 18:
    print("Du är myndig")

else:
    print("Du är myndig om",skillnad, "år")

#2.5
print("hur många elever vill ha...")
tvåKorv = int(input("Två vanliga korvar?"))
treKorv = int(input("Tre vanliga korvar?"))
tvåvegan = int(input("Två vegankorvar?"))
trevegan = int(input("Tre vegankorvar?"))

antalKorv = tvåKorv*2 + treKorv*3 
antalvegan = tvåvegan*2 + trevegan*3
antalElever = tvåKorv+treKorv+tvåvegan+trevegan

korvförpackning = antalKorv/8
veganförpackning = antalvegan/4

prisKorv = math.ceil(korvförpackning) * 20.95
prisvegan = math.ceil(veganförpackning) * 34.95
prisDricka = antalElever * 13.95
totPris = prisDricka + prisKorv + prisvegan

print("dryck:",antalElever)
print("korv:",antalvegan)
print("vegan:",antalKorv)
print("totalkostnad:", totPris,"kr")
