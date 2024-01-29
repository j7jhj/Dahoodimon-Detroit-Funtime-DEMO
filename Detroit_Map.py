from Items_List import Guns
from Gang_Members import Enemies
import os 
from collections import Counter

def District_One():
    """District One"""
    def Trevor_Attack_Menu():
        """Battle Menu"""
        os.system('cls')
        print(Enemies['Trevor']['Name']), '\n', print(f"Special Move:", Enemies['Trevor']['Special_Move']), '\n', print(f"HP:", Enemies['Trevor']['HP'])
        print("\nAttack")

        OptionInput = input("|>")
        if OptionInput.lower() == ('attack') and Guns['Amongus Gun']['Equipped'] == True:

            Enemies['Trevor']['HP'] -= Guns['Amongus Gun']['Damage']           
        elif OptionInput.lower() == ('attack') and Guns['Goofy Gun']['Equipped'] == True:
            
            Enemies['Trevor']['HP'] -= Guns['Goofy Gun']['Damage'] 
        elif Guns["Indian's Profession"]['Equipped'] == True:
            
            Enemies['Trevor']['HP'] -= Guns["Indian's Profession"]['Damage'] 


    print("######### DISTRICT ONE #########"), '\n', print("raid"), '\n', print("leave")

    station1_option = input("|>")

    while Enemies['Trevor']['HP'] > 0:
        Trevor_Attack_Menu()



