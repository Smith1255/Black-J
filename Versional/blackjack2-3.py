#Andrew Smith
#November 6 2014
from sys import exit
import string

import time
import random


class color:	
	BLUE = '\033[94m'
	RED = '\033[91m'
 	GREEN = '\033[92m'
 	BOLD = '\033[1m'
 	UNDERLINED = '\033`[4m'
 	END = '\033[0m'
	DARKCYAN = '\033[36m'
#Colors for use in text^

version = str("2.3")
#Used to call version number

def vers_please():
	print "{" + version + "}"
	print "Copyright KM187 App Development"
	print "November 5, 2014"

#Used for copyright header

#Variables[
letter = ""

game = False

oponent = False

card = 0

#Variable End]

#Functions[
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
        print ""
#used to create blank lines

def super_space(x):
	count = x
	while count > 0:
		space()
		count = count - 1
#used for creating x blank lines

def line_please():
	print color.BOLD + "-"*50 + color.END
#creates uniform dotted line

def thinking(x):
        time.sleep(x)
#Delays execution time

def side_scroll():
	super_space(2)
	thinking(1)

#Function end]


super_space(50)
line_please()
vers_please()
line_please()
print color.BOLD + color.DARKCYAN + "Welcome to NEW and IMPROVED Killa Mo Casino" + color.END
print color.BOLD + color.BLUE + "For updates and features, simply enter 'feat'" + color.END
print color.BOLD + color.BLUE + "For the manual, enter 'man'" + color.END
print color.BOLD + color.BLUE + "For credits, enter 'credits'" + color.END
print color.BOLD + color.BLUE + "To quit, type 'quit''" + color.END
space()
print color.BOLD + color.BLUE + "To play simply type 'play'" + color.END
line_please()
super_space(2)



while game == False:
#GAME WHILE LOOP
	space()
	card_total = 0
	card_total2 = 0
	#Both variables serve as a card value count throughout hands; put here not in variable class so that they reset each hand
	table = raw_input("What would you like do do?: ")
	#Yes or No to 'Seat at BlackJack table'

	if table == "play":
		super_space(50)
		print color.BOLD + "----------------------------------------------------------" + color.END
		print color.BOLD +  "Good. We'll get your hand ready." + color.END
		print color.BLUE + "shuffling............." + color.END
		
		
		thinking(1)
		super_space(3)
		line_please()
		
		print color.BOLD + "Your first card is a:" + color.END
		card_total = new_card()
		print str(card_total) + " of " + card_letter()
		#First User Card

		space()
		print color.BLUE +  "Oponent recieved cards....... " + color.END
		space()
		thinking(.5)
	
		hand = False
		
		while hand == False:
		#ALL PLAYERS HAND WHILE LOOP	
						
			while oponent == False:
			#OPPONENT HAND WHILE LOOP
				
				card_total2 += new_card()
                        	if card_total2 < 15:
                                	card_total2 += new_card()
                                	oponent = False	
					#Opponent AI hand logic
                     
                        	else:
                    	            	oponent = True
					#End of oppenent's hand

			hit = raw_input(color.BOLD + "Would you like to hit or stay? ('Enter' will stay') " + color.END)
			
			if hit == "h" or hit == "hit" or hit == "Hit" or hit == "HIT":
				super_space(50)
				print color.BOLD + "HIT" + color.END
				super_space(2)
				card = new_card()
				print "You received a " + color.BOLD + str(card) + color.END + " of " + str(card_letter()) 
				card_total += card
				space()
				
				if card_total > 21:
					print "total points: " + str(card_total)
					print color.RED + "GAMEOVER!" + color.END + " You're over 21!"
					print "Tough luck, your opponent had " + str(card_total2) + " points!"
					hand = True
					space()
					again = raw_input("Play again? (Press Enter) ")
					#GAMEOVER

				elif card_total == 21:
					print "21! " + color.DARKCYAN + "You Win!!" + color.END
					hand = True
					#BLACKJACK

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
					#No blackjack or gameover, continuation of loop...
			else:
			#User chose to 'Stay'
				super_space(50)
				print color.BOLD + "STAY" + color.END
                                super_space(2)
				print "Your final score is " + str(card_total)
				space()
                                
                                #RESULTS:
	
                        	if card_total == card_total2:
					print "You tied! It looks like you're just not good enough!"
					hand = True
					space()
					print color.BOLD + "Play again? " + color.END
                                        #PLAYER TIE
					
				elif card_total2 > 21:
					print "Your opponent had " + str(card_total2) + ", You automatically win!"
					hand = True
					space()
             				print color.BOLD + "Play again? " + color.END
					#OPPONENT GAMEOVER	
	      
                                elif card_total < card_total2:
         				print color.RED + "You lost by " + str(card_total2 - card_total) + " points! You need more practice!"
                   			hand = True
					space()
					print color.BOLD + "Play again? " + color.END
					#PLAYER LOSS

				elif card_total > card_total2:
					print "Pat yourself on the back! " + color.DARKCYAN + "You beat" + color.END + " your opponent by " + str(card_total - card_total2) + " points!"
					hand = True
					space()
					print color.BOLD + "Play again? " + color.END
					#PLAYER WIN	
	elif table == "quit":
	#NO TO SEAT AT TABLE
		super_space(50)
		print color.BOLD + "Okay, the seat is always open." + color.END
		super_space(3)
		game = True
		
	elif table == "Man" or table == "man":
	#MANUAL
		line_please()
		super_space(50)
		print color.BOLD + color.RED + "MANUAL" + color.END
		print " The Basic premis of the game is that you are playing a blackjack like game with a computer opponent."
		print " When the game begins, you will recieve a card with a value 1 through 11 (1 through Ace). You can hit or stay, depending on how close you are to 21."
		print " If you hit 21, you (or even your partner) win automatically. If you go over 21, you will lose autommatically."
		print " Your opponent will hit, receive cards, and stay in the 'background'"
		print " The object of the game is to get the higher point value, as close to 21 without going over."
		space()
		print " When the game asks for user input, such as 'Play again? Y/N', the system will accept uppercase and lowercase"
		space()
		print " Betting will be implemented in the future"
		super_space(3)
		print " Press Y to play, or N to quit"
		       
	
	elif table == 'feat':
	#UPDATES
		super_space(50)
		line_please()
		
		print color.BOLD + "In this version " +  "{" + version + "}" +  " the updates are as follows:" + color.END
		space()
		print """
			*Spaces strategically placed throughout game
			*New update menu
			*Vastly improved opponent AI
			*Each hand now displays not only total points, but new card given (value and suit)
			*Credits Page
			*Scrolling text"""
		#UPDATES^
		space()
		
		print color.BOLD + "There is also a new set of 'in-code' additions:" + color.END
		
		space()
		
		print """
			*Easy way to add spaces
			*New suit generator
			*Upgraded AI system	
			*Ability to 'pause' the exxecution of tasks, therefore artificially simulating things like 'Card Shuffleing'
			*Code is Commented"""
		#INCODE^
		
		space()
		
		print color.BOLD + "Any additional updates:" + color.END
		space()
		print """
			*Major bug fixes
			*Cleaned up code"""
		#EXTRAS
		line_please()
	
		super_space(5)
		print "Press Y to play, or N to quit"
	
	elif table == 'credits':
		super_space(50)
		print color.BOLD + "CREDITS" + color.END
		side_scroll()
		line_please()
		print color.BOLD + "Developing done in KM187 labs, Mansfield Massachusetts" + color.END
		side_scroll()
		print "Development headed by:"
		side_scroll()
		print color.BOLD + "JACK MACVICAR" + color.END
		side_scroll()
		print color.BOLD + "ANDREW SMITH" + color.END
		side_scroll()
		print "Current version: "
		side_scroll()
		print version
		side_scroll()
		print "Conception:"
		side_scroll()
		print "January, 2014"
		side_scroll()
		print color.BOLD +  "Special Thanks:" + color.END
		side_scroll()
		print "Ryan Roche, project inspiration"
		side_scroll()
		print "CodeAcademy, project knowledge"
		side_scroll()
		print "KillaMo, company inspiration"
		side_scroll()
		print "Jake Tryder, company cheerleader"
		side_scroll()
		print color.BOLD + "Written in:" + color.END
		side_scroll()
		print "Python 2.7.4, Unix"
		side_scroll()
		print "Copyright KM187 2014"
		side_scroll()
		print color.BOLD + "KILLA?" + color.END
		side_scroll()
		print color.BOLD + "MO!" + color.END
		side_scroll()
		line_please()
		side_scroll()
		line_please()
		side_scroll()
		print "0     0  0    0           "
		thinking(.5) 
		print "0    0  0 0  0 0          "
		thinking(.5)
		print "0   0  0   00   0         "
		thinking(.5)
		print "0  0  0    00    0        "
		thinking(.5)
		print "0 0                       "
		thinking(.5)
		print "00   0            0       "
		thinking(.5)
		print "0 0                       "
		thinking(.5)
		print "0  00              0      "
		thinking(.5)
		print "0   0                     "
		thinking(.5)
		print "0  0 0              0     "
		thinking(.5)
		print "0     0                   "
		thinking(.5)
		print "0 0    0             0    "
		side_scroll()
		line_please()
		side_scroll()
		line_please()
		side_scroll()
		print "Play?:"
	else:
	#NO YES/NO/MAN/FEAT CHOSEN
		super_space(50)
		print color.BOLD + "I'm sorry I didn't quite understand. Start the program again." + color.END
		super_space(2)
		game = True
