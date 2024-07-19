def createcard():
	cardtypelist = ["Cœur", "Pique", "Trêfle", "Carré"]
	cardlist = []

	for type in cardtypelist:
		for i in range(13):
			cardlist.append(f"{i+1} {type}")

	return cardlist
