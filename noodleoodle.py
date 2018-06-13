import os #To use terminal commands (os.system('clear'))
os.system('clear') #Clears terminal

title = "Python - Noodleoodle (Sequel to Ravioli)\n"
print(title)
print("You run. You run, and you run, until you can't run anymore. Finally, you find\nyourself well away from that house. You are back at that very bench where\nit all started. You spot a sketchy hoodlum tailing you, you speed up to try\nand escape. He reaches into his pocket, what do you do?")
print("\n1.Run\n2.Take cover\n3.Surrender with hands up\n")
while True:
    try:
        ch1 = int(input("Enter option number (1-3): ")) #Sets choice variable
        if ch1 >= 1 and ch1 <= 3: #Ensures choice numeric input is between 1 and 3
            if ch1 == 1:
                os.system('clear')
                print(title)
                print('You takeoff, as you sprint down the street you look behind you, only to find\nthat nobody was pursuing you. When suddenly you hear the loud, echoing "CRACK!"\nof a 50 cal. And suddenly, everything goes dark...\n')
                print("You Dead! lol xD\n")
                break #Kills Program
            elif ch1 == 2:
                os.system('clear')
                print(title)
                print('You immediately take cover behind a nearby tree. Hearing no gunshots, you peek out\nfrom behind the tree to be startled, as the hoodlum is right in your face.\nInstinctually, you clock him in the nose. He is stunned, staggering back he yells\n"Ah! Good lord, calm down! I just wanted to sell you my mixtape!!"')
                print('Suddenly, the man whips out a purple scar and qucikly taps you with it.')
                print("\nYou Dead! lol xD\n")
                break
            elif ch1 == 3:
                os.system('clear')
                print(title)
                print('The hoodlum stands before you, he utters "Chill out bro! I just wanted to see if\nyou' + "'" + 'd buy a copy of my new mixtape. Suddenly, someone behind you puts a potato\nsack over your head, and stuffs you into a van.\n')
                usrin = input("Press enter to continue...")
                if len(usrin) >= 0:
                    os.system('clear')
                    print(title)
                    print('You are transported to an unknown location, all you know is that you heard an\nelevator earlier, along with lots of echoing. You are seated in a very cold, oddly\nmoist chair. The sack is lifted off your head, there is a table in front of you.\nThe table has two bowls on it, one appearing to be filled with ravioli, and the\nother filled with ramen. A vooice echoing within the room tells you that you must\neat one of the bowls of food. Which do you eat?')
                    print('\n1.The bowl of ravioli\n2.The bowl of ramen\n')
                    ch2 = int(input("Enter option number (1-2): "))
                    if ch2 >= 1 and ch2 <= 2:
                        if ch2 == 1:
                            os.system('clear')
                            print(title)
                            print("You finish the bowl of ravioli. A dizzying feeling overwhelms you, you pass out.\nYou awake and a man appears seated in front of you, wealthy and in his 50's.\nFor some odd reason he seems to be awkwardly fondling a strangely moist ravioli in\nhis right hand.")
                            print("\nThe man stands up, drops the ravioli, waddles towards you, stops close to\nyou, t-bags 2.5 times, sings 'Im a Little Teapot', and takes another strangely\nmoist ravioli from his backpocket, and dropshots you with it. As you begin to\nlose counsciousness, you can hear the man, firmly grasping, awkwardly fondling\nanother moist ravioli while giggling.")
                            print("\nYou Dead! lol xD\n")
                            break
                        elif ch2 == 2:
                            os.system('clear')
                            print(title)
                            print('You finish eating the bowl of ramen, you pass out. You awaken to find yourself damp,\nand in a chair. You cannot exit your seat. You look to find your restraints only to\nsee that you are tied to the chair with a seemingly floppy noodle, as every time you\nmove you hear it squish and flop.')
                            print('\nYou hear a voice echoing from somewhere in the room, a man. He asks you\n"The numbers Mason, what do they mean?!" What is your answer?')
                            print('\n1.What is this 2010?! Black Ops 1 is dead!\n2.Mason? Who the hell is Mason?!\n3.What are you talking about? What numbers?!\n4.They mean let me go.\n5.Ascension...\n6.Nothing. Sit there and flop.\n')
                            ch3 = int(input("Enter option number (1-6): "))
                            if ch3 >= 1 and ch3 <=6:
                                if ch3 == 1: #1.What is this 2010?! Black Ops 1 is dead!
                                    os.system('clear')
                                    print(title)
                                    print('The voice then responds with "No u!" You then recieve\na bullet to the back of the skull and die instantly.')
                                    print("\nYou Dead! lol xD\n")
                                    break
                                    break
                                elif ch3 == 2: #2.Mason? Who the hell is Mason?!
                                    os.system('clear')
                                    print(title)
                                    print('The man then converses with his partner "We got the wrong guy."\nHis partner responds with "He can' + "'" + 't be allowed to talk." You then feel\na prick in your arm, you drift off to sleep. You never wake up.')
                                    print("\nYou Dead! lol xD\n")
                                    break
                                elif ch3 == 3: #3.What are you talking about? What numbers?!
                                    os.system('clear')
                                    print(title)
                                    print('The man, enraged, then speaks in all-caps "THE NUMBERS MASON!"')

                            else: #If input is not between 1 and 6
                                os.system('clear')
                                print("\nNo, just no...\n")
                                break
                        else:
                            os.system('clear')
                            print("\nNo, just no...\n")
                            break
                    else: #If input is not 1 or 2
                        os.system('clear')
                        print("\nNo, just no...\n")
                        break
                else: #If input is not 1, 2, or 3
                    os.system('clear')
                    print("\nNo, just no...\n")
                    break
            else: #If the input choice is not between 1 and 3
                os.system('clear')
                print("\nNo, just no...\n")
                break
    except(ValueError): #If not valid input (Not integer)
        os.system('clear')
        print("\nNo, just no...\n")
        break
    except(KeyboardInterrupt): #If you Ctrl + C
        print("\n\nWow, well you're garbage.\n")
        break
