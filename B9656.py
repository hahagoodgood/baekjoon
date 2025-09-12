'''
#qustion
B9656
The stone game is a fun game that two people enjoy.

There are N stones on the table.
Sang-geun and Chang-young take turns to take one or three stones.
The person who takes the last stone loses the game.

Write a program that saves the winner when two people play the game perfectly.
The game starts with Sang-geun first.

---
##input
N is given in the first line (1 ≤ N ≤ 1000)

---
##output
If Sang-geun wins the game, he outputs SK,
and if Chang-young wins the game, he outputs CY.
'''
import sys

def b9545(n:int):
    if n % 2 == 0 :
        return 'SK'
    return 'CY'
if __name__ == '__main__':
    sys.stdout.write(b9545(int(sys.stdin.readline())))