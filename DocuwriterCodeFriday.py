# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 09:33:27 2024

@author: owen.merrill
"""

import json

def main():
    keepGoing = True
    while keepGoing == True:
        selection = getMenuChoice()
        if selection == "0" :
            keepGoing = False
        elif selection == "1" :
            activeGame = getDefaultGame()
        elif selection == "2" :
            activeGame = loadGame()
        elif selection == "3" :
            saveGame(activeGame)
        elif selection == "4" :
            editNode(activeNode)
        elif selection == "5" :
            playGame(activeGame)
        else:
            print("Please input a valid response")

def getMenuChoice():
    print("""
      0) exit
      1) load default game
      2) load a game file
      3) save the current game
      4) edit or add a node
      5) play the current game
    """)
    selection = input("Please input the number that corresponds to your choice: ")
    return selection


def playGame(activeGame):
    game = activeGame
    inGame = True
    activeNode = "start"
    while(inGame == True):
        if activeNode == "quit":
            inGame = False
        else:
            activeNode = playNode(activeNode, game)


def playNode(activeNode, game):
    (description, menu1, node1, menu2, node2) = game[activeNode]

    print(f"""
          {description}
          1. {menu1}
          2. {menu2}
          """)
    choice = input("please type the number that corresponds to your desired course of action: ")
    if choice == "1":
        activeNode = node1
    elif choice == "2":
        activeNode = node2
    else:
        print("Improper input. Please try again.")
    return(activeNode)

def getDefaultGame():
    activeGame = {"start": ["Do you win or lose?", "win", "start", "Lose", "quit"]}
    print("Game Loaded")
    return(activeGame)

def saveGame(activeGame):
    outFile = open("game.json", "w")
    json.dump(activeGame, outFile, indent=2)
    outFile.close()
    print("Game Saved")


def loadGame():
    inFile = open("game.json", "r")
    activeGame = json.load(inFile)
    print("Data loaded.")
    return (activeGame)

def editNode(activeGame):
    for key in  activeGame.keys():
            print(f"  {key}")
    selection = input("input the node would you like to edit: ")
    if selection in activeGame.keys:
    	newNode = activeGame[selection]
    else:
        newNode = ["","","","",""]
    (description, menu1, node1, menu2, node2) = newNode
    newDescription = editField("description", description)
    newMenu1 = editField("menu1", menu1)
    newNode1 = editField("node1", node1)
    newMenu2 = editField("menu2", menu2)
    newNode2 = editField("node2", node2)
    activeGame[newNode] = [newDescription, newMenu1, newNode1, newMenu2, newNode2,]
    return(activeGame)

def editField(prompt, curentValue):
    print (prompt, curentValue)
    edits = input("please enter the new value")
    if edits == "":
    	edits = curentValue
    print("Saved")
    return edits

main()