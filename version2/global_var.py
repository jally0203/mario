
# global variables

#layout
bets = []
digitsH = []
digitsL = []
creditDigit = None
winDigit = None
lights = []
# matrix
betImgs = ['dog.png', 'man.png', 'dog.png', 'man.png', 'dog.png', 'man.png', 'dog.png', 'man.png']
awards = [5, 10, 15, 20, 20, 30, 40, 100]
keys = ['8', '7', '6', '5', '4', '3', '2', '1']
awards = [15, 20, 2, 0, 5, 2, 10, 20, 2, 40, 5, 2, 15, 30, 2, 0, 5, 2, 10, 20, 50, 100, 25, 5]
types = [5, 3, 3, 0, 7, 6, 6, 4, 1, 1, 7, 5, 5, 2, 2, 0, 7, 6, 6, 4, 0, 0, 0, 7]
# STM
state = 0
reset_flag = False
# bet and win
playBet = []
credit = 10
win = 0
comparing_bet = 0
# control
curLight = 0
