from random import randint
board = []

for x in range(10):
	board.append(["O"] * 10 )

def print_board(board):
	for space in board:
		print " ".join(space)

print_board(board)
print "Let's play battleship!"

def small_random(board):
	return [randint(0,len(board[0]) - 1),randint(0,len(board) - 1)]

smallships = []

for x in range(4):
	smallships.append(small_random(board))

print smallships

for x in range(11):
	if x == 10:
		print "Game over!"
		break
	print "This is turn", x + 1
	guess_col = int(raw_input("Guess Col:"))
	guess_row = int(raw_input("Guess Row:"))
	guess = [guess_col,guess_row]
	if guess_col not in range(10) or\
	   guess_row not in range(10):
		   print "That's not even in the range!"
	elif guess in smallships and len(smallships) == 1:
		print "You have sunk all the battleships!"
		break
	elif board[guess[1]][guess[0]] == "X" or \
		 board[guess[1]][guess[0]] == "A":
			 print "You have hit there before!"
	elif guess in smallships:
		board[guess[1]][guess[0]] = "A"
		smallships.remove(guess)
		print_board(board)
		print "You hit a small battleship!"
	else:
		board[guess[1]][guess[0]] = "X"
		print_board(board)
		print "You don't hit anything~ orz"
	x = x + 1




