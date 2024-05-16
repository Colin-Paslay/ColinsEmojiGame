import os

from emoji import emojize


wins = 0
losses = 0
phase = 1

group = "🧑🤝🧑"
castle = emojize(":castle:")
two = emojize(":2nd_place_medal:")
bluePortal = emojize(":blue_circle:")
orangePortal = emojize(":orange_circle:")
gun = emojize(":water_pistol:")
tree = emojize(":deciduous_tree:")
guy = emojize(":man:")
pick = emojize(":pick:")
diamond = emojize(":gem_stone:")
sword = emojize(":crossed_swords:")
shield = emojize(":shield:")
triangle = emojize(":red_triangle_pointed_up:")
ganon = emojize(":ogre:")
mushroom = emojize(":mushroom:")
princess = emojize(":princess:")
turtle = emojize(":turtle:")
night = emojize(":night_with_stars:")
ghost = emojize(":ghost:")
berry = emojize(":strawberry:")
pack = emojize(":backpack:")
face1 = emojize(":grinning_face:")
face2 = emojize(":grinning_face_with_big_eyes:")
face3 = emojize(":grinning_face_with_smiling_eyes:")
face4 = emojize(":beaming_face_with_smiling_eyes:")
face5 = emojize(":grinning_squinting_face:")
faceImp = emojize(":imposter:")
cowboy = emojize(":cowboy_hat_face:")
desert = emojize(":desert:")
planet = emojize(":ringed_planet:")
salute = emojize(":saluting_face:")
flag = emojize(":flag_super_earth:")

phase1_emoji = [group,castle,two]
phase2_emoji = [bluePortal, gun, orangePortal]
phase3_emoji = [guy, pick, diamond]
phase4_emoji = [guy, sword, ganon, triangle, triangle, triangle]
phase5_emoji = [mushroom, princess, turtle]
phase6_emoji = [castle, night]
phase7_emoji = [pack, berry, ghost]
phase8_emoji = [face1, face2, face3, faceImp, face4, face5]
phase9_emoji = [cowboy, gun, desert]
phase10_emoji = [salute, flag, planet]



print("This is a guessing game about guessing games")
print("\nRead the emojis and type in the full name of the game they represent.")
input("\nPress enter to start. ")
while True:
    os.system('cls')
    print("The current phase is "+str(phase)+". You have won "+str(wins)+" phases.")
    if losses <= 4:
        if phase == 1:
            print(phase1_emoji)
            selection = input("The game is: ")
            if selection.lower() == "team fortress two" or selection.lower() == "team fortress 2":
                input("Correct! ")
                wins += 1
            else:
                losses += 1
                input("Wrong. ")
            phase += 1
        elif phase == 2:
            print(phase2_emoji)
            selection = input("The game is: ")
            if selection.lower() == "portal" or selection.lower() == "portal 2" or selection.lower() == "portal two":
                input("Correct! ")
                wins += 1
            else:
                losses += 1
                input("Wrong. ")
            phase += 1
        elif phase == 3:
            print(phase3_emoji)
            selection = input("The game is: ")
            if selection.lower() == "minecraft" or selection.lower == "minceraft":
                input("Correct! ")
                wins += 1
            else:
                losses += 1
                input("Wrong. ")
            phase += 1
        elif phase == 4: 
            print(phase4_emoji)
            selection = input("The game is: ")
            if selection.lower() == "the legend of zelda" or selection.lower() == "legend of zelda" or selection.lower() == "zelda":
                input("Correct! ")
                wins += 1
            else:
                losses += 1
                input("Wrong. ")
            phase += 1
        elif phase == 5:
            print(phase5_emoji)
            selection = input("The game is: ")
            if selection.lower() == "mario" or selection.lower() == "super mario bros" or selection.lower() == "super mario brothers":
                input("Correct! ")
                wins += 1
            else:
                losses += 1
                input("Wrong. ")
            phase += 1
        elif phase == 6:
            print(phase6_emoji)
            selection = input("The game is: ")
            if selection.lower() == "fortnite":
                input("Correct! ")
                wins += 1
            else:
                losses += 1
                input("Wrong. ")
            phase += 1
        elif phase == 7:
            print(phase7_emoji)
            selection = input("The game is: ")
            if selection.lower() == "pacman" or selection.lower() == "pac-man":
                input("Correct! ")
                wins += 1
            else:
                losses += 1
                input("Wrong. ")
            phase += 1
        elif phase == 8:
            print(phase8_emoji)
            selection = input("The game is: ")
            if selection.lower() == "amogus" or selection.lower() == "among us" or selection.lower() == "amongus":
                input("Correct! ")
                wins += 1
            else:
                losses += 1
                input("Wrong. ")
            phase += 1
        elif phase == 9:
            print(phase9_emoji)
            selection = input("The game is: ")
            if selection.lower() == "red dead redemption" or selection.lower() == "red dead redemption 2":
                input("Correct! ")
                wins += 1
            else:
                losses += 1
                input("Wrong. ")
            phase += 1
        elif phase == 10:
            print(phase10_emoji)
            selection = input("The game is: ")
            if selection.lower() == "helldivers" or selection.lower() == "helldivers 2":
                input("Correct! ")
                wins += 1
            else:
                losses += 1
                input("Wrong. ")
            phase += 1
        else:
            os.system('cls')
            print("Congratulations! You Win! You answered "+str(wins)+" of the questions correctly!\n")
            if wins == 10: print("Great job on your perfect score!")
            else: print("Try to improve your score next time!")
            break
    elif losses == 5:
        print("Careful now...")
        if phase == 6:
            print(phase6_emoji)
            selection = input("The game is: ")
            if selection.lower() == "fortnite":
                input("Correct! ")
                wins += 1
            else:
                losses += 1
                input("Wrong. ")
            phase += 1
        elif phase == 7:
            print(phase7_emoji)
            selection = input("The game is: ")
            if selection.lower() == "pacman" or selection.lower() == "pac-man":
                input("Correct! ")
                wins += 1
            else:
                losses += 1
                input("Wrong. ")
            phase += 1
        elif phase == 8:
            print(phase8_emoji)
            selection = input("The game is: ")
            if selection.lower() == "amogus" or selection.lower() == "among us" or selection.lower() == "amongus":
                input("Correct! ")
                wins += 1
            else:
                losses += 1
                input("Wrong. ")
            phase += 1
        elif phase == 9:
            print(phase9_emoji)
            selection = input("The game is: ")
            if selection.lower() == "red dead redemption" or selection.lower() == "red dead redemption 2":
                input("Correct! ")
                wins += 1
            else:
                losses += 1
                input("Wrong. ")
            phase += 1
        elif phase == 10:
            print(phase10_emoji)
            selection = input("The game is: ")
            if selection.lower() == "helldivers" or selection.lower() == "helldivers 2":
                input("Correct! ")
                wins += 1
            else:
                losses += 1
                input("Wrong. ")
            phase += 1
        else:
            os.system('cls')
            print("Unfortunately you only tied. 5 wins and 5 losses.")
            break
    else:
        os.system('cls')
        print("You lose. Idiot.")
        break