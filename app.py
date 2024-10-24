import random
import os
letters = '   a  b  c  d  e  f  g  h'
board = [[] for i in range(8)]
print(letters)
for string in range(1, 9):
    for el in range(8):
        board[string-1].append(random.choice([0, 1]))
    print(string, board[string-1])
os.system('cls')
