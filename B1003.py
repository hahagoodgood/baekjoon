"""
#question
No.1003
Calling fibonacci(3) results in the following sequence of events:

fibonacci(3) calls fibonacci(2) and fibonacci(1) (the first call).
fibonacci(2) calls fibonacci(1) (the second call) and fibonacci(0).
The second call to fibonacci(1) outputs 1 and returns 1.
fibonacci(0) outputs 0 and returns 0.
fibonacci(2) obtains the results of fibonacci(1) and fibonacci(0), and returns 1.
The first call to fibonacci(1) outputs 1 and returns 1.
fibonacci(3) obtains the results of fibonacci(2) and fibonacci(1), and returns 2.
1 is printed twice, and 0 is printed once. Given a number N, write a programme to determine how many times 0 and 1 are printed when fibonacci(N) is called.

---
##input:`
The first line contains the number of test cases, T.

Each test case consists of a single line containing N. N is a natural number less than or equal to 40, or 0.

---
output:
For each test case, output the number of times 0 is printed and the number of times 1 is printed, separated by a space.

#문제:
1003번
fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.

fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
fibonacci(0)은 0을 출력하고, 0을 리턴한다.
fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.
1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

---
##입력:
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.

---
##출력:
각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.
"""

import sys
def B1003(n:int):
    # When n==0, the number of calls to 0 is 1, and the number of calls to 1 is 0
    # n==0일때 0의 호출 개수 1, 1의 호출개수 0
    if n == 0:
        return f"1 0"
    else:
        # Initialise the DP table with [0, 0] as n+1 elements.
        # dp 테이블을 [0, 0]이 n+1개 요소로 초기화
        dp = [[0,0]]*(n+1)
        # When n==0, the number of calls to 0 is 1, and the number of calls to 1 is 0
        #n==0일때 0의 호출 개수 1, 1의 호출개수 0
        dp[0] = [1,0]
        # When n==1, the number of calls to 0 is 0, and the number of calls to 1 is 1
        #n==1일때 0의 호출 개수 0, 1의 호출 개수 1
        dp[1] = [0,1]
        # The number of 0s and 1s called in the Fibonacci sequence at n -> The sum of the number of 0s and 1s called at n-1 and n-2
        # 피보나치 수열 n의 0과 1의 호출 개수 -> n-1 과 n-2의 0과 1의 호출 개수의 합
        for i in range(2,n+1):
            dp[i] = [dp[i-1][0]+dp[i-2][0],dp[i-1][1]+dp[i-2][1]]
        return f"{dp[n][0]} {dp[n][1]}"
if __name__ == "__main__":
    testcase = int(sys.stdin.readline())
    for _ in range(testcase):
        sys.stdout.write(B1003(int(sys.stdin.readline()))+"\n")
