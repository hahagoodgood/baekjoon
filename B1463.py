'''
Make it 1

---
Problem
Therer are three operations available for an integer X, as follows:

1. If X is divisible by 3, divide it by 3.
2. If X is divisible by 2, divide by 2.
3. Subtract 1.
Given an integer N, you wish to create 1 by appropriately using the three operations above. Output the minimum number of operations required.

---
Input
The first line contains an integer N, which is greater than or equal to 1 and less than or equal to 106 .

---
Output
Output the minimum number of operations required on the first line.
'''
import sys
def b1453(n:int):
    #DP table initialization
    dp = [0]*(n+1)
    for i in range(2, n+1):
        dp[i] = dp[i-1] + 1
        # When divisible only by 3
        if i%3 == 0:
            dp[i] = min(dp[i], dp[i//3]+1)
        # When divisible only by 2
        if i%2 == 0:
            dp[i] = min(dp[i], dp[i//2]+1)
    return dp[n]

if __name__ == '__main__':
    sys.stdout.write(str(b1453(int(sys.stdin.readline()))))