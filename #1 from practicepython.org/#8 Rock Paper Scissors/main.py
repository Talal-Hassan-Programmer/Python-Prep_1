# Rock Paper Scissors | Game

import random


c = ['r', 'p', 's']

cp = []
up = []

while True:
    ch = random.choice(c) # computer choice
    uc = input("Enter your choice (r for rock, p for  paper, s for scissors): | Exit for quiting\n" ).lower() # user choice

    if ((ch == 'r' and uc == 's') or (ch == 'p' and uc == 'r') or (ch == 's' and uc == 'p')):
       cp.append(1)
    elif (uc == 'exit'):
        print("Computer Points: ", sum(cp))
        print("User Points: ", sum(up))
        print("Exiting the game.")
        break
    elif (uc not in c):
        print("Retry with a valid choice.")
    else:
        up.append(1)