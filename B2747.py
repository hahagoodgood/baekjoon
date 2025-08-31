import sys

def main(n:int):
    dp = [0]*(n+1)
    if n > 0:
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
    return sys.stdout.write(str(dp[n]))



if __name__ == '__main__':
    main(int(sys.stdin.readline()))