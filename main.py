import random
from colorama import Fore, Style
import time

player1Card = []
player2Card = []

cardtypelist = ["Cœur", "Pique", "Trêfle", "Carré"]
cardlist = []

def translate(card):
	cardnumber = card.split(" ")[0]
	cardtype = card.split(" ")[1]

	if (int(cardnumber) == 1):
		value = "As"
	elif (int(cardnumber) == 11):
		value = "Valet"
	elif (int(cardnumber) == 12):
		value = "Dame"
	elif (int(cardnumber) == 13):
		value = "Roi"
	else:
		value = cardnumber

	if (cardtype == "Cœur" or cardtype == "Carré"):
		cardtype = f"{Fore.RED}{cardtype}"
	else:
		cardtype = f"{Fore.BLACK}{cardtype}"

	return f"{value} {cardtype}{Fore.RESET}"

def game(card1, card2):
	cardnumber1 = card1.split(" ")[0]
	cardnumber2 = card2.split(" ")[0]

	if (cardnumber1 == cardnumber2):
		return 0
	else:
		if (int(cardnumber1) == 1):
			return 1
		elif (int(cardnumber2) == 1):
			return 2
		else:
			if (cardnumber1 > cardnumber2):
				return 1
			else:
				return 2

def display():
	if (len(player1Card) > len(player2Card)):
		count = len(player1Card)
	else:
		count = len(player2Card)

	print(f"{Fore.CYAN}Joueur 1\t\tJoueur 2{Fore.RESET}")
	for i in range(count):
		space = "\t\t\t"
		if (i < len(player1Card)):
			value1 = translate(player1Card[i])
			if (len(player1Card[i]) > 7):
				space = "\t\t"
		else:
			value1 = ""
		if (i < len(player2Card)):
			value2 = translate(player2Card[i])
		else:
			value2 = ""

		print(f"{value1}{space}{value2}")

	print()

def gaincard(player, card1, card2, temp):
	rdm = random.randint(1, 2)
	if (rdm == 1):
		player.append(card1)
		player.append(card2)
	else:
		player.append(card2)
		player.append(card1)

	if (len(temp) > 0):
		for card in temp:
			player1Card.append(card)
			temp.remove(card)

for type in cardtypelist:
	for i in range(13):
		cardlist.append(f"{i+1} {type}")

cardcount = len(cardlist)

while (len(cardlist) > 0):
	card1 = random.choice(cardlist)
	player1Card.append(card1)
	cardlist.remove(card1)

	card2 = random.choice(cardlist)
	player2Card.append(card2)
	cardlist.remove(card2)

display()

temp = []
turn = 0
start = time.time()

while True:
	turn = turn +1
	if (len(player1Card) == 0):
		print(f"{Fore.YELLOW} Gagant : Joueur 2 ({turn} tours - {round((time.time() - start)*1000)}ms)")
		break
	if (len(player2Card) == 0):
		print(f"{Fore.YELLOW} Gagant : Joueur 1 ({turn} tours - {round((time.time() - start)*1000)}ms)")
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

	display()
