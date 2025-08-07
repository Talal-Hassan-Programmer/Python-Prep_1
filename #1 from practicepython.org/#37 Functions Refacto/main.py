
# Draw the game board
def horizontal_line():
    print("+---" * user_c + "+") 

def vertical_line():
    print("|   " * (user_c+1) )

def draw_board():
    for i in range(user_c):
        horizontal_line()
        vertical_line()
    horizontal_line()

# Call the function to draw the board
user_c = int(input("Enter the Size (3x3) is 3   (8x8) is 8   (19x19) is 19: "))


draw_board()

print("Game board drawn successfully!")