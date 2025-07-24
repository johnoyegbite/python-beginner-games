panel = 3
def create_board():
    board = []
    for i in range(panel):
        row = []
        for j in range(panel):
            row.append("-") 
        board.append(row)
    return board


def show_board(board):
    print('-' * 9)
    for i in range(panel):
        for j in range(panel):
            print(board[i][j], end = ' ')
            if j < panel - 1:
                print('|', end ='')
        print()
        if i < panel - 1:
            print('-' * 9)

def player_symbol():
    player_1 = 'X' 
    player_2 = 'O'
    select_player = input("Enter the character you want to display (X/O): ")
    
    if select_player.upper() == 'X':
        Computer = player_2
    else:
        Computer = player_1 
    
    
def player_name():
    player_name  = input("Enter name of choice: ")

def declare_winner(board, player_name, player_symbol):
    possible_win = [[board[0][0] == board[0][1] == board[0][2]],
                    [board[1][0] == board[1][1] == board[1][2]],
                    [board[2][0] == board[2][1] == board[2][2]],
                    [board[0][0] == board[1][1] == board[2][2]],
                    [board[0][2] == board[1][1] == board[2][0]],
                    [board[0][0] == board[1][0] == board[2][0]],
                    [board[0][1] == board[1][1] == board[2][1]],
                    [board[0][2] == board[1][2] == board[2][2]]]
  
    for win in possible_win:
        if win == "X" * 3:
            print("Computer is the winner")
        elif win == "O" * 3:
            print(f"{player_name} is the winner")
    return "There is no winner yet"
board = create_board()
symbol = player_symbol()
show_board(board)
player_name()
player_symbol()
declare_winner(board, player_name, player_symbol)

def declare_winner(board):
    turns = 9
    player_1 = 'X' 
    player_2 = 'O'
    select_player = input("Enter the character you want to display (X/O): ")
    player_name  = input("Enter name of choice: ")
    if select_player.upper() == 'X':
        Computer = player_2
    else:
        Computer = player_1 
   
    for turn in range(3, turns):
        if Computer == player_2:
            if board[0][0] == board[0][1] == board[0][2]:
                return "Computer is the winner"
            elif  board[1][0] == board[1][1] == board[1][2]:
                return "Computer is the winner"
            elif board[2][0] == board[2][1] == board[2][2]:
                return "Computer is the winner"
            elif board[0][0] == board[1][1] == board[2][2]:
                return "Computer is the winner"
            elif board[0][2] == board[1][1] == board[2][0]:
                return "Computer is the winner"
            elif board[0][0] == board[1][0] == board[2][0]:
                return "Computer is the winner"
            elif board[0][1] == board[1][1] == board[2][1]:
                return "Computer is the winner"
            elif board[0][2] == board[1][2] == board[2][2]:
                return "Computer is the winner"
        else:
            if board[0][0] == board[0][1] == board[0][2]:
                return f"Player {player_name} is the winner"
            elif  board[1][0] == board[1][1] == board[1][2]:
                return f"Player {player_name} is the winner"
            elif board[2][0] == board[2][1] == board[2][2]:
                return f"Player {player_name} is the winner"
            elif board[0][0] == board[1][1] == board[2][2]:
                return f"Player {player_name} is the winner"
            elif board[0][2] == board[1][1] == board[2][0]:
                return f"Player {player_name} is the winner"
            elif board[0][0] == board[1][0] == board[2][0]:
                return f"Player {player_name} is the winner"
            elif board[0][1] == board[1][1] == board[2][1]:
                return f"Player {player_name} is the winner"
            elif board[0][2] == board[1][2] == board[2][2]:
                return f"Player {player_name} is the winner"
    return "There is no winner"

board = create_board()
show_board(board)
declare_winner(board)


