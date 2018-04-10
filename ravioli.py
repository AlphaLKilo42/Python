print("\nPython - Kidnapping Escape Game \n")
print("One day, you are walking to a friend's house after school, it's a fairly \n" + "long walk there and you decide to sit down at a bench to rest for a few minutes.\n" + "Suddenly, an armored vehicle pulls up, and 2 armed men rush out, aiming at you \n" + "with the disc loaded Nerf guns and forcing you into the vehicle. You are knocked outvia chloroform soaked rag, and transported to a discreet location. You regain\nconciousness and find yourself in a chair, with your hands zip tied to the back of\nit. You are able to read the Braille lettering on the zipties. It reads:\n" + '"Made in China."' + " You are in a dimly lit, empty, concrete room. There is one door\nprotected by 2 armed guards, each with a grey, Fortnite SMG. There is also a man\nsitting calmly in a chair across from you. He looks to be in his mid to late 50's\nand wealthy judging by his suit and his singular ravioli that he was awkwardly\nfondling in his right hand. \n")
print('You need to escape the zip ties. You have 3 options.\n\n' + 'Option 1:\n' + 'You have a razor blade in your shoe, grab it and use it to cut through the ties.\n\n' + 'Option 2:\n' + 'You have keys on your lanyard danglangling from your jeans, grab one and saw through\n' + 'the zip ties.\n\n' + 'Option 3:\n' + 'You also have a 4" pocket knife in your back pocket. Use it to slice through\n' + 'the ties.\n')
while True:
	try: 
		choice1 = int(input("How will you free your hands? Enter the option number (1-3): "))
		if choice1 >= 1 and choice1 <= 3:
			if choice1 == 1:
				print("\nThe man notices you attempting to reach for your shoe. He removes the blade from\n" + "your shoe and cuts your wrists with it, you bleed out.")#, and begins interrogating you claiming\n" + "that he will let you live if you tell him\n" + "what he needs to know.")
				#print('He asks you about a man, by the name of "Yousif". He demands that you tell him\n' + "where he is.")
			elif choice1 == 2:
				print("\nThe man hears your keys danglangling as you attempt to grab one, stands up, drops theravioli, t-pose walks towards you, stops close to you, tbags 3 times, sings Im a\nLittle Teapot, grabs the dangle, takes another strangely moist ravioli from his backpocket, and suffocates you with it. As you begin to lose counsciousness, you can\nhear the man, firmly grasping, fondling another ravioli while giggling.")
			elif choice1 == 3:
				print("\nYou successfully escape the ties without being noticed. Your hands are now free,\n" + "what will you do next?\n")
				print("You are now able to do a multitude of things. But for simplicity's sake you'll\n" + "have 3 choices.\n")
				print("Choice 1:\n" + "Rush the door, take out the guards and bolt.\n\n" + "Choice 2:\n" + "Wait until the man comes over to 'wake you up' and ambush him\n\n" + "Or Choice 3:\n" + "Rush the man in the chair and take him as hostage for your escape.\n\n")
				try:
					choice2a =int(input("How will you attempt your initial escape? Enter the choice number (1-3): "))
					if choice2a >= 1 and  choice2a <= 3:
						if choice2a == 1:
							print("\nThe guards shoot you as soon as you exit the chair, you are dead on the spot.")
						elif choice2a == 2:
							print("\nThe man is caught off-guard, giving you the upper hand. You hit him with a\n" + "gut punch hunching him over. Your knife is knocked free from your hands during the\n" + "altercation. The guards then take aim at you, what is your next move?")
							print("\nYou have 2 choices.\n\nChoice 1:\n" + "Go for the knockout; Knee him in the chin.\n\n" + "Choice 2:\n" +  "Grab and pull him up by the back of his collar, and continue to fight him.\n\n")
							try:
								choice2b = int(input("Enter the action number (1-2): "))
								if choice2b >= 1 and choice2b <= 2:
									if choice2b == 1:
										print("\nYou successfully land the knee and KO the man. However, as the man collapses to the ground, the guards take aim at you, and with no cover to run to, they shoot you dead.")
									elif choice2b == 2:
										print("\nAs you pull the man up, the guards take aim at you. Just as the guards squeeze\ntheir triggers, the man then speedily turns on you, choking you until he\nunknowingly, takes the bullets for you while he is attempting to strangle you.\nThe guards inadvertantly empty their clips into him (They a wee bit retarded), they reload, put another clip in him, reload. They reload a few more times, he still\n" + "doesn't die. They empty more rounds into him, he is still alive. Finally they unload50 more clips into him, and he gets knocked out from the impact of the bullet to hishead. Still not dead. You rush the door while they reload. They attempt to hault youby blocking the doorway. You kick the bigger guys legs out, retrieve your pocket\n" + "knife, and stab the other in the ribs. You have escaped. You run outside to find\nyou are in your friend's backyard. You can still hear the guards shooting the man,\nstill isn't dead...")
								else:
									print("\nInvalid input, can you not read?!\n")
								break
							except (ValueError, TypeError): 
								print("\nInvalid input, can you not read?!\n")
								break
						elif choice2a == 3:
							print("\nYou manage to fight the man enough and get him into a choke hold. However,\n" + "you have no weapon to hold him as a hostage. He gives you an elbow to the ribs,\n" + "forcing you to release him. The guards shoot out your knee. You collapse onto\n" + "the ground, bleeding and slipping into unconciousness, and eventually bleed out.")
					else:
						print("\nInvalid input, can you not read?!\n")
					break
				except (ValueError, TypeError): 
					print("\nInvalid input, can you not read?!\n")
					break
		else:
			print("\nInvalid input, can you not read?!\n")
		break
	except (ValueError, TypeError):
			print("\nInvalid input, can you not read?!\n")
			break
