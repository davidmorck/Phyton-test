def km_miles(dist):
    nMiles = dist * 1.609
    print(dist, "km motsvarar", nMiles, "miles")

def miles_km(dist):
    nKm = dist * 0.621
    print(dist, "miles motsvarar", nKm, "km")

anvDist = input("Ange en distans i km eller miles> ")

numChar = len(anvDist) - 1

if (anvDist[numChar] == "m"):
    km_miles(anvDist)
