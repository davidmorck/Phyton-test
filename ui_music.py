import requests
import ui
artists = []

idUrl = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"

artistsArr = requests.get(idUrl)
artistJson = artistsArr.json()["artists"]

for artist in artistJson:
    artists.append(artist["name"])

while True != False:
    ui.line(True)
    ui.header("Välkommen till artist-wiki")
    ui.line(True)

    nummer = 0
    for art in artists:
        ui.echo(art + " ----- " + str(nummer))
        nummer +=1
    u_inp = ui.prompt("Ange en artists nummer eller 'exit' om du vill avsluta programmet> ")
    if "exit" in u_inp.lower():
        break
    else:
        try:

            a_artist = int(u_inp)

            ui.line()
            ui.echo("Du har valt " + artists[a_artist])

            dinArtist = artistJson[a_artist]["id"]

            getIdUrl = idUrl + dinArtist

            artArr = requests.get(getIdUrl)
            artJson = artArr.json()["artist"]

            artGenre = artJson["genres"]
            artY = artJson["years_active"]
            artM = artJson["members"]
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
        except:
            print("Invalid input")
        input("Tryck enter för att fortsätta")
        ui.clear()