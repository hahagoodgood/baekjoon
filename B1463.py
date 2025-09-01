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
def B1453(n:int):
    # n이 1일때
    if n == 1:
        return 0
    # n이 3 이거나 2 일때
    if n == 2 or n == 3:
        return 1
    #dp 테이블 초기화
    dp = [107]*(n+1)
    dp[0] = -1
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    for i in range(4, n+1):
        #2와 3으로 모두 나눠질 때
        if not((i%2) or (i%3)):
            dp[i] = min(dp[i-1], dp[i//2], dp[i//3]) + 1
        # 3으로만 나눠질 때
        elif not(i%3):
            dp[i] = min(dp[i-1], dp[i//3]) + 1
        # 2로만 나누질 때
        elif not(i%2):
            dp[i] = min(dp[i-1], dp[i//2]) + 1
        else :
            dp[i] = dp[i-1]+1
    return dp[n]

if __name__ == '__main__':
    sys.stdout.write(str(B1453(int(sys.stdin.readline()))))