#Andrew Smith
#November 5 2014
from sys import exit
import string

import time

class color:	
	BLUE = '\033[94m'
	RED = '\033[91m'
 	GREEN = '\033[92m'
 	BOLD = '\033[1m'
 	UNDERLINED = '\033`[4m'
 	END = '\033[0m'
	DARKCYAN = '\033[36m'

import random

version = str("2.1")
def vers_please():
	print "{" + version + "}"
	print "Copyright KM187 App Development"
	print "November 4, 2014"

letter = ""
def new_card():
        return random.randint(1, 11)
def hrd_card():
        return random.randint(1,11)
def card_letter():
        letter = random.sample(set('DCHS'), 1)[0]
        if letter == "D":
                return color.RED + "Diamonds" + color.END
        elif letter == "H":
                return color.RED + "Hearts" + color.END

        elif letter == "C":
                return color.BOLD + "Clubs" + color.END

        elif letter == "S":
                return color.BOLD + "Spades" + color.END
        else:
                return 0
def space():
        print "              "
def super_space(x):
	count = x
	while count > 0:
		print "                   "
		count = count - 1
def line_please():
	print color.BOLD + "---------------------------------------------------------------------------" + color.END


def thinking(x):
        time.sleep(x)



game = False

oponent = False

card = 0

super_space(25)
line_please()
vers_please()
line_please()
print color.BOLD +  "Welcome to NEW and IMPROVED Killa Mo Casino" + color.END
print color.BOLD +  "For updates and features, simply enter 'feat'" + color.END
space()
print color.BOLD +  "Would you like a seat at the BlackJack table? If not, enter 'Man' to view the manual." + color.END



while game == False:
	space()
	card_total = 0
	card_total2 = 0
	table = raw_input("Yes or No ")
	if table == "y":
		print color.BOLD + "----------------------------------------------------------" + color.END
		print color.BOLD +  "Good. We'll get your hand ready." + color.END
		print color.BLUE + "shuffling............." + color.END
		
		space()
		thinking(1)		
		print color.BOLD + "Your first card is a:" + color.END
		card_total = new_card()
		print card_total
		space()
		print color.BLUE +  "Oponent recieved cards....... " + color.END
		space()
		card_total2 = 0
				 
			
			
		
		if card_total2 == int(21):
			print "Wow your opponent got 21, " + color.RED + "You lose!" + color.END
			print "Play again? (Press Enter) "
		thinking(.5)
	
		jugar = False
		while jugar == False:
			while oponent == False:
				card_total2 += new_card()
                        	if card_total2 < 15:
                                	card_total2 += new_card()
                                	oponent = False
                     
                        	else:
                    	            	oponent = True

			hit = raw_input(color.BOLD + "Would you like to hit or stay? " + color.END)
			if hit == "h":
				card = new_card()
				space()
				print "You received a " + color.BOLD + str(card) + color.END + " of " + str(card_letter()) 
				card_total += card
				space()

				if card_total > 21:
					print "total points: " + str(card_total)
					print color.RED + "GAMEOVER!" + color.END + " You're over 21!"
					print "Tough luck, your opponent had " + str(card_total2) + " points!"
					jugar = True
					space()
					again = raw_input("Play again? (Press Enter) ")
				elif card_total == 21:
					print "21! " + color.DARKCYAN + "You Win!!" + color.END
					jugar = True
					space()
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
					space()
			else:
				print "Your final score is " + str(card_total)
				space()
                        	if card_total == card_total2:
					print "You tied! It looks like you're just not good enough!"
					space()
					jugar = True
					print color.BOLD + "Play again? " + color.END
				elif card_total2 > 21:
					print "Your opponent had " + str(card_total2) + ", You automatically win!"
					jugar = True
					space()
					print color.BOLD + "Play again? " + color.END      
                                elif card_total < card_total2:
         				print color.RED + "You lost by " + str(card_total2 - card_total) + " points! You need more practice!"
                   			jugar = True
					space()
					print color.BOLD + "Play again? " + color.END
				elif card_total > card_total2:
					print "Pat yourself on the back! " + color.DARKCYAN + "You beat" + color.END + " your opponent by " + str(card_total - card_total2) + " points!"
					jugar = True
					space()
					print color.BOLD + "Play again? " + color.END	
	elif table == "n":
		print color.BOLD + "Okay, the seat is always open." + color.END
		space()
		space()
		space()
		game = True
		
	elif table == "Man":
		print color.BOLD + "---------------------------------------------------------------------------" + color.END
		print "                                                                                                            "                                                       
                print "                                                                                                            "
		print "                                                                                                            "
		print " The Basic premis of the game is that you are playing a blackjack like game with a computer opponent.                                                                                                           "
		print " When the game begins, you will recieve a card with a value 1 through 11 (1 through Ace). You can hit or stay, depending on how close you are to 21.                                                                                                            "
		print " If you hit 21, you (or even your partner) win automatically. If you go over 21, you will lose autommatically.                                                                                                           "
		print " Your opponent will hit, receive cards, and stay in the 'background'                                                                                                             "
		print "                                                                                                             "
		print "                                                                                                            "
		print "                                                                                                            "
		print " Press Y to play, or N to quit                                                                                                            "
		       
	
	elif table == 'feat':
		super_space(5)
		line_please()
		print "In this version " +  "{" + version + "}" +  " the updates are as follows:"
		space()
		print """*Spaces strategically placed throughout game
*New update menu
*Vastly improved opponent AI
*Each hand now displays not only total points, but new card given (value and suit)"""
		space()
		print "There is also a new set of 'in-code' additions:"
		space()
		print """*Easy way to add spaces
*New suit generator
*Upgraded AI system	
*Ability to 'pause' the exxecution of tasks, therefore artificially simulating things like 'Card Shuffleing'"""
		space()
		print "Any additional updates:"
		space()
		print """*Major bug fixes
*Cleaned up code"""
		super_space(5)
		print "Press Y to play, or N to quit"
	else:
		print color.BOLD + "I'm sorry I didn't quite understand. Start the program again." + color.END
		game = True
