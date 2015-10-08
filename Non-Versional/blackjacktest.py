#COMMENT ADDED ON OCTOBER 7 2015 -------------------------------*
#First working version 
#March 8 2014
#Andrew Smith
#---------------------------------------------------------------*
from sys import exit
class color:	
	BLUE = '\033[94m'
	RED = '\033[91m'
 	GREEN = '\033[92m'
 	BOLD = '\033[1m'
 	UNDERLINED = '\033`[4m'
 	END = '\033[0m'
	DARKCYAN = '\033[36m'
print color.BOLD +  "----------------------------------------------------------" + color.END
print color.BOLD +  "Welcome to Casino de Smith!" + color.END

print color.BOLD +  "Would you like a seat at the BlackJack table? If not, enter 'Man' to view the manual." + color.END


import random
def new_card():
	return random.choice(('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'A'))
game = False
while game == False:
	card_total = 0
	card_total2 = 10
	table = raw_input("Yes or No ")
	if table == "y":
		print color.BOLD + "----------------------------------------------------------" + color.END
		print color.BOLD +  "Good. We'll get your hand ready." + color.END
		print color.BLUE + "shuffling............." + color.END
		print color.BOLD + "Your first card is a:" + color.END
		card_total = new_card()
		print card_total
		print color.BLUE +  "Oponent recieved 2 cards....... " + color.END
		card_total2 = new_card()
		if card_total2 == int(21):
			print "Wow your opponent got 21, " + color.RED + "You lose!" + color.END
			print "Play again? (Press Enter) "
		
		jugar = False
		while jugar == False:
			hit = raw_input(color.BOLD + "Would you like to hit or stay? " + color.END)
			if hit == "h":
				card_total = card_total + new_card()
				if card_total > 21:
					print "total points: " + str(card_total)
					print color.RED + "GAMEOVER!" + color.END + " You're over 21!"
					print "Tough luck, your opponent had " + str(card_total2) + " points!"
					jugar = True
					again = raw_input("Play again? (Press Enter) ")
				elif card_total == 21:
					print "21! " + color.DARKCYAN + "You Win!!" + color.END
					jugar = True
					again = raw_input("Play again? (Press Enter) ")
					if 'y': 
                                		game = False
					elif 'n':
						print "See you again! "
						game = True
					else:
						print "I don't quite understand. Quiting anyways."
						game = True
				else:
					print "total points: " + str(card_total)
			else:
				print "Your final score is " + str(card_total)
                        	if card_total == card_total2:
					print "You tied! It looks like you're just not good enough!"
					jugar = True
					print color.BOLD + "Play again? " + color.END      
                                elif card_total < card_total2:
         				print color.RED + "You lost by " + str(card_total2 - card_total) + " points! You need more practice!"
                   			jugar = True
					print color.BOLD + "Play again? " + color.END
				elif card_total > card_total2:
					print "Pat yourself on the back! " + color.DARKCYAN + "You beat" + color.END + " your opponent by " + str(card_total - card_total2) + " points!"
					jugar = True
					print color.BOLD + "Play again? " + color.END	
	elif table == "n":
		print color.BOLD + "Okay, the seat is always open." + color.END
		game = True
	elif table == "Man":
		print color.BOLD + "---------------------------------------------------------------------------" + color.END
		print "                                                                                                            "                                                       
                print "                                                                                                            "
		print "                                                                                                            "
		print "                                                                                                            "
		print "                                                                                                            "
		print "                                                                                                            "
		print "                                                                                                            "
		print "                                                                                                            "
		print "                                                                                                            "       
	
	else:
		print color.BOLD + "I'm sorry I didn't quite understand. Start the program again." + color.END
		game = True
