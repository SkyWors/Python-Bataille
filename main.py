import random
import time
from colorama import Fore
from functions.translate import translate
from functions.game import game
from functions.display import display
from functions.gaincard import gaincard
from functions.createcard import createcard

player1Card = []
player2Card = []
temp = []
turn = 0
start = time.time()

cardlist = createcard()

while (len(cardlist) > 0):
	card1 = random.choice(cardlist)
	player1Card.append(card1)
	cardlist.remove(card1)

	card2 = random.choice(cardlist)
	player2Card.append(card2)
	cardlist.remove(card2)

display(player1Card, player2Card)

while True:
	turn +=1

	if (len(player1Card) == 0):
		print(f"{Fore.YELLOW} Gagnant : Joueur 2 ({turn} tours - {round((time.time() - start)*1000)}ms)")
		break
	if (len(player2Card) == 0):
		print(f"{Fore.YELLOW} Gagnant : Joueur 1 ({turn} tours - {round((time.time() - start)*1000)}ms)")
		break

	print (f"{Fore.YELLOW}Game :{Fore.RESET} " + translate(player1Card[0]) + "\t\t" + translate(player2Card[0]) + "\n")

	card1 = player1Card[0]
	card2 = player2Card[0]
	player1Card.remove(player1Card[0])
	player2Card.remove(player2Card[0])

	win = game(card1, card2)

	if (win == 0):
		temp.append(card1)
		temp.append(card2)

	if (win == 1):
		gaincard(player1Card, card1, card2, temp)

	if (win == 2):
		gaincard(player2Card, card1, card2, temp)

	display(player1Card, player2Card)
