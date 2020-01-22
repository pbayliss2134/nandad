import time
import random
import os

wood = 0
stone = 0
metal = 0
gold = 0
money = 5000
cloth = 0
defence = 0

damageDealt = 0
damage = 0
healthDamage = random.randint(1,20)
crimeLevelBooster = random.randint(1,20)
inventory = []
health = 100
crimeLevel = 0
expLevel = 0
level = 0

# Class that organizes all menu functions in one place. Call these using Menus.NameOfMenu

class Menus:
    def CraftingMenu():
        print()
        print("======================================================#")
        print("#                 Welcome to Crafting!                #")
        print("======================================================#")
        print("#1 Wooden Broad Sword|      Ingredients: 10W 2S       #")
        print("#2 Stone Broad Sword |      Ingredients: 5W 15S       #")   
        print("#3 Metal Broad Sword |  Ingredients: 5W 10S 15M       #")
        print("#4 Golden Broad Sword| Ingredients: 20W 20S 100M 100G #")
        print("======================================================#")
        print("#5 Wooden Armour|           Ingredients: 70W 10C      #")
        print("#6 Stone Armour|            Ingredients: 75S 15C      #")
        print("#7 Metal Armour|            Ingredients: 70M 40C      #")
        print("#8 Golden Armour|          Ingredients: 100G 50M 60C  #")
        print("======================================================#")
        print()
        print("W = Wood (",wood,")")
        print("S = Stone (",stone,")")
        print("M = Metal (",metal,")")
        print("G = Gold (",gold,")")
        print("C = Cloth (",cloth,")")
        print()
        print("WARNING: KEEP IN MIND THAT WHEN YOU CRAFT AN ITEM, THE STAT OF THE ITEM YOU CRAFTED WILL")
        print("OVERRIDE YOUR CURRENT EQUIPED ITEM. THERE IS NO WAY TO REVERSE THIS. E.G: IT IS NOT")
        print("ADVISED TO CRAFT A WOODEN BROAD SWORD AFTER CRAFTING A GOLD BROAD SWORD AS ALTHOUGH THE")
        print("GOLD BROAD SWORD WILL STILL BE VIEWABLE IN YOUR INVENTORY, THERE IS NO WAY TO RE-EQUIP IT,")
        print("MEANING YOUR DAMAGE MULTIPLIER WOULD BE REPLACED BY THE WOODEN BROAD SWORD.")
        print("SAME GOES FOR ARMOUR SETS.")
        print()
    
        while True:
            try:
                craftItem = int(input("What would you like to craft? > "))

                if craftItem > 8 or craftItem < 1:
                    print("Incorrect Input. Try Again...")
                    continue

                # Crafting for Wooden Broad Sword.
                
                if craftItem == 1:
                    print("Attempting to craft Wooden Broad Sword...")
                    time.sleep(1)

                    if wood < 10 or stone < 2 or wood < 10 and stone < 2:
                        print("You do not have enough materials for this operation.")
                        print()
                        quitCrafting = input("Would you like to end crafting (1) or proceed back to the menu? (2) > ")

                        if quitCrafting == 1:
                            print("Okay, quitting crafting...")
                            print()
                            time.sleep(2)
                            break

                        if quitCrafting == 2:
                            print("Okay, proceeding back to the crafting menu.")
                            Menus.CraftingMenu()
                            break

                    if wood >= 10 and stone >= 2:
                        print("Wooden Broad Sword has been crafted.")
                        print("Wooden Broad Sword has been appended to your inventory.")
                        
                        damage = 15
                        
                        inventory.append("Wooden Broad Sword")
                        break

                # Crafting for Stone Broad Sword.

                if craftItem == 2:
                    print("Attempting to craft Stone Broad Sword.")
                    time.sleep(1)

                    if wood < 5 or stone < 15 or wood < 5 and stone < 15:
                        print("You do not have enough materials for this operation.")
                        print()
                        quitCrafting = input("Would you like to end crafting (1) or proceed back to the menu? (2) > ")

                        if quitCrafting == 1:
                            print("Okay, quitting crafting...")
                            print()
                            time.sleep(2)
                            break

                        if quitCrafting == 2:
                            print("Okay, proceeding back to the crafting menu.")
                            Menus.CraftingMenu()
                            break
                        
                    if wood >= 5 and stone >= 15:
                        print("Stone Broad Sword has been crafted.")
                        print("Stone Broad Sword has been appended to your inventory.")

                        damage = 25

                        inventory.append("Stone Broad Sword")
                        break

                # Crafting for Metal Broad Sword.

                if craftItem == 3:
                    print("Attempting to craft Metal Broad Sword.")
                    time.sleep(1)

                    if wood < 5 or stone < 10 or metal < 15 or wood < 5 and stone < 10 and metal < 15:
                        print("You do not have enough materials for this operation.")
                        print()
                        quitCrafting = input("Would you like to end crafting (1) or proceed back to the menu? (2) > ")

                        if quitCrafting == 1:
                            print("Okay, quitting crafting...")
                            print()
                            time.sleep(2)
                            break

                        if quitCrafting == 2:
                            print("Okay, proceeding back to the crafting menu.")
                            Menus.CraftingMenu()
                            break

                    if wood >= 5 and stone >= 10 and metal >= 15:
                        print("Metal Broad Sword has been crafted.")
                        print("Metal Broad Sword has been appended to your inventory.")

                        damage = 35

                        inventory.append("Metal Broad Sword")
                        break

                # Crafting for Golden Broad Sword.

                if craftItem == 4:
                    print("Attempting to craft Golden Broad Sword.")

                    if wood < 20 or stone < 20 or metal < 100 or gold < 100 or wood < 20 and stone < 20 and metal < 100 and gold < 100:
                        print("You do not have enough materials for this operation.")
                        print()
                        quitCrafting = input("Would you like to end crafting (1) or proceed back to the menu? (2) > ")

                        if quitCrafting == 1:
                            print("Okay, quitting crafting...")
                            print()
                            time.sleep(2)
                            break

                        if quitCrafting == 2:
                            print("Okay, proceeding back to the crafting menu.")
                            Menus.CraftingMenu()
                            break

                    if wood >= 20 and stone >= 20 and metal >= 100 and gold >= 100:
                        print("Golden Broad Sword has been crafted.")
                        print("Golden Broad Sword has been appended to your inventory.")

                        damage = 60

                        inventory.append("Golden Broad Sword")
                        break

                # Crafting for Wooden Armour.

                if craftItem == 5:
                    print("Attempting to craft Wooden Armour.")

                    if wood < 70 or cloth < 10 or wood < 70 and cloth < 10:
                        print("You do not have enough materials for this operation.")
                        print()
                        quitCrafting = input("Would you like to end crafting (1) or proceed back to the menu? (2) > ")

                        if quitCrafting == 1:
                            print("Okay, quitting crafting...")
                            print()
                            time.sleep(2)
                            break

                        if quitCrafting == 2:
                            print("Okay, proceeding back to the crafting menu.")
                            Menus.CraftingMenu()
                            break

                    if wood >= 70 and cloth >= 10:
                        print("Wooden Armour has been crafted.")
                        print("Wooden Armour has been appended to your inventory.")

                        defence = 0.9

                        inventory.append("Wooden Armour")
                        break

                # Crafting for Stone Armour.

                if craftItem == 6:
                    print("Attempting to craft Stone Armour.")

                    if stone < 75 or cloth < 15 or stone < 75 and cloth < 15:
                        print("You do not have enough materials for this operation.")
                        print()
                        quitCrafting = input("Would you like to end crafting (1) or proceed back to the menu? (2) > ")

                        if quitCrafting == 1:
                            print("Okay, quitting crafting...")
                            print()
                            time.sleep(2)
                            break

                        if quitCrafting == 2:
                            print("Okay, proceeding back to the crafting menu.")
                            Menus.CraftingMenu()
                            break

                    if stone >= 75 and cloth >= 15:
                        print("Stone Armour has been crafted.")
                        print("Stone Armour has been appended to your inventory.")

                        defence = 0.8

                        inventory.append("Stone Armour")
                        break

                # Crafting for Metal Armour.                

                if craftItem == 7:
                    print("Attempting to craft Metal Armour.")

                    if metal < 70 or cloth < 40 or metal < 70 and cloth < 40:
                        print("You do not have enough materials for this operation.")
                        print()
                        quitCrafting = input("Would you like to end crafting (1) or proceed back to the menu? (2) > ")

                        if quitCrafting == 1:
                            print("Okay, quitting crafting...")
                            print()
                            time.sleep(2)
                            break

                        if quitCrafting == 2:
                            print("Okay, proceeding back to the crafting menu.")
                            Menus.CraftingMenu()
                            break

                    if metal >= 70 and cloth >= 40:
                        print("Metal Armour has been crafted.")
                        print("Metal Armour has been appended to your inventory.")

                        defence = 0.7

                        inventory.append("Metal Armour")
                        break

                # Crafting for Golden Armour.

                if craftItem == 8:
                    print("Attempting to craft Golden Armour")

                    if gold < 100 or metal < 50 or cloth < 60 or gold < 100 and metal < 50 and cloth < 60:
                        print("You do not have enough materials for this operation.")
                        print()
                        quitCrafting = input("Would you like to end crafting (1) or proceed back to the menu? (2) > ")

                        if quitCrafting == 1:
                            print("Okay, quitting crafting...")
                            print()
                            time.sleep(2)
                            break

                        if quitCrafting == 2:
                            print("Okay, proceeding back to the crafting menu.")
                            Menus.CraftingMenu()
                            break

                    if gold >= 100 and metal >= 50 and cloth >= 60:
                        print("Golden Armour has been crafted.")
                        print("Golden Armour has been appended to your inventory.")

                        defence = 0.4

                        inventory.append("Golden Armour.")
                        break
                        
            except ValueError:
                print("Invalid Input. Try Again...")
                continue
        
    def HelpMenu():
        print()
        print("You are in a communist society.")
        print("Your aim is to override the dictator master.")
        print()
        print("You have an inventory that you append items to when you obtain them.")
        print()
        print("You have a crime level that increases whenever you do a crime.")
        print("If your crime level reaches 100, you will instantly be caught and")
        print("executed.")
        print()
        print("You have a health bar that in the event it reaches 0, you will die.")
        print()
        print("You will start with 5000 cash")
        print()
        print("You have EXP that at the end of every mission translates to cash.")
        print()
        print("Crafting will be introduced as the game gets underway.")
        print()
        input("Press any key to continue...")

    def QuitMenu():
        print("You have chosen to quit the game.")
        
        while True:
            try:
                quit_ = str(input("Are you sure? (y/n) > "))

                if quit_ == "y":
                    print("Quitting...")
                    time.sleep(2)
                    exit()

                if quit_ == "n":
                    print("OK, continuing...")
                    time.sleep(2)
                    break

                if quit_ != "y" or quit_ != "n":
                    print("Incorrect input... Try again.")
                    continue

            except ValueError:
                print("Incorrect input... Try again.")
                continue

# Game officially starts with a loading screen.
            
loadingScreen = "Loading..."
for letter in loadingScreen:
    print(letter)
    time.sleep(0.5)
    
print("Your parents birthed you into this society 23 years ago.")
print("You do not want to live in a dictatorship, a communist establishment")
print("that hates you, that is biased against you. You want to try and rebel and")
print("take back your freedom in this society.")

while True:
    try:
        startOrQuit = int(input("Do you want to start (1), quit (2), or open help menu? (3) > "))

        if startOrQuit == 1:
            print("Starting...")
            print()
            time.sleep(2)
            break

        if startOrQuit == 2:
            Menus.QuitMenu()

        if startOrQuit == 3:
            Menus.HelpMenu()
            print()
            break

        if startOrQuit > 3 or startOrQuit < 1:
            print("Invalid Input... Try Again.")
            print()
            continue

    except ValueError:
        print("Invalid Input... Try Again.")
        continue

print("Your friend, Zakary, owns his own blacksmith. He to wants to rebel against")
print("the communist society you both live in. He has learned what you plan to do, ")
print("therefore has gifted you a sword to kickstart your rebellion.")
print()

print("Basic Sword has been appended to your Inventory!")
inventory.append("Basic Sword")

userName = input("Before we get going, what is your name? > ")
print("Hi,",userName,"!")

print("A communist representative arrives at your doorstep. He is promoting the corrupt")
print("ways of the government. What will you do?")
print()
print("(1) Jump from your open window and stab the representative in the head, leaving")
print("no trace of murder.")
print()
print("(2) Politely agree with the communist, while inside you are raging with fury.")
print()
print("(3) Knock the guy out.")
print()
print("(4) Shout at the representative and scare him off.")
print()
print("(5) Ignore the communist representative.")
print()

while True:
    try:
        decision1 = int(input("What will you choose? > "))

        if decision1 == 1:
            risk1 = random.randint(1,4)
            
            if risk1 == 1:
                print("You unlock your window, do a 360 backflip and while mid-air, you pull your sword out.")
                print("You stealthily and swiftly insert the sword into the representatives head with a solid hand, ")
                print("leaving no trace of murder... Unless you don't hide the evidence...")
                print()
                print("You gain 40EXP!")
                expLevel = expLevel + 40

                crimeLevel = crimeLevel + crimeLevelBooster
                break

            if risk1 == 2:
                print("You go to your window, but realise it is locked and by the time you find the key, the communist")
                print("turns into a 90 foot long crocodile that consumes your whole country in a matter of minutes.")
                print()
                print(userName,"was slain by Giant Communist Croc!")
                print("GAME OVER!!!")
                print("You died with",expLevel,"EXP and with these items:",inventory,".")
                exit()

            if risk1 == 3:
                print("Your window is locked. You cannot find the key. You just decide to ignore the representative.")
                print("Anyway, he does not deserve your time...")
                break

        if decision1 == 2:
            risk2 = random.randint(1,3)

            if risk2 == 1:
                print("You politely agree with the communist, and although you can feel the rage bubbling inside you, you")
                print("manage to contain yourself.")
                expLevel = expLevel + 20
                break

            if risk2 == 2:
                print("You try to agree with the communist, however, your fury gets to you. You bare your sword at the communist, and")
                print("he runs away. The next day the police turn up (PC Skae). You are lucky to only get a Stage 3 Caution, if you get another, you")
                print("will be instantly arrested. You are lucky this is only in affect for a month.")

                crimeLevel = crimeLevel + crimeLevelBooster
                break

        if decision1 == 3:
            risk3 = random.randint(1,3)

            if risk3 == 1:
                print("You swing open the door, and put the unexpecting man into a forceful headlock. He is armed with a knife, but you")
                print("manage to disarm him. You punch him hard in his right temple with a firm right hook. He is knocked out.")

                crimeLevel = crimeLevel + crimeLevelBooster
                break

            if risk3 == 2:
                print("You swing the door open, and bring your heavy fist back to punch, and you swing with so much rage that you miss.")
                print("The communist representative draws a knife from his hip and slashes you, giving you a nasty cut on your arm.")

                health = health - healthDamage
                print("You lost",healthDamage,"health.")
                break

        if decision1 == 4:
            risk4 = random.randint(1,3)

            if risk4 == 1:
                print("You open your window and yell at the communist. He looks intimidated when you threaten him with your sword and")
                print("decides to flee from your vision.")
                break

            if risk4 == 2:
                print("You proceed to yell at the communist. Instead of running, he calls the police. When the police arrive, they")
                print("inform you that you need to pay a hefty fine of 300 cash for anti-social behaviour.")
                print()
                
                print("You reluctantly hand over the money. You lost 300 cash.")
                money = money - 300
                break

        if decision1 == 5:
            print("You ignore the communist representative. He eventually leaves.")
            break
                
    except ValueError:
        print("Invalid Input... Try Again.")
        continue

input("Press any key to continue...")

print()
print("You are sat at your PC, contemplating ideas on how to approach destroying this communist dictatorship you are in.")
print("You are just sat doing this as your friend Zakary shoots you a call on Skype. You pick up his call and he")
print("has an idea. To start raising controversy, you should raid the local communist social club and take money")
print("and recources. You realise this could be a smart decision if you succeed.")
print()
print("First, you will need recources. Your friend Zakary arrives at your home and gives you some stone, wood, gold, cloth")
print("and metal.")
print()

stone = stone + 30
wood = wood + 30
metal = metal + 5
gold = gold + 1
cloth = cloth + 25

print("30 Stone added.")
print("30 Wood added.")
print("5 Metal added.")
print("1 Gold added.")
print("25 Cloth added.")
print()

input("Press any key to continue...")

print("Zakary leads you to his bench, where he shows you the craft of making a weapon. He hands the material over")
print("to you. You need to make a Stone Broad Sword. A wooden one is too weak for you at the moment.")

Menus.CraftingMenu()

print()
print("Thats great. You will now have the capacity for some extra damage!")
print()

print("You walk into town, your weapon holstered in your belt, positioned so it is hidden underneath your thick jacket.")
print("The communist social club is just across the street. The plan is to come in from behind, so you take a notebook")
print("and jot down security guard positions and trajectory for your attack. The front door is not an option, so you")
print("decide to scale a pipe in a dark alleway with no one looking. You enter the alleway with nobody seeing you.")
print()
input("Press any key to continue...")
print()
print("You are on the roof of the communist social club. You clamber down the back of the building and bust open the back door.")
print("Unfortunately, there is one guard posted a bit in front of the door. He hears the noise, so you back off behind a wall.")
print()
print("What will you do?")
print()
print("1. As the guard walks out into the open, silently strike him with a solid swipe.")
print()
print("2. Pounce swiftly around the corner and choke the guard to death.")
print()

while True:
    try:
        guardAnswer = int(input("> "))

        if guardAnswer == 1:
            guardChance = random.randint(1,5)
            
            if guardChance == 1:
                print("As the guard comes through the door into the open, you stab him quietly in the back.")
                
                damageRandomiser = random.randint(1,40)
                damageRandomiser = damageRandomiser + damage
                print("You deal",damageRandomiser,"to the guard. Silent strikes wipe out the reciever instantly.")
                
                print("You lug his body into a nearby skip and cover the dead corpse with rubbish.")
                crimeLevel = crimeLevel + 5
                expLevel = expLevel + 40
                break

            if guardChance == 2:
                print("You try to strike the guard, but he is expecting you. He pins you to the wall and slits your")
                print("throat. He takes your corpse inside.")
                print()
                print("The game will now terminate since you have died... LOL!")
                exit()

        if guardAnswer == 2:
            guardChance = random.randint(1,5)

            if guardChance == 1:
                print("You pounce around the corner at the guard, pummeling him to the ground. He hits his head on the concrete")
                print("and blood spirts everywhere. You choke him from his neck until he dies. You hide his body in a rubbish bin.")

                damageRandomiser = random.randint(1,40)
                damageRandomiser = damageRandomiser + damage
                print("You deal",damageRandomiser,"to the guard. Silent strikes wipe out the reciever instantly.")
                crimeLevel = crimeLevel + 5
                expLevel = expLevel + 40
                break

            if guardChance == 2:
                print("You pounce around the corner but the guard uses momentum against you to pin you to the floor. Once you are")
                print("grounded, he pummels your skull multiple times until your brain ruptures.")
                print()
                print("The game will now terminate since you died... LOL!")
                exit()

        if guardAnswer > 2 or guardAnswer < 1:
            print("Invalid Input... Try Again.")
            continue
        
    except ValueError:
        print("Invalid Input... Try Again.")
        continue

print()
input("Press any key to continue...")
print()
print("You have made your way in.")
print("You turn the corner, there you see a high security door. You try the handle...")
print("ITS UNLOCKED!!! This is horrible security, but none-the-less, you continue through.")
print()
print("You turn the corner, and you see a huge silver door, with a large circular handle attached to the front.")
print("It looks like the vault to you... ")
print()
print("But you have made one huge mistake. You did not bring a drill to break into the vault. You need assistance, so you")
print("ring your friend Zakary for help. You tell him you forgot your thermal drill, and he tells you he will grab his and")
print("be right over.")
print()
print("30 seconds pass, and you are waiting. You back closer to the door, but trip on a metal shelf. The loud clinging and")
print("clanging alerts one guard of your position... He arrives in your eyeline.")
print()
input("Press any key to continue...")
print()
print("What will you do?")
print("1. Pounce the guard and stab him.")
print("2. As the guard turns, silently strike him in the back of the neck with a fist, giving him a violent seizure.")
print()

while True:
    try:
        guardAttackAnswer = int(input("> "))
        guardAttackChance = random.randint(1,6)

        if guardAttackAnswer == 1:
            if guardAttackChance == 1 or guardAttackChance == 2 or guardAttackChance == 3 or guardAttackChance == 4:
                print("You pounce the guard, and he falls to the ground. You stab the living daylight out of him.")

                damageRandomizer = random.randint(1,41)
                damageDealt = damageDealt + damageRandomizer + damage
                print("You deal",damageDealt,"to the guard.")
                print()
                crimeLevel = crimeLevel + 10
                expLevel = expLevel + 40
                break

            if guardAttackChance == 5:
                print("You try to stab the guard, but he evades your strike. He judo trips you, and throttles you to death.")
                print("GAME OVER. You die with",expLevel,"EXP and these items:",inventory,".")
                input("Press any key to continue...")
                print()
                print("The game will now terminate because you died.")
                time.sleep(2)
                
                exit()

        if guardAttackAnswer == 2:
            if guardAttackChance == 1 or guardAttackChance == 2 or guardAttackChance == 3 or guardAttackChance == 4:
                print("You do a 720 in the air and bash the guard on the back of the neck with a strong fist.")

                damageRandomizer = random.randint(1,40)
                damageDealt = damageDealt + damageRandomizer + damage
                print("You deal",damageDealt,"to the guard.")
                print()
                crimeLevel = crimeLevel + 10
                expLevel = expLevel + 40
                break

            if guardAttackChance == 5:
                print("You do a 720 mid air, but the guard stops you in his tracks. He stabs you in the heart.")
                print("GAME OVER. You die with",expLevel,"EXP and these items:",inventory,".")
                input("Press any key to continue...")
                print()
                print("The game will now terminate because you died.")
                time.sleep(2)

                exit()

        if guardAttackAnswer > 2 or guardAttackAnswer < 1:
            print("Invalid Input... Try Again.")
            print()
            continue
        

    except ValueError:
        print("Invalid Input... Try Again.")
        continue

input("Press any key to continue...")
print()
print("You have been waiting 5 minutes, and Zakary arrives carrying his big thermal drill. He connects it to the power brick with a")
print("large battery, connects it to the large wheel on the front of the vault and attaches a sort of device. When you ask")
print("what the device is, he tells you it is a silencer so no noise is made. He wasn't lying. When he switches on the")
print("drill, the silent procedure begins.")
print()
print("10 seconds of hyper powered drilling passes...")
input("Press any key to continue...")
print()
print("The vault door comes slightly ajar. You enter to find stacks of money, jewels and materials. Your body tingles with")
print("excitement. This is the first mission on your quest to domination.")
print()
print("Materials Added:")
print("30 Wood")
print("30 Stone")
print("20 Metal")
print("50 Cloth")
print("15 Gold")
print("20,000 Cash")

wood = wood + 30
stone = stone + 30
metal = metal + 20
cloth = cloth + 50
gold = gold + 15
money = money + 20000

os.system("cls")

print("You arrive back at your crib. After your encounters, your crime level is",crimeLevel,"and your EXP is",expLevel,".")
print("Your EXP will now translate to cash. If exp is > 50 then you gain 10000 cash.")
input("Press any key to continue...")

if expLevel > 20:
    print("You have gained 10000 cash.")
    money = money + 10000
else:
    print("Not enough EXP.")
    

print()
print("You cash is now at a total of",money,".")
print()
print("Would you like to open the crafting menu (1), or continue with the game? (2)")

while True:
    try:
        craftingMenuOrContinue = int(input("> "))

        if craftingMenuOrContinue == 1:
            print("Okay, opening crafting...")
            time.sleep(2)
            Menus.CraftingMenu()
            break

        if craftingMenuOrContinue == 2:
            print("Okay, continuing the game...")
            time.sleep(2)
            break

        if craftingMenuOrContinue < 1 or craftingMenuOrContinue > 2:
            print("Invalid Input... Try Again.")
            print()
            continue

    except ValueError:
        print("Invalid Input... Try Again.")
        print()
        continue

os.system("cls")
print()
print("That is it for Communist Society Version 1.0.0")
print()
print("Note From Developer: Thank you for playing, hope you had fun!")
    


            





































































































































































































































































































































































































































































                
                

                

            

            
                
            


            








            
        

    
                    

