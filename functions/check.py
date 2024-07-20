def check(card1, card2):
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
