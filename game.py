from math import e
import random
import time
import os
from slowprint.slowprint import*

def clear():
    command = 'cls'
    os.system(command)

def quit():
    time.sleep(1)
    clear()
    print('--------------------------------------------------------------------')
    slowprint('Thank you for playing this game.', 1)
    slowprint('Made by, Jesse van Vianen', 1)
# ----------------------------------------DONT FORGET TO CHANCE THE DATE-------------------------------------------------
    slowprint('And Noah Zonneveld, 01-10-2021.', 1)
    slowprint('Signing off...', 1)
    print('--------------------------------------------------------------------')
    time.sleep(1)
    clear()
    exit()

def died():
    time.sleep(3)
    slowprint('You died', 1)
    time.sleep(1)
    slowprint('Do you wanna try again?', 1)
    choise1 = input('Y/N: ')
    clear()
    if choise1 == 'Y':
        restart()
    elif choise1 == 'N':
        quit()

def won():
    time.sleep(3)
    slowprint('You won the game!', 1)
    print('')
    time.sleep(1)
    slowprint('press enter to continue', 1)
    input('')
    clear()
    slowprint('There are 3 wins', 1)
    slowprint('Do you wanna try again for a different win?', 1)
    tryAgain = input('Y/N: ')
    if tryAgain == 'Y':
        restart()
    elif tryAgain == 'N':
        quit()

def restart():
    time.sleep(1)
    slowprint('The game will restart', 1)
    time.sleep(1)
    clear()
    main()

clear()

print('=======================================================================')
slowprint('Welcome to the game......', 1)
print('=======================================================================')
print('')
slowprint('press enter to continue', 1)

input('')
clear()

slowprint('First of all, this game is about saving a prisoner from his cell. ', 1)
slowprint('You get a few choices and have to pick one,', 1)
slowprint('If you survive the choices you\'ve made,', 1)
slowprint('You win the game.', 1)
slowprint('If you die along the choices you\'ve made...', 1)
slowprint('You lose!', 1)
slowprint('If you wanna restart the game, type: restart', 1)
slowprint('If you wanna quit the game, type: quit', 1)
slowprint('Goodluck...', 1)
print('========================================================================')

for n in range(0,5):
    if n == 0:
        print('--------')
    elif n == 1:
        print('------')
    elif n == 2:
        print('----')
    elif n == 3:
        print('--')
    time.sleep(1)

slowprint('Lets begin the game!', 1)
time.sleep(1)

def main():
    time.sleep(1)
    clear()

    slowprint('You are a person who is captured by the army...', 1)
    slowprint('They tell you to save a soldier who is imprisoned, ', 1)
    slowprint('You dont know what to expect...', 1)
    slowprint('All you know is that you have to survive for your freedom.', 1)
    slowprint('They send you to the place and you end up at a big castle!', 1)
    slowprint('They leave until you enter...', 1)
    slowprint('Your first thought is, should I enter this castle?', 1)
    print('--------------------------------------------------------------------')

    slowprint('Do you enter the castle?', 1)
    enterCastle = input('yes / no: ')
    clear()
                                        # entering the castle
    if enterCastle == 'yes':
        slowprint('You enter the castle', 1)
        slowprint('You have entered the castle', 1)
        slowprint('You see two large metal doors', 1)
        
        slowprint('Which one do you go through?', 1)
        enterDoor = input('door 1 / door 2: ')
        clear()
                                        # entering door 1
        if enterDoor == 'door 1':
            slowprint('You open door 1', 1)
            slowprint('When you enter into the room the door closes behind you', 1)
            slowprint('When the lights go on you see a room full of giant spiders', 1)
            slowprint('You battle the spiders and...', 1)

            time.sleep(1)
            slowprint('You won the battle', 1)
            print('')
            slowprint('Press enter to continue')
            input('')
            clear()

            slowprint('You continue walking and fall though a trapdoor', 1)
            slowprint('You\'re stuck', 1)
            slowprint('You need to think of a way to get out of the pit', 1)
            slowprint('There are a few options on the ground to help you escape', 1)
            
            slowprint('What will you choose', 1)
            choise2 = input('rope / ladder: ')
            clear()
                                        # choosing the rope
            if choise2 == 'rope':
                slowprint('You see a rope, can you use this rope to climb up?', 1)
                slowprint('You somehow get the rope around some wood and start climbing', 1)
                slowprint('But for some reason the rope breaks', 1)
                slowprint('You can barely hold on to something', 1)
                slowprint('you\'re half way up', 1)
                slowprint('You can continue climbing or let yourself drop so you might try again', 1)
                
                slowprint('What will you do?', 1)
                climbDrop = input('climb / drop: ')
                clear()
                                        # you continue climbing
                if climbDrop == 'climb':
                    slowprint('You continue climbing', 1)
                    slowprint('You reach the top', 1)
                    slowprint('You decide to continue looking for the pisoner', 1)
                    slowprint('You continue on and reach a room with a boss', 1)
                    slowprint('You see two weapons lying on the floor', 1)
                    slowprint('One is a sword imbedded with magic', 1)
                    slowprint('The other one is a minigun with 3000 rounds', 1)
                    slowprint('You have enough time to run to one of them and grab it', 1)
                    
                    slowprint('Whwich weapon do you choose?', 1)
                    weaponChoise = input('minigun / sword: ')
                    clear()
                                        # you choose the minigun
                    if weaponChoise == 'minigun':
                        slowprint('You pick the minigun and start schooting the boss', 1)
                        slowprint('After schooting about half the bulltes your weapon overheats', 1)
                        slowprint('You are vulnerable and the boss is charging you', 1)
                        slowprint('You are smart and run away from the boss', 1)
                        slowprint('After circling around the room you run back to the minigun', 1)
                        slowprint('The weapon cooled down and you shoot the boss', 1)
                        slowprint('The boss dies and falls over', 1)
                        time.sleep(1)
                        
                        print('')
                        slowprint('Press enter to continue', 1)
                        input('')
                        clear()

                        slowprint('As you continue walking to look for the prisoner', 1)
                        slowprint('You notice you got stabbed and you\'re slowly losing blood', 1)
                        slowprint('After looking for 5 more minutes you collapse', 1)
                        died()
                            
                                        # you choose the sword
                    elif weaponChoise == 'sword':
                        slowprint('You pick up the sword', 1)
                        slowprint('The boss charges at you and you cut him', 1)
                        slowprint('After one cut the boss explodes and leaves a black mist behind', 1)
                        slowprint('You see the boss dropped some loot and you go and take a look', 1)
                        slowprint('You see boots that give you super speed when you put them on', 1)
                        slowprint('You also see a pair of gloves', 1)
                        slowprint('There is note that sais: \'These gloves give you super strength,', 1)
                        slowprint('but once you put them on you can never take them off', 1)
                        time.sleep(1)
                        
                        print('')
                        slowprint('Press enter to continue', 1)
                        input('')
                        clear()

                        slowprint('You use the super speed to quick search the castle', 1)
                        slowprint('You find the prisoner and try to break the jailcell by using your super speed', 1)
                        slowprint('Unfortunately that doesn\'t work', 1)
                        slowprint('You doubt for a bit if you should put on the gloves and decide it is the best option', 1)
                        slowprint('You put them on and break jails easily', 1)
                        slowprint('You and the prisoner walk out of the castle', 1)
                        won()

                    elif weaponChoise == 'restart':
                        restart()
                    elif weaponChoise == 'quit':
                        quit()
                                    # you let yourself drop
                elif climbDrop == 'drop':
                    slowprint('You break your leg and get eaten by the monster that lives inside the pit', 1)
                    died()
                elif climbDrop == 'restart':
                    restart()
                elif climbDrop == 'quit':
                    quit()
                                        # choosing the ladder
            elif choise2 == 'ladder':
                slowprint('You put the ladder down and start climbing', 1)
                slowprint('Because you want to hurry you fall down and break your leg', 1)
                slowprint('Luckily there is a man who heard you and gives you a potion', 1)
                slowprint('You drink the potion and your leg is healed', 1)
                slowprint('You climb out of the pit, more carefull this time', 1)
                slowprint('You continue to the next room', 1)
                slowprint('When you enter the room you see a strong looking alien', 1)
                slowprint('You stare at each other', 1)
                slowprint('After a few seconds the alien attacks you', 1)
                slowprint('You go unconscious', 1)
                time.sleep(1)
                
                print('')
                slowprint('Press enter to continue', 1)
                input('')
                clear()

                slowprint('When you wake up you\'re in the alien\'s ship', 1)
                slowprint('The alien is taking you to his home planet, Ognuturn', 1)
                slowprint('When you arrive you\'re being searched by his superiors', 1)
                slowprint('They see potention in you and think for some reason you\'re their ruler', 1)
                slowprint('If you stay you\'ll rule over Ognuturn, but you\'ll never be able to go back to earth', 1)
                slowprint('If you leave and go back to earth you can finish your mission', 1)
                
                slowprint('What will you do?', 1)
                worldChoice = input('stay / leave: ')
                clear()

                                        # you stay on Ognuturn
                if worldChoice == 'stay':
                    slowprint('You stay on Ognuturn', 1)
                    slowprint('You become the ruler', 1)
                    slowprint('As ruler you get access to eternal life', 1)
                    slowprint('You get everything you ever wanted and more', 1)
                    slowprint('You forget of you life on earth', 1)
                    slowprint('You continue living, far past the prisoner you were supposed to save', 1)
                    slowprint('Mission failed?', 1)
                    won()

                                        # you go back to earth
                elif worldChoice == 'leave':
                    slowprint('You return to earth', 1)
                    slowprint('You find the prisoner with the help of the aliens', 1)
                    slowprint('You continue living your life on earth', 1)
                    slowprint('Nothing specials happens and eventually you die of old age', 1)
                    slowprint('Mission complete', 1)
                    won()

                elif worldChoice == 'restart':
                    restart()
                elif worldChoice == 'quit':
                    quit()

            elif choise2 == 'restart':
                restart()
            elif choise2== 'quit':
                quit()

                                        # entering door 2
        elif enterDoor == 'door 2':
            slowprint('You open door 2', 1)
            slowprint('You walk in and as the door falls shut', 1)
            slowprint('You see two armed guards', 1)
            slowprint('You attack the guards', 1)
            print('')
            slowprint('Press enter to continue', 1)
            clear()

            randomEncounter = int(random.randint(1,2))
            print('Encounter: ' + str(randomEncounter))
            slowprint('Do you want to continue this encounter?', 1)
            slowprint('If you don\'t continue the game will restart', 1)
            continueEncounter = input('yes / no')
            clear()

                                        # you continue the encounter
            if continueEncounter == 'yes':
                                        # if you get the first encounter (you win the battle)
                if randomEncounter == 1:
                    print()

                                        # if you get the second encounter (you  lose the battle)
                elif randomEncounter == 2:
                    slowprint('The guard win and you are being tortured', 1)
                    slowprint('They wanna know where the army is located', 1)
                    slowprint('You can stay silent or tell them', 1)

                    slowprint('What do you do?', 1)
                    torture = input('talk / keep quiet')
                    clear()

                    if torture == 'talk':
                        slowprint('You tell the location from the arm and you get locked away', 1)

                    elif torture == 'keep quiet':
                        slowprint('You keep quiet and they keep torturing you', 1)
                        slowprint('Until out of nowhere a ninja shows', 1)
                        slowprint('The ninja rescues you and you walk out of the room', 1)
                        time.sleep(1)
                        clear()
                        
                        slowprint('You and the ninja come across a boss', 1)
                        slowprint('Together you go and fight the boss, but he is really strong', 1)
                        slowprint('You notice you don\'t have the strength to fight because of the torture', 1)
                        slowprint('The ninja has no choise but to fight alone and loses', 1)
                        slowprint('The boss defeats you both', 1)
                        died()

                    elif torture == 'restart':
                        restart()
                    elif torture == 'quit':
                        quit()

                                        # you restart the game for a different encounter
            elif continueEncounter == 'restart' or continueEncounter == 'no':
                restart()
            elif continueEncounter == 'quit':
                quit()

        elif enterDoor == 'restart':
            restart()
        elif enterDoor == 'quit':
            quit()

                                        # not entering the castle
    elif enterCastle == 'no':
        slowprint('The Guards have shot you.', 1)
        died()
    elif enterCastle == 'restart':
        restart()
    elif enterCastle == 'quit':
        quit()

main()