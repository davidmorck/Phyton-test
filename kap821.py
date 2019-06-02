import requests

def get(url):
    resp = requests.get(url)
    reJson = resp.json()
    return(reJson)