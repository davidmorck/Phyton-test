import requests

artists = ["Ariana Grande",
"Avicii",
"Blink -182",
"Brad Paisley",
"Ed Sheeran",
"Imagine Dragons",
"Maroon 5",
"Scorpions"]

idUrl = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"

artistsArr = requests.get(idUrl)
artistJson = artistsArr.json()
artisterArr = artistJson["artists"]

nummer = 0

for art in artists:
    print(art + " ----- " + str(nummer))


    nummer +=1

a_artist = int(input("Ange en artists nummer> "))

print("")
print("-----------------------")
print ("Du har valt " + artists[a_artist])

dinArtist = artisterArr[a_artist]
dinArtistId = dinArtist["id"]

getIdUrl = idUrl + dinArtistId

artArr = requests.get(getIdUrl)
artJson = artArr.json()
artJsonObj = artJson["artist"]

artGenre = artJsonObj["genres"]
artY = artJsonObj["years_active"]
artM = artJsonObj["members"]
artArray = [artGenre,artY,artM]
typeOfData = ["Genre:", "Active Years:", "Members:"]

num1 = 0
print("-----------------------")

for j in artArray:
    print(typeOfData[num1])

    for i in j:
        print(i.capitalize())
    
    print("")
    num1 += 1

