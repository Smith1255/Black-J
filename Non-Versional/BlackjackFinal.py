#COMMENT ADDED ON OCTOBER 7 2015 -------------------------------*
#This was the first version two - first add-on since 'blackjack33' 
#November 4 2014
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
print color.BOLD +  "----------------------------------------------------------" + color.END
print color.BOLD +  "Would you like a seat at the table?" + color.END
import random
def new_card():
	return random.randint(1, 11)
game = False
while game == False:
	card_total = 0
	table = raw_input("Yes or No ")
	if table == "y":
		print color.BOLD + "----------------------------------------------------------" + color.END
		print color.BOLD +  "Good. We'll get your hand ready." + color.END
		print "shuffling............."
		print color.BOLD + "Your first card is a:" + color.END
		card_total = new_card()
		print card_total
		
		jugar = False
		while jugar == False:
			hit = raw_input(color.BOLD + "Would you like to hit or stay? " + color.END)
			if hit == "h":
				card_total = card_total + new_card()
				if card_total > 21:
					print card_total
					print "GAMEOVER! You're over 21!"
					jugar = True
					again = raw_input("Play again? (Press Enter) ")
				elif card_total == 21:
					print "21! You Win!!"
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
					print card_total
			else:
				print "Your final score is: "
				print card_total 
                        	jugar = True
				game = True      
                                         		
                   
	
	elif table == "n":
		print color.BOLD + "Okay, the seat is always open." + color.END
		game = True
	else:
		print color.BOLD + "I'm sorry I didn't quite understand. Start the program again." + color.END
		game = True
