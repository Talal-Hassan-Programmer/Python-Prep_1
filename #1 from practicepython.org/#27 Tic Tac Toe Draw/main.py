# Step 1: Create the board
game = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Print the board
for row in game:
    print(row)


players = ["X", "O"]
turn = 0
max_turns = 9

while turn < max_turns:
    move = input(f"Player {players[turn % 2]}, enter your move (row,col): ")
    row, col = map(int, move.split(","))
    row -= 1
    col -= 1
    if game[row][col] == 0:
        game[row][col] = players[turn % 2]
        turn += 1

        print("Current board:")
        for row in game:
            print(row)
    else:
        print("That spot is already taken.")

    

