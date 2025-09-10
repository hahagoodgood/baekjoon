'''
#qustion
No.14916
Chunhyang works at the convenience store counter.

A customer asks for change only in 2-won and 5-won coins.
She has an infinite supply of 2-won and 5-won coins.
She must give change using the minimum number of coins.
Write a program that, given change amount n, outputs the minimum number of coins required.

For example, if the change is 15 won, she should give 3 five-won coins.
If the change is 14 won,
she should give 2 five-won coins and 2 two-won coins, totaling 4 coins.
If the change is 13 won, she should give 1 five-won coin and 4 two-won coins, totaling 5 coins.
This minimizes the number of coins used.

---
##input
The first line contains the amount of change, n (1 ≤ n ≤ 100,000).

---
##output
Output the minimum number of coins required for change.
If change cannot be given, output -1.
'''
import sys

def B9655(n:int):
    if n <=4 :
        if n%2 == 0:
            return n//2
        return -1
    else:
        dp = [[0,0]]*(n+1)
        dp[1] = [0, 0]
        dp[2] = [1, 0]
        dp[3] = [0, 0]
        dp[4] = [2, 0]
        dp[5] = [0, 1]
        for i in range(6,n+1):
            if dp[i - 5] != [0, 0]: dp[i] = [dp[i - 5][0], dp[i - 5][1] + 1]
            elif dp[i-2] != [0,0]: dp[i] = [dp[i-2][0]+1, dp[i-2][1]]
            else: return -1
        return sum(dp[n])
if __name__ == '__main__':
    sys.stdout.write(str(B9655(int(sys.stdin.readline()))))