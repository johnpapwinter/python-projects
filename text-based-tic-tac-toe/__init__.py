
def initialize_board():
    return [["-" for row in range(3)] for column in range(3)]


def show_board(input_board):
    for row in input_board:
        print(row)


def validate_victory(input_board):
    for i in range(len(input_board)):
        for j in range(len(input_board)):
            if input_board[0][j] == input_board[1][j] == input_board[2][j] \
                    and input_board[0][j] == input_board[1][j] == input_board[2][j] != "-":
                return True
        if input_board[i][0] == input_board[i][1] == input_board[i][2] \
                and input_board[i][0] == input_board[i][1] == input_board[i][2] != "-":
            return True

    if input_board[0][0] == input_board[1][1] == input_board[2][2] \
            and input_board[0][0] == input_board[1][1] == input_board[2][2] != "-":
        return True
    if input_board[2][0] == input_board[1][1] == input_board[0][2] \
            and input_board[2][0] == input_board[1][1] == input_board[0][2] != "-":
        return True

    return False


def player_mark(player):
    if player:
        return "X"
    else:
        return "O"


def place_mark(x1, y1, mark):
    board[x1][y1] = mark


def check_empty_place(x1, y1):
    if board[x1][y1] == "X" or board[x1][y1] == "O":
        return False
    else:
        return True


player1 = True
turn = 1
board = initialize_board()


while True:
    show_board(board)

    if player1:
        print(f"This is player 1's turn")
    else:
        print(f"This is player 2's turn")

    x = int(input("insert x coordinate: "))
    y = int(input("insert y coordinate: "))

    if check_empty_place(x, y):
        if player1:
            place_mark(x, y, "X")
        else:
            place_mark(x, y, "O")

        if validate_victory(board):
            if player1:
                print(f"Player 1 wins!")
                break
            else:
                print(f"Player 2 wins!")
                break

        player1 = not player1
        turn += 1
    else:
        print("This spot is occupied! Try again!")

    if turn > 9:
        print("The game is a draw!")
        break
