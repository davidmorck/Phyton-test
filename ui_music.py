import requests
import ui
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
ui.line(True)
ui.header("Välkommen till artist-wiki")
ui.line(True)

for art in artists:
    ui.echo(art + " ----- " + str(nummer))


    nummer +=1

a_artist = int(ui.prompt("Ange en artists nummer> "))

ui.line()
ui.echo("Du har valt " + artists[a_artist])

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
ui.line()

for j in artArray:
    ui.echo(typeOfData[num1])

    for i in j:
        ui.echo(i.capitalize())
    ui.line()
    num1 += 1

