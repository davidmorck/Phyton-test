def km_miles(dist):
    nMiles = dist * 1.609
    print(dist, "km motsvarar", nMiles, "miles")

def miles_km(dist):
    nKm = dist * 0.621
    print(dist, "miles motsvarar", nKm, "km")

anvDist = input("Ange en distans i km eller miles> ")

anvChar = len(anvDist) - 1

anvInt = anvDist.split(" ") 

if (anvDist[anvChar] == "m"):
    km_miles(int(anvInt[0]))

if (anvDist[anvChar] == "s"):
    miles_km(int(anvInt[0]))
