import random
while True:
	myWord = input("Type the word, type random for a random word: ")
	randomWord = ["jazz", "jail", "scratch", "smell", "apple", "water", "honey", "river", "random", "happy", "smile", "cheer", "avacado", "orange", "word", "desert", "dazzle", "mirage", "saloon", "dust", "hill", "sand", "metropolis", "misisippi", "oil", "ocean", "emerald", "green", "chemical", "plant", "marble", "spring", "yard", "labrynth", "star", "light", "scrap", "brain", "aquatic", "ruin", "casino", "night", "top", "mystic", "cave", "sky", "chase", "wing", "fortress", "death", "egg", "palm", "tree", "panic", "colision", "chaos", "tidal", "tempest", "quartz", "quadrant", "wacky", "work", "bench", "workbench", "stardust", "dust", "speedway", "speed", "way", "metalic", "madness", "metal", "mad", "angel", "island"]
	if myWord == "random":
		myWord = random.choice(randomWord)
	else:
		pass
	score = 0
	attempts = input("How many attempts do you want before guessing? ")
	for x in range(int(attempts)):
		letter = input("Guess a letter: ")
		if letter in myWord:
			print(letter + " is in the word")
		else:
			print(letter + " is not in the word.")
		count = 1
		for l in myWord:
			if l == letter:
				print(count)
				count += 1
	choise = input("Guess the word: ")
	if choise == myWord:
		print("We have a winner!")
		score = score + 1
	else:
		print("sorry no good.")
		print("The word was: " + myWord)