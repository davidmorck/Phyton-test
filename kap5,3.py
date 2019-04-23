
norden = ["danmark", "finland", "island", "norge", "sverige"]
stor = ["england", "nordirland", "skottland", "wales"]

land = (input("Ange ett land för att få reda på om det tillhör Norden eller Stoprbrittanien> ").lower())

if land in norden:
    print (land.capitalize(),"Tillhör norden")
elif land in stor:
    print (land.capitalize(),"Tillhör Storbrittanien")
else:
    print("Landet tillhör varken Norden eller Storbrittanien")