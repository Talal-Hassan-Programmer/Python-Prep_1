# Step 1: Create the board
ans = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Print the board
for row in ans:
    print(row)


players = ["x", "o"]
turn = 0
max_turns = 9

while True:
    move = input(f"Player {players[turn % 2]}, enter your move (row,col): ")
    row, col = map(int, move.split(","))
    row -= 1
    col -= 1
    if ans[row][col] == 0:
        ans[row][col] = players[turn % 2]
        turn += 1

        print("Current board:")
        for row in ans:
            print(row)
    else:
        print("That spot is already taken.")
    
    # Check for a winner
    if (ans[0][0] == "x" and ans[0][1] == "x" and ans[0][2] == "x") or \
        (ans[1][0] == "x" and ans[1][1] == "x" and ans[1][2] == "x") or \
        (ans[2][0] == "x" and ans[2][1] == "x" and ans[2][2] == "x") or \
        (ans[0][0] == "x" and ans[1][0] == "x" and ans[2][0] == "x") or \
        (ans[0][1] == "x" and ans[1][1] == "x" and ans[2][1] == "x") or \
        (ans[0][2] == "x" and ans[1][2] == "x" and ans[2][2] == "x") or \
        (ans[0][0] == "x" and ans[1][1] == "x" and ans[2][2] == "x") or \
        (ans[0][2] == "x" and ans[1][1] == "x" and ans[2][0] == "x"):
        print("Player 1 wins")
        break

    
    elif (ans[0][0] == "o" and ans[0][1] == "o" and ans[0][2] == "o") or \
        (ans[1][0] == "o" and ans[1][1] == "o" and ans[1][2] == "o") or \
        (ans[2][0] == "o" and ans[2][1] == "o" and ans[2][2] == "o") or \
        (ans[0][0] == "o" and ans[1][0] == "o" and ans[2][0] == "o") or \
        (ans[0][1] == "o" and ans[1][1] == "o" and ans[2][1] == "o") or \
        (ans[0][2] == "o" and ans[1][2] == "o" and ans[2][2] == "o") or \
        (ans[0][0] == "o" and ans[1][1] == "o" and ans[2][2] == "o") or \
        (ans[0][2] == "o" and ans[1][1] == "o" and ans[2][0] == "o"):
        print("Player 2 wins")
        break


    elif turn == max_turns:
        print("It's a draw")
        break
    

