import time
import os
import sys
from Items_List import Currency
from Characters import Logos_and_Characters
from Items_List import Guns
from Detroit_Map import District_One
from Items_List import ItemsList
from Restaurants import The_Game_Beery
from Restaurants import Jamals

# Pls dont cancel me also these are the values/lists
GameLoop = True
menu = True
play = False
Credits = False
Enemies = 0
Equipped_Weapon = "Placeholer"



def clear():
  os.system('cls')



def Goofy_ah_Menu():
  clear()

  print(Logos_and_Characters['Detroit']), '\n', print("<-------------------------------------------------->")
  print("Travel"), '\n', print("Inventory"), '\n', print("Menu")



def Inventory():
  clear()
  """Inventory Function. (Kinda) works"""
  play = False
  print(Logos_and_Characters['Inventory']), '\n', print("<-------------------------------------------------->")
  print("Cash:"),print(Currency['Money'])

  for items in ItemsList:
    print(f"\n-> {items}")
  
  print("\n Equip | Type 'back' to return to game menu")

  InventoryOption = input("|>")

  if InventoryOption.lower() == ("back"):
    play = True

    clear()
  elif InventoryOption.lower() == ('amongus gun'):
    """I apologize for the horrendous looking code but this is the equip feature for the amongus gun"""
    if Guns['Amongus Gun']['Equipped'] == False and Guns['Amongus Gun']['Owned'] == True:
        
        Guns['Amongus Gun']['Equipped'] = True 
        Guns['Goofy Gun']['Equipped'] = False
        Guns["Indian's Profession"]['Equipped'] = False

        print("Equipped Amongus Gun!")

        time.sleep(2)
    else:
      print("You can't equip this item")

      time.sleep(2)

      

def traveling():
  """Travelling guide"""
  clear()
  play = False
  print(Logos_and_Characters['Travel']), '\n', print("<-------------------------------------------------->")
  print("\nDistrict One"), '\n', print("The Game Beery"), '\n', print("Jamals"), '\n', print("Back")

  traveloption = input("|>")
  if traveloption.lower() == ('district one'):
    District_One()
  elif traveloption.lower() == ('the game beery'):
    clear()
    The_Game_Beery()
  elif traveloption.lower() == ('jamals'):
    clear()
    Jamals()
  elif traveloption.lower() == ("back"):
    clear()
    play = True



#Game loop
while GameLoop:
  while menu == True:
    """Menu screen"""
    print(Logos_and_Characters['MainLogo'])
    print("<-------------------------------------------------------------->")
    print("PLAY"), '\n', print("Credits"), '\n', print("Quit")
    print("<-------------------------------------------------------------->")

    option = input("|> ")
    if option.lower() == ('play'):
      play = True
      menu = False

    elif option.lower() == ('credits'):
      Credits = True
      menu = False

    elif option.lower() == ('quit'):
      quit()

    else:
      clear()
      continue



  while Credits == True:

    """Hall Of Shame: The Dahoodimon Developers (ULTRAKILL REFERENCE!) """
    clear()
    print(Logos_and_Characters['Credits'])
    print("\nj7jhj - the god of Gen Alpha (aka the developer)")
    print("\n\t-- THE LIST --"), '\n', print("Arth - Ideas"), '\n', print("MrMix - Ideas")
    print("\ntype 'menu' to return to the menu")

    creditoption = input("|> ")
    if creditoption.lower() == ('menu'):
      clear()
      menu = True
      Credits = False



  while play == True:

    """The while loop for the entire game! May the brainrot begin"""

    Goofy_ah_Menu()
    MenuInput = input("|>")

    if MenuInput.lower() == ('inventory'):
      Inventory()

    elif MenuInput.lower() == ('menu'):
      play = False
      menu = True
      clear()
    
    elif MenuInput.lower() == ('travel'):
      traveling()
      
    



