# Check Tic Tac Toe


ans = [[1,2,1],
       [1,2,2],
       [2,1,1]]  # YOU CAN CHANGE TH3E VALUE OF ans TO TEST YOUR CODE 1 IS FOR PLAYER 1 AND 2 IS FOR PLAYER 2


if (ans[0][0] == 1 and ans[0][1] == 1 and ans[0][2] == 1) or \
   (ans[1][0] == 1 and ans[1][1] == 1 and ans[1][2] == 1) or \
   (ans[2][0] == 1 and ans[2][1] == 1 and ans[2][2] == 1) or \
   (ans[0][0] == 1 and ans[1][0] == 1 and ans[2][0] == 1) or \
   (ans[0][1] == 1 and ans[1][1] == 1 and ans[2][1] == 1) or \
   (ans[0][2] == 1 and ans[1][2] == 1 and ans[2][2] == 1) or \
   (ans[0][0] == 1 and ans[1][1] == 1 and ans[2][2] == 1) or \
   (ans[0][2] == 1 and ans[1][1] == 1 and ans[2][0] == 1):
    print("Player 1 wins")
elif (ans[0][0] == 2 and ans[0][1] == 2 and ans[0][2] == 2) or \
    (ans[1][0] == 2 and ans[1][1] == 2 and ans[1][2] == 2) or \
    (ans[2][0] == 2 and ans[2][1] == 2 and ans[2][2] == 2) or \
    (ans[0][0] == 2 and ans[1][0] == 2 and ans[2][0] == 2) or \
    (ans[0][1] == 2 and ans[1][1] == 2 and ans[2][1] == 2) or \
    (ans[0][2] == 2 and ans[1][2] == 2 and ans[2][2] == 2) or \
    (ans[0][0] == 2 and ans[1][1] == 2 and ans[2][2] == 2) or \
    (ans[0][2] == 2 and ans[1][1] == 2 and ans[2][0] == 2):
    print("Player 2 wins")
else:
    print("It's a draw")