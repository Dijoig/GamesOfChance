import random

money = 100
#Write your game of chance functions here

#Heads o Tails function, the player can choose head or tails and will win base on a 50% probability
def heads_or_tails(amount, choice):
	print("YOU ARE PLAYING HEADS OR TAILS!!")
	choice = choice.lower()
	if (amount <= 0 or amount > money or (choice not in ["heads", "tails"])):
		print("You have to bet on a positive number equal or less your total money. The options to bet are heads or tails!")
		return

	randFactor = random.randint(1,2)
	result = ""
	if (randFactor == 1):
		result = "heads"
	else:
		result = "tails"
	print("The coin flips....")
	print("It is... " + result + "!!!!!")
	print("You chose " + choice)
	if (choice != result):
		amount *= -1
		print("You lost " + str(amount))
	else:
		print("You won " + str(amount))
	print("Total money is now " + str(money + amount))
	return amount

#ChoHan function simulate the game where two dices are thrown and the player bet if the sum will be even or odd
def cho_han(amount, choice):
	print("YOU ARE PLAYING CHO-HAN!!")
	choice = choice.lower()
	if (amount <= 0 or amount > money or (choice not in ["odd", "even"])):
		print("You have to bet on a positive number equal or less your total money. The options to bet are even or odd!")
		return

	dice1 = random.randint(1, 6)
	dice2 = random.randint(1, 6)
	result = ""
	sum = dice1 + dice2
	print("Dice one rolls for: " + str(dice1))
	print("Dice two rolls for: " + str(dice2))
	print("The sum is: " + str(sum))
	print("You chose " + choice)


	if (sum % 2 == 0):
		result = "even"
	else:
		result = "odd"

	if (choice != result):
		amount *= -1
		print("You lost " + str(amount))
	else:
		print("You won " + str(amount))
	print("Total money is now " + str(money + amount))
	return amount


#draw_from_deck function will simulate two players drawing a card from a deck of cards, the higher card wins!
def draw_from_deck(amount):
	print("YOU ARE PLAYING DRAW FROM DECK!!")
	if (amount <= 0 or amount > money):
		print("You have to bet on a positive number equal or less your total money.")
		return

	deck = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 11, 12, 13, 
		1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 11, 12, 13]

	player_pick = random.randint(0, len(deck)-1)
	player_card = deck[player_pick]
	deck.pop(player_pick)
	opponent_pick = random.randint(0, len(deck)-1)
	opponent_card = deck[opponent_pick]
	print("You draw " + str(player_card))
	print("Your opponent picked " + str(opponent_card))

	if (player_card < opponent_card):
		amount *= -1
		print("You lost...You loose " + str(amount))
	elif (player_card == opponent_card):
		amount = 0
		print("it's a draw! No one wins...")
	else:
		print("You won!! You profit is " + str(amount))
	print("Total money is now " + str(money + amount))
	return amount

#roulette function will simulate a game of roulette
def roulette(amount, choice):
	print("YOU ARE PLAYING ROULETTE!!")
	if (amount <= 0 or amount > money):
		print("Invalid choice or amount. Make sure your amount is positive and you have enough money for it. Make sure you choose odd or even or a number between 0-36")
		return
	if (type(choice) == str):
		choice = choice.lower()
		if (choice.lower() not in ["even", "odd"]):
			print("Invalid choice or amount. Make sure your amount is positive and you have enough money for it. Make sure you choose odd or even or a number between 0-36")
			return
	if (type(choice) == int):
		if (choice < 0 or choice > 36):
			print("Invalid choice or amount. Make sure your amount is positive and you have enough money for it. Make sure you choose odd or even or a number between 0-36")
			return

	roulette_double_0 = list(range(0, 38)) + [0]
	crupier_factor = random.randint(0, 37)
	crupier_roll = roulette_double_0[crupier_factor]
	print("The crupier rolled " + str(crupier_roll))
	print("You chose " + str(choice))
	
	if (type(choice) == str):
		if (crupier_roll == 0):
			amount *= -1
			print("Bad luck, the dice hit 0... You loose " + str(amount))
		elif (crupier_roll % 2 == 0):
			if (choice == "even"):
				print("You won! Profit: " + str(amount))
			else:
				amount *= -1
				print("Bad luck... You losse " + str(amount))
		else:
			if (choice == "odd"):
				print("You won! Profit: " + str(amount))
			else:
				amount *= -1
				print("Bad luck... You losse " + str(amount))
	elif (type(choice) == int):
		if (choice == crupier_roll):
			amount *= 35
			print("You did it! Got the jackpot... You win " + str(amount))
		else:
			amount *= -1
			print("Bold try... No luck though, you loose " + str(amount))
	print("Your money is now " + str(money + amount))
	return amount
			
		


			




	

		





#Call your game of chance functions here
money += heads_or_tails(5, "heads")
print("")
money += heads_or_tails(7, "tails")
print("")
money += cho_han(18, "EVEN")
print("")
money += cho_han(11, "odD")
print("")
money += draw_from_deck(15)
print("")
money += draw_from_deck(3)
print("")
money += roulette(22, 2)
print("")
money += roulette(22, "odd")
print("")
money += roulette(22, "even")




















#Should go fine:
#heads_or_tails(22, "heads")
#heads_or_tails(22, "tails")

#Should raise warning:
#heads_or_tails(-22, "heads")
#heads_or_tails(222, "heads")
#heads_or_tails(22, "heaqeqweqsadws")

#Should go fine:
#cho_han(77, "EVEN")
#cho_han(23, "odD")

#Should raise warning:
#cho_han(-1, "even")
#cho_han(2222, "even")
#cho_han(11, "oafefqweqwesdwd")

#Should be fine:
#draw_from_deck(88)
#draw_from_deck(22)

#Should raise warnings:
#draw_from_deck(-22)
#draw_from_deck(10111)

#Should raise warnings:
#roulette(222, "odd")
#roulette(-22, "odd")
#roulette(10, "oadwqdwqdsadd")
#roulette(10, -2)
#roulette(10, 4444)

#Should be fine:
#roulette(10, "eVen")
#roulette(10, "oDd")
#roulette(10, 0)
#roulette(10, 24)

