import random

def givecard(cards, player1, player2):
	while (len(cards) > 0):
		card1 = random.choice(cards)
		player1.append(card1)
		cards.remove(card1)

		card2 = random.choice(cards)
		player2.append(card2)
		cards.remove(card2)
