
import random

win_combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

def check_board(spaces):
	for x in win_combos:
		if spaces[x[0]] == spaces[x[1]] == spaces[x[2]] == "X":
			print("Player 1 wins")
			return True
		elif spaces[x[0]] == spaces[x[1]] == spaces[x[2]] == "O":
			print_board(spaces)
			print("Player 2 wins")
			return True
	if " " not in spaces:
		print("Game ends in a tie")
		return True

	return False

def print_board(spaces):
	print("Board")
	print("%s | %s | %s" % (spaces[0], spaces[1],spaces[2]))
	print("---------")
	print("%s | %s | %s" % (spaces[3], spaces[4],spaces[5]))
	print("---------")
	print("%s | %s | %s" % (spaces[6], spaces[7],spaces[8]))


def get_input(spaces):
	# user_input = false;
	while True:
		try:
			num = int(raw_input("Enter move (1 - 9)>> "))
		except ValueError:
			print("That wasn't a number")
		else:
			if num > 9 or num < 1 or spaces[num -1] != " ":
				print("Invalid selection")
			else:
				spaces[num -1] = "X"
				break;
def ai_turn(spaces):
	while True:
		selection = random.randint(0,8)
		if spaces[selection] == " ":
			spaces[selection] = "O"
			break;	

def play_again():
	while True:
		try:
			val = raw_input("Play again y/n?>>")
		except ValueError:
			print("Invalid entry")
		else:
			if val == "Y" or val == "y":
				return True
			elif val == "N" or val == "n":
				return False
			else:
				print("Invalid entry")



def main():
	while True:
		spaces = [" " for i in range(9)]
		while check_board(spaces) == False:
			print_board(spaces)
			get_input(spaces)
			if check_board(spaces) == True:
				break;
			ai_turn(spaces)
		if play_again() == False:
			print("Thanks for playing!")
			break;

if __name__ == "__main__":
    main()