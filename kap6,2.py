import requests
vUrl= "https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/"

Astad= input("Ange stad> ")

checkStad = [
    "stockholm",
    "göteborg",
    "malmö",
    "uppsala",
    "västerås"
]
if Astad in checkStad:
    stadUrl = vUrl + Astad
    resp = requests.get(stadUrl)
    väderRes = resp.json()
    väder = väderRes["forecasts"]
    antalV = len(väder)
    for j in väder:
        print("on",j["date"],"the weather will be" , j["forecast"])
else:
    print("staden finns inte med")

