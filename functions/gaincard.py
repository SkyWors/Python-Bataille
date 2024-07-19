import random

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
			player.append(card)
			temp.remove(card)
