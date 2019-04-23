import requests
url = "http://77.238.56.27/examples/numinfo/?integer="

jämt= input("Ange ett jämnt tal> ")

urlInt = url + str(jämt)
print (urlInt)
r = requests.get(urlInt)

response_dictionary = r.json()

if(int(jämt) %2 == 0):
    print(response_dictionary)
else:
    print("Talet är inte jämnt")
    