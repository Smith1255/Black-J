#Andrew Smith
#November 9 2014
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

version = str("4.1")
#Used to call version number

def vers_please():
	print "{" + version + "}"
	print "Copyright KM187 App Development"
	print "November 9, 2014"

#Used for copyright header^


#needed for LOGIN[
import pickle

def pickleOut():
	outFile = open("tempdict.txt", "wb") 
        pickle.dump(tempdict, outFile)
        outFile.close()

def pickleIn():
	inFile = open("tempdict.txt", "rb")
	filedict = pickle.load(inFile)
	inFile.close()
	return filedict
pickleIn()

permdict = {}
permdict = pickleIn()

tempdict = permdict


r = ""
loginname = ""

#End of LOGIN]


#Variables[
letter = ""

game = False

oponent = False

card = 0

bank = 100000

player = 100



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
def bank_green():
	return color.GREEN + color.BOLD + " $" + str(bank) + color.END
def user_green():
	return color.GREEN + color.BOLD + " $" + str(player) + color.END

def sav():
	tempdict[loginname] = player
        pickleOut()
def menuPrint():

	line_please()
	vers_please()
	line_please()
	print color.BOLD + color.DARKCYAN + "Welcome to NEW and IMPROVED Killa Mo Casino" + color.END
	print color.BOLD + color.BLUE + "For updates and features, simply enter 'feat'" + color.END
	print color.BOLD + color.BLUE + "For the manual, enter 'man'" + color.END
	print color.BOLD + color.BLUE + "For credits, enter 'credits'" + color.END
	print color.BOLD + color.BLUE + "To quit, type 'quit''" + color.END
	space()
	print color.BOLD + color.BLUE + "To visit the 'Accounts' page, type 'account'"
	space()
	print color.BOLD + color.BLUE + "Mid-Game, you can type 'save' at the main menu option to save your bank progress"
	space()
	print color.BOLD + color.BLUE + "To play simply type 'play'" + color.END
	line_please()
	super_space(2)



while game == False:
#GAME WHILE LOOP
	space()
	card_total = 0
	card_total2 = 0
	bet = 0
	#Resets bet every hand
	betChoice = " "
	betQuit = 0
	#Both variables serve as a card value count throughout hands; put here not in variable class so that they reset each hand
	menuPrint()
	table = raw_input("Enter main menu choice here: ")
	#Yes or No to 'Seat at BlackJack table'

	if table == "play" or table == "p":
		super_space(50)
		print color.BOLD + "----------------------------------------------------------" + color.END
		print color.BOLD +  "Good. We'll get your hand ready." + color.END
		print color.BLUE + "shuffling............." + color.END
		
		
		thinking(1)
		super_space(3)
		line_please()
		choice = ""
		if loginname != "":

			print "You have" + user_green()
			choice = raw_input("Would you like to bet? (Y/N): ")
			betting = False

		if choice == "Y" or choice == "y":
			super_space(50)
			
			if player == 0:
                        	print "You have no money!"
                                print "No bets for you."
                                thinking(1)
				super_space(3)
                                betting = True
                                        #Player has no money, goes to non-betting
		
			super_space(50)

			while betting == False:
			#While loop to determine bet

				bet = raw_input("What are you going to bet?: $")
			
				bet = int(bet)

				if bet > player:
					print "That bet is not allowed"
					bet = 0
					#Entered too high of a bet, resets to beginning of betting section
					betQuit = betQuit + 1
					if betQuit == 3:
						print "Too many false bets. Moving on."
						thinking(1.5)			
						super_space(50)
						betting = True
						#After 3 "false" bets, automatically jumps to non-betting section
				else:
					player = player - bet
					bank = bank + bet
					print "You have $" + str(player)
					#Money is taken from player and put into bank
					print "Thank you"
					print "You have" + user_green() + " left."
					thinking(1)
					line_please()
					super_space(3)
					betting = True
		
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
                                	oponent = False
					#Opponent AI hand logic
                     
                        	elif card_total2 > 15:
					oponent = True

			hit = raw_input(color.BOLD + "Would you like to hit or stay?: " + color.END)
			hit = str.lower(hit)

			if hit == "h" or hit == "hit":
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
					raw_input(color.BOLD + color.RED + "Play again? Press 'Enter' " + color.END)
					super_space(50)
					#GAMEOVER

				elif card_total == 21:
					print "21! " + color.DARKCYAN + "You Win!!" + color.END
					player = player + 2*bet
					bank = bank - 2*bet
					#Orginal bet replaced, then additional bet value added (opposite for bank)
					print "You now have" + user_green()
					hand = True
					raw_input(color.BOLD + color.RED + "Play again? Press 'Enter' " + color.END)
					super_space(50)
					#BLACKJACK

					space()
				else:
					print "total points: " + str(card_total)
					space()
					#No blackjack or gameover, continuation of loop...
			elif hit == "stay" or hit == "s":
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
					raw_input(color.BOLD + color.RED + "Play again? Press 'Enter' " + color.END)
                                        super_space(50)
					#PLAYER TIE
					
				elif card_total2 > 21:
					print "Your opponent had " + str(card_total2) + ", You automatically win!"
					player = player + 2*bet
                                        bank = bank - 2*bet
					#Refer back to 'BlackJack' hand
					print "You now have" + user_green()
					hand = True
					space()
             				raw_input(color.BOLD + color.RED + "Play again? Press 'Enter' " + color.END)
					super_space(50)
					#OPPONENT GAMEOVER	
	      
                                elif card_total < card_total2:
         				print color.RED + "You lost by " + str(card_total2 - card_total) + " points! You need more practice!" + color.END
                   			hand = True
					space()
					raw_input(color.BOLD + color.RED + "Play again? Press 'Enter' " + color.END)
					super_space(50)
					#PLAYER LOSS

				elif card_total > card_total2:
					print "Pat yourself on the back! " + color.DARKCYAN + "You beat" + color.END + " your opponent by " + str(card_total - card_total2) + " points!"
					player = player + 2*bet
                                        bank = bank - 2*bet
					#Refer back to 'BlackJack' hand
					print "You now have" + user_green()
					hand = True
					space()
					raw_input(color.BOLD + color.RED + "Play again? Press 'Enter'" + color.END)
					super_space(50)
					#PLAYER WIN	
	elif table == "quit":
	#NO TO SEAT AT TABLE
		super_space(50)
		print color.BOLD + "Okay, the seat is always open." + color.END
		super_space(3)
		game = True
	
	elif table == "bank inquiry" or table == "bi":
		print bank_green()
		#Allows player to check casino funds

	elif table == "personal inquiry" or table == "pi":
                print user_green()
		#Allows player to check personal funds

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
		print " To check bank (casino) funds, type 'bank inquiry' or 'bi' at ""What would you like do do?: "" prompt"
		print " To check bank (personal) funds, type 'personal inquiry' or 'pi' at ""What would you like do do?: "" prompt"
		space()
		print " In order to bet, select 'Y' at bet screen, and enter an amount that is less than total funds"
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
			*Scrolling text
			*Accounts and universal banking
			*Betting
			*Ability to creat and delete accounts
			*New account menu"""
		#UPDATES^
		space()
		
		print color.BOLD + "There is also a new set of 'in-code' additions:" + color.END
		
		space()
		
		print """
			*Easy way to add spaces
			*New suit generator
			*Upgraded AI system	
			*Ability to 'pause' the exxecution of tasks, therefore artificially simulating things like 'Card Shuffleing'
			*Code is Commented
			*Pickling
			*Account management"""
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

	elif table == 'save':
		sav()
		print tempdict[loginname]
		print "Account info saved."

	elif table == 'account':
		
		super_space(50)

		#User chooses "accounts" at initial menu
		accountMenuLoop = False
	
		while accountMenuLoop == False:
			print color.BOLD + "Here you can create and account, log in to an account, or delete an account" + color.END
        		space()
			account_choice = raw_input("What would you like to do: ")
        		account_choice = str.lower(account_choice)
 			super_space(50)                        

         		if account_choice == "c" or account_choice == "create":
                		r = raw_input("What is your name?: ")
                		r = str.lower(r)
                		tempdict[r] = 100
			
                		print "Okay, " + r + ", You have $" + str(tempdict[r])
                		pickleOut()
				
				thinking(1.5)
                		loginname = r
				super_space(50)
	
        		elif account_choice  == "l" or account_choice == "log" or account_choice == "login" or account_choice == "log in":
                		loginname = raw_input("What is the account name?: ")
                		loginname = str.lower(loginname)
				super_space(50)

				if loginname not in tempdict:
					print color.RED + "No account by that name, going to account menu" + color.END
				
					space()
				else:
					print tempdict[loginname]
	
                			player = tempdict[loginname]
                			print "Ok, You have $" + str(player) + " In your bank account."
               				
					thinking(1.5)
                                	super_space(50)

					accountMenuLoop = True

        		elif account_choice == "clear" or account_choice == "delete" or account_choice == "d":
                		delAccount = False

				while delAccount == False:

					delchoice = raw_input("Do you want to clear all or delete one account?(Clear/Delete): ")
                			delchoice = str.lower(delchoice)
					
					if delchoice == "c" or delchoice == "clear":
						isok = raw_input(color.BOLD + "Are you sure? (Y/N): " + color.END)
                        			isok = str.lower(isok)
						if isok == "y" or isok == "yes":
                               	 			
							tempdict = {}
                                			print "Names Cleared"
							thinking(1.5)
                                			super_space(50)
                               				
							delAccount = True

							pickleOut()

                			elif delchoice == "d" or delchoice == "delete":
                        			print "All accounts:"
                        			for key in tempdict:
                                			print key
                        			deleteName = raw_input("Ok, Enter a name to delete: ")
                        			deleteName = str.lower(deleteName)
                        			
						if deleteName is int:
                                			print "That is not a name"
                        			for name in tempdict:
                                			if deleteName in tempdict:
                                        			del tempdict[deleteName]
								print deleteName + " Deleted"
								super_space(50)
                                        			break
                                			else:
                                         			if str.lower(deleteName) not in tempdict:
                                                			print "No account by that name"
                                                			break
						delAccount = True
					else:
						print "Didnt quite understand that."
						super_space(5)
        		elif account_choice == "done":
                		accountMenuLoop = True
        		else:
                		print "Sorry didn't quite get that"
                		print "Going back to main menu"
                		accountMenuLoop = True
				
	else:
	#NO YES/NO/MAN/FEAT CHOSEN
		super_space(50)
		print color.BOLD + "I'm sorry I didn't quite understand. Start the program again." + color.END
		super_space(2)
		pickleOut()
		game = True
