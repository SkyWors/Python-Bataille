from functions.display import display
from functions.createcard import createcard
from functions.givecard import givecard
from functions.worker import worker

if __name__ == "__main__":
	player1 = []
	player2 = []

	givecard(createcard(), player1, player2)

	display(player1, player2)

	worker(player1, player2)
