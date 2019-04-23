namn = ["Daniel Radcliffe", "Rupert Grint", "Emma Watson", "Selena Gomez"]
kön = ["man", "man", "kvinna", "kvinna"]
ögon = ["brun","blå","brun","brun"]
hår = ["brun","röd","brun","brun"]
rättnamn=[]

Akön = input("ange kön> ")
Ahårfärg = input("ange hårfärg> ")
Aögonfärg = input("ange ögonfärg> ")

Akön = Akön.lower()
Ahårfärg = Ahårfärg.lower()
Aögonfärg = Aögonfärg.lower()

namnVar = 0
antalnamn = len(namn)

while (namnVar<antalnamn):
    if (Akön == kön[namnVar]and Aögonfärg == ögon[namnVar] and Ahårfärg == hår[namnVar]):
        rättnamn.append(namn[namnVar])
    namnVar+=1

if(len(rättnamn)!=0):
    print("Du liknar:",rättnamn)
else:
    print("Du liknar ingen kändis.")