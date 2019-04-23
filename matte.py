import requests

url = "https://nokflex.nok.se//api/solution/assignment/"

assign = input("Ange uppgiftsnummer: ")

assUrl = url+ assign

respAss = requests.get(assUrl)

json = respAss.json()

print(json)