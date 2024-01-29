from Characters import Logos_and_Characters
from Items_List import Currency
from Items_List import Food
from Items_List import ItemsList
import time

# All the restaraunts in the game
def The_Game_Beery():
    """The Game Beery: But hey, thats just a beery, a GAME BEERY, thanks for drinking!"""
    print(Logos_and_Characters['Game Beery']), '\n', print("<----------------------------------------------------------------------------->")
    print("MENU: (30 Money) The Last Beery | (20 Money) FNAF Lore Drop | (80 Money) Thats just a beery, a GAME BEERY!")
    print("<----------------------------------------------------------------------------->")

    Game_Beery_option = input("|>")
    if Game_Beery_option.lower() == ("the last beery") and Currency['Money'] >= 30:
        Food['The Last Beery']['Amount Owned'] += 1
        Currency['Money'] -= 30

        if Food['The Last Beery'] in ItemsList:
            print("'Added The Last Beery in inventory")
        else:
            ItemsList.append(Food['The Last Beery'])

        print(f"You've recieved one 'The Last Beery' drink! | Current balance: {Currency['Money']}")

        time.sleep(3)
    elif Game_Beery_option.lower() == ("fnaf lore drop") and Currency['Money'] >= 20:
        Food['FNAF Lore Drop']['Amount Owned'] += 1
        Currency['Money'] -= 20

        if Food['FNAF Lore Drop'] in ItemsList:
            print("'Added FNAF Lore Drop in inventory")
        else:
            ItemsList.append(Food['FNAF Lore Drop'])

        print(f"You've recieved one 'FNAF Lore Drop' drink! | Current balance: {Currency['Money']}")

        time.sleep(3)
    elif Game_Beery_option.lower() == ("thats just a beery, a game beery") and Currency['Money'] >= 80:
        Food['Thats Just A BEERY, A GAME BEERY!']['Amount Owned'] += 1
        Currency['Money'] -= 80

        if Food['Thats Just A BEERY, A GAME BEERY!'] in ItemsList:
            print("'Added Thats Just A BEERY, A GAME BEERY! in inventory")
        else:
            ItemsList.append(Food['Thats Just A BEERY, A GAME BEERY!'])

        print(f"You've recieved one 'Thats Just A BEERY, A GAME BEERY!' drink! | Current balance: {Currency['Money']}")

        time.sleep(3)
    else:
        print("you dont have any money")

        time.sleep(3)



def Jamals():
    """Jamal Inc. Get delicious treats!"""
    print(Logos_and_Characters['Jamals']), '\n', print("<----------------------------------------------------------------------------->")
    print("MENU: (32 Money) Jamanut The Donut | ( 15 Money) Johannes The Cookie")
    print("<----------------------------------------------------------------------------->")

    Jamal_option = input("|>")
    """Jamanut the Donut  + Johannes Cookie"""
    if Jamal_option.lower() == ("jamanut the donut") and Currency['Money'] >= 32:
        Food['Jamanut The Donut']['Amount Owned'] += 1
        Currency['Money'] -= 32

        if Food['Jamanut The Donut'] in ItemsList:
            print("'Added Jamanut Donut in inventory")
        else:
            ItemsList.append(Food['Jamanut The Donut'])

        print(f"You've recieved one 'Jamanut The Donut'! | Current balance: {Currency['Money']}")
        
        time.sleep(3)
    elif Jamal_option.lower() == ("johannes the cookie") and Currency['Money'] >= 15:
        Food['Johannes The Cookie']['Amount Owned'] += 1
        Currency['Money'] -= 15

        if Food['Johannes The Cookie'] in ItemsList:
            print("'Added Johannes The Cookie in inventory")
        else:
            ItemsList.append(Food['Johannes The Cookie'])

        print(f"You've recieved one 'Johannes The Cookie'! | Current balance: {Currency['Money']}")

        time.sleep(3)
    else:
        print("you dont have any money")

        time.sleep(3)
