import os

def line(bubb = False):
    if bubb == True:
        print("*******************************")
    else:
        print("-------------------------------")

def header(text):
    lenght = 30 - len(text)
    space = lenght/2
    spaceRound = round(space)
    edTex = "|"
    for i in range(1,spaceRound):
        edTex = edTex + " "
    edTex = edTex + text
    for i in range(1,spaceRound):
        edTex = edTex + " "
    edTex = edTex + "|"
    print(edTex)

def echo(text):
    print("| "+text)

def prompt(text):
    userIn = input(text)
    return(userIn)

def clear():
    clear = lambda: os.system('cls')
    clear()
