import time
from colorama import Fore
from functions.translate import translate
from functions.check import check
from functions.gaincard import gaincard
from functions.display import display

def worker(player1, player2):
	temp = []
	turn = 0
	start = time.time()

	while True:
		turn +=1

		if (len(player1) == 0):
			print(f"{Fore.YELLOW} Gagnant : Joueur 2 ({turn} tours - {round((time.time() - start)*1000)}ms)")
			break
		if (len(player2) == 0):
			print(f"{Fore.YELLOW} Gagnant : Joueur 1 ({turn} tours - {round((time.time() - start)*1000)}ms)")
			break

		card1 = player1[0]
		card2 = player2[0]
		player1.remove(player1[0])
		player2.remove(player2[0])

		win = check(card1, card2)

		if (win == 0):
			temp.append(card1)
			temp.append(card2)

		if (win == 1):
			gaincard(player1, card1, card2, temp)

		if (win == 2):
			gaincard(player2, card1, card2, temp)

		print (f"{Fore.YELLOW}Game :{Fore.RESET} " + translate(card1) + "\t\t" + translate(card2) + "\n")
		display(player1, player2)
