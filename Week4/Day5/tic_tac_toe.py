def display_board(board):
    clear_output()
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])
    
test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)
X|O|X
O|X|O
X|O|X

def player_input():
    marker = ''
    while marker != 'x' and marker !='o':
        marker = input('playeruno, choose x or o: ')
    playeruno= marker
    if playeruno == 'x':
        playeruno = 'o'
    else:
        playerdos = 'x'
    return (playauno, playados)

player_input()
playeruno, choose x or o: 
playeruno, choose x or o: 


['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
def place_marker(board, marker, position):
    board[position] = marker
test_board