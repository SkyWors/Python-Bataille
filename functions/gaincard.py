import random

def gaincard(player, card1, card2, temp):
	rdm = random.randint(1, 2)
	if (rdm == 1):
		player.append(card1)
		player.append(card2)
	else:
		player.append(card2)
		player.append(card1)

	while temp:
		card = temp.pop(0)
		player.append(card)
