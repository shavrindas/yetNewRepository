import random

tictactoe = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]

def draw_board():
    for i in range(3):
        print()
        print("-----------")
        for j in range(3):

            print(tictactoe[i][j],  end=" | ")
    print()
    print("-----------")


def user_input():
    while True:
        x, y = map(int, input().split())
        if tictactoe[x-1][y-1] == ' ':
            tictactoe[x-1][y-1] = 'o'
            break

def computer_input():
    while True:
        x = random.choice([0, 1, 2])
        y = random.choice([0, 1, 2])
        if tictactoe[x][y] == ' ':
            tictactoe[x][y] = 'x'
            break

def check_win():
    if tictactoe[0][0] == tictactoe[0][1] == tictactoe[0][2] != ' ':
        return(1)
    if tictactoe[1][0] == tictactoe[1][1] == tictactoe[1][2] != ' ':
        return(1)
    if tictactoe[2][0] == tictactoe[2][1] == tictactoe[2][2] != ' ':
        return(1)
    if tictactoe[0][0] == tictactoe[1][0] == tictactoe[2][0] != ' ':
        return(1)
    if tictactoe[0][1] == tictactoe[1][1] == tictactoe[2][1] != ' ':
        return(1)
    if tictactoe[0][2] == tictactoe[1][2] == tictactoe[2][2] != ' ':
        return(1)
    if tictactoe[0][0] == tictactoe[1][1] == tictactoe[2][2] != ' ':
        return(1)
    



def main():
    draw_board()
    while True:
        user_input()
        computer_input()
        draw_board()
        if check_win():
            print("win")
            break

main()