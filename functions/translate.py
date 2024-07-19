from colorama import Fore

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
