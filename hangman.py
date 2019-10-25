import random
while True:
	myWord = input("Type the word, leave blank for a random word: ")
	randomWord = ["jazz", "jail", "scratch", "smell", "apple", "water", "honey", "river", "random", "happy", "smile", "cheer", "avacado", "orange", "word", "desert", "dazzle", "mirage", "saloon", "dust", "hill", "sand", "metropolis", "misisippi", "oil", "ocean", "emerald", "green", "chemical", "plant", "marble", "spring", "yard", "labrynth", "star", "light", "scrap", "brain", "aquatic", "ruin", "casino", "night", "top", "mystic", "cave", "sky", "chase", "wing", "fortress", "death", "egg", "palm", "tree", "panic", "colision", "chaos", "tidal", "tempest", "quartz", "quadrant", "wacky", "work", "bench", "workbench", "stardust", "dust", "speedway", "speed", "way", "metalic", "madness", "metal", "mad", "angel", "island", "hydro", "city", "garden", "carnival", "ice", "cap", "launch", "base", "mushroom", "valley", "flying", "fly", "battery", "lava", "reef", "hidden", "palace", "sanctuary", "doomsday", "doom", "day", "highway", "escape", "seaside", "sea", "side", "crisis", "rooftop", "roof", "run", "planet", "wisp", "studio", "super", "press", "titanic", "monarch", "reverie", "hyper", "ultimate", "technology", "the", "or", "and", "if", "not", "sorry", "cant", "repeat", "but", "burn", "to", "ash", "please", "thank", "you", "diamond", "ruby", "saphire", "gem", "stone", "jewel", "gypsy", "gold", "silver", "bronze", "tide", "iceberg", "wolf", "wet", "see", "alpha", "beta", "omega"]
	if myWord == "":
		myWord = random.choice(randomWord)
	else:
		pass
	Word = myWord
	myWord = list(myWord)
	letters = len(myWord)
	guessList = list("_" * letters)
	score = 0
	attempts = input("How many attempts do you want before guessing? (I recommend 8) ")
	print(guessList)
	for x in range(int(attempts)):
		guess = input("Guess a letter: ")
		index = 0
		for letter in myWord:
			if letter == guess:
				guessList[index] = guess
			index += 1
		print(guessList)
	choise = input("Guess the word: ")
	if choise == Word:
		print("We have a winner!")
		print("The word was indeed " + Word + ".")
		score = score + 1
	else:
		print("sorry no good.")
		print("The word was: " + Word)
	playAgain = input("Do you want to play again? y/n ")
	if playAgain == "y":
		pass
	elif playAgain == "n":
		print("Thanks for playing!")
		break
	else:
		print("Error: " + playAgain + " was not a choice")
		print("Interpreting vauge answer as: n")
		break
