# create board
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

player = 'O'
bot = 'X'


# all possible winning moves which are 8 moves in a 2d matrix 3x8
def winnings(board):
    wins = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    return wins


print("board positions:")
print("[0][0], [0][1], [0][2]")
print("[1][0], [1][1], [1][2]")
print("[2][0], [2][1], [2][2]")
print("\n")

print("type -1 -1 if you want to show the heuristics and exit")


# print board
def printBoard(board):
    print(board[0][0] + ' |    ' + board[0][1] + '   | ' + board[0][2])
    print('---------------')
    print(board[1][0] + ' |    ' + board[1][1] + '   | ' + board[1][2])
    print('---------------')
    print(board[2][0] + ' |    ' + board[2][1] + '   | ' + board[2][2])
    print("\n")


printBoard(board)


# check if there are free spaces in the board
def spaceIsFree(row, col):
    for i in range(len(board)):
        if board[row][col] == ' ':
            return True
        else:
            return False


# checking if there's a draw
def checkDraw():
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True


# checking for any wins
def checkForWin():
    # checks in each row of matrix "wins" for 3 consecutive X's or O's
    for arr in winnings(board):
        if arr == ['X', 'X', 'X'] or arr == ['O', 'O', 'O']:
            return True
    return False


def insertLetter(letter, row, col):
    # first checks if there's a free cell in the board
    if spaceIsFree(row, col):
        # inserts the specified letter into the board
        board[row][col] = letter
        printBoard(board)
        # if both players don't win and board is full, exit game.
        if checkDraw():
            print("Draw!")
            exit()
        # if one player wins, print winner, calculate heuristics , then exit game
        if checkForWin():
            print(letter, " wins")
            heuristicSearch(board)
            exit()
        return
    else:
        print("position is already filled")
        row, col = list(map(int, input("Enter row and column for a new position: ").split()))
        if row > 3 or col > 3:
            print("out of range try again..")
            row, col = list(map(int, input("Enter row and column for a new position: ").split()))
        insertLetter(letter, row, col)
        return


def heuristicSearch(board):
    # all possible moves to win the game are 8
    possibleXwins = 8
    possibleOwins = 8
    wins = winnings(board)
    # check kol row fl winnings law la2eet O aw X a3mel moves - 1
    for i in range(len(wins)):  # rows
        for j in range(len(board)):  # columns
            if wins[i][j] == 'O':
                possibleXwins -= 1
            if wins[i][j] == 'X':
                possibleOwins -= 1
    # 3amalt l loop de 3shan howa kan by3ml -1 kol amma yshof aktar mn X aw O fl row l wahed fa by3ml - mareten wana
    # 3yzah ye3ml mara wahda
    for i in range(len(wins)):  # rows
        for j in range(len(board)-1):  # columns
            # if there are two X's or O's in the same row add 1
            if wins[i][j] == wins[i][j+1] == 'O':
                possibleXwins += 1
            elif wins[i][j] == wins[i][j+1] == 'X':
                possibleOwins += 1

    E = possibleXwins - possibleOwins
    print("E =", E, "\nX wins = ", possibleXwins, ",O wins =", possibleOwins, "\n")
    return E


def playerMove():
    row, col = list(map(int, input("Enter row and column for a new 'O' position: ").split()))
    if row == -1 or col == -1:
        print("E = ", heuristicSearch(board))
        exit()
    insertLetter(player, row, col)
    return


def botMove():
    row, col = list(map(int, input("Enter row and column for a new 'X' position: ").split()))
    if row == -1 or col == -1:
        print("E = ", heuristicSearch(board))
        exit()
    insertLetter(bot, row, col)
    return


while not checkForWin():
    botMove()
    playerMove()
