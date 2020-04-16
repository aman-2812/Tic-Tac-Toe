from IPython.display import clear_output


def display_board(board):
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("-|-|-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-|-|-")
    print(board[1] + "|" + board[2] + "|" + board[3])


def player_config():
    player1_name = input("\nPlayer 1, Enter your name : ")
    marker1 = input("Hi {}!! Choose any one symbol in X or O : ".format(player1_name))
    while marker1 != 'X' and marker1 != 'O':
        marker1 = input("{}, you chose a wrong marker. Choose between X or O : ".format(player1_name))
    player2_name = input("Player 2, Enter your name : ")
    marker2 = 'O'
    if marker1 == 'X':
        marker2 = 'O'
    else:
        marker2 = 'X'
    print("Hi {}, you have been assigned {}".format(player2_name, marker2))
    player_dic = {"player1": player1_name, "marker1": marker1, "player2": player2_name, "marker2": marker2}
    return (player_dic)


def check_result(board):
    if (board[1] == board[2] == board[3]):
        return ("win", board[1])
    elif (board[4] == board[5] == board[6]):
        return ("win", board[4])
    elif (board[7] == board[8] == board[9]):
        return ("win", board[7])
    elif (board[1] == board[5] == board[9]):
        return ("win", board[1])
    elif (board[3] == board[5] == board[7]):
        return ("win", board[3])
    elif (board[1] == board[4] == board[7]):
        return ("win", board[1])
    elif (board[2] == board[5] == board[8]):
        return ("win", board[2])
    elif (board[3] == board[6] == board[9]):
        return ("win", board[3])
    else:
        return ("in_progress", " ")

def reset_game():
    global board
    board = [' '] * 10
    global position
    position = [''] * 10

def play_game(player_data):
    display_board(board)
    for i in range(1, 10):
        if i % 2 != 0:
            player_name = player_data['player1']
            player_marker = player_data['marker1']
        else:
            player_name = player_data['player2']
            player_marker = player_data['marker2']

        marker_position = int(input("{} Enter your position on board. Choose a number from 1 to 9 : ".format(player_name)))
        while (1 > marker_position or marker_position > 9) or marker_position in position:
            if marker_position in position:
                marker_position = int(
                    input("You already entered this no. Please don't cheat. Enter the number again : "))
            else:
                marker_position = int(
                    input("Entered position {} is invalid. Enter Something from 1 to 9 : ".format(marker_position)))
        position[i] = marker_position
        board[int(position[i])] = player_marker
        display_board(board)
        (result, winning_marker) = check_result(board)

        if (result == 'win' and winning_marker != ' '):
            if (winning_marker == player_data['marker1']):
                print("Hurray!!! {} is the winner.".format(player_data['player1']))
                break
            elif (winning_marker == player_data['marker2']):
                print("Hurray!!! {} is the winner.".format(player_data['player2']))
                break

        if i == 9:
            print("Hard Luck!!! It's a Draw.")

if __name__ == '__main__':
    print("Welcome to Tic Tac Toe !!!!!")
    print("\nDirections to play:\n 1) Enter your details\n 2)Choose a no. from 1 to 9 and it will resemble the following cell in the board")
    cell_placeholders= [x for x in "0123456789"]
    display_board(cell_placeholders)
    player_data = player_config()
    play_again=True
    while play_again:
        reset_game()
        play_game(player_data)
        play_again=False
        play_again=input("\n\nType True to play again else press Enter")

