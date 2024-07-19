from colorama import Fore
from functions.translate import translate

def display(player1, player2):
	if (len(player1) > len(player2)):
		count = len(player1)
	else:
		count = len(player2)

	print(f"{Fore.CYAN}Joueur 1\t\tJoueur 2{Fore.RESET}")
	for i in range(count):
		space = "\t\t\t"
		if (i < len(player1)):
			value1 = translate(player1[i])
			if (len(player1[i]) > 7):
				space = "\t\t"
		else:
			value1 = ""
		if (i < len(player2)):
			value2 = translate(player2[i])
		else:
			value2 = ""

		print(f"{value1}{space}{value2}")

	print()
