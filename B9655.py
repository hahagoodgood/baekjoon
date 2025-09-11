'''
#qustion
Stone Game is a fun game for two players.

There are N stones on the table. Sang-geun and Chang-young take turns removing stones,
taking either 1 or 3 stones at a time. The player who takes the last stone wins the game.

Write a program to determine the winner when both players play perfectly.
Sang-geun starts the game.

---
##input
The first line contains an integer N. (1 ≤ N ≤ 1000)

---
##output
If Sanggeun wins the game, it outputs SK; if Changyoung wins the game, it outputs CY.

---
문제
돌 게임은 두 명이서 즐기는 재밌는 게임이다.

탁자 위에 돌 N개가 있다. 상근이와 창영이는 턴을 번갈아가면서 돌을 가져가며,
돌은 1개 또는 3개 가져갈 수 있다. 마지막 돌을 가져가는 사람이 게임을 이기게 된다.

두 사람이 완벽하게 게임을 했을 때, 이기는 사람을 구하는 프로그램을 작성하시오.
게임은 상근이가 먼저 시작한다.

---
입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 1000)

---
출력
상근이가 게임을 이기면 SK를, 창영이가 게임을 이기면 CY을 출력한다.
'''
import sys


def b9655(N:int):
    if N%2==0:return 'CY'
    return 'SK'

if __name__ == '__main__':
    sys.stdout.write(B9655(int(sys.stdin.readline())))