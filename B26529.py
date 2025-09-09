'''
#qestion
No.26529
You’re going to raise farm animals and you decided to start with bunnies, the easiest of animals.
To your surprise they are breeding like rabbits, so much so that you’re unable to count them accurately.
However, you know that rabbits’ breeding patterns always follow the Fibonacci sequence. The Fibonacci sequence is defined as follows:

F(0) = 1, F(1) = 1, F(N) = F(N-1)+F(N-2)

Given the number of months the rabbits have been breeding, use the Fibonacci sequence to determine the number of rabbits you should have.

---
##input
The first line will contain a single integer n that indicates the number of data sets that follow.
Each data set will start with a single integer x denoting the number of months that have passed since you bought your initial pair of rabbits.
0≤x≤45

---
##output
For each test case, output the expected number of rabbits after x months.

---
#문제:
1003번
당신은 농장 동물을 키우기로 했고, 가장 쉬운 동물인 토끼부터 시작하기로 결정했습니다.
놀랍게도 토끼들은 토끼처럼 번식하고 있어서, 정확히 세기도 어려울 정도입니다.
하지만 토끼의 번식 패턴은 항상 피보나치 수열을 따른다는 것을 알고 있습니다. 피보나치 수열은 다음과 같이 정의됩니다:

F(0) = 1, F(1) = 1, F(N) = F(N-1)+F(N-2)

토끼들이 번식한 개월 수를 고려하여, 피보나치 수열을 사용하여 현재 보유해야 할 토끼의 수를 구하시오.

---
##입력
첫 번째 줄에는 뒤따르는 데이터 세트의 개수를 나타내는 정수 n이 하나 들어 있습니다.
각 데이터 세트는 처음 토끼 한 쌍을 구입한 이후로 지난 달 수를 나타내는 정수 x 하나로 시작합니다.
0≤x≤45

---
##출력
각 테스트 케이스에 대해, x개월 후 예상되는 토끼의 수를 출력하십시오.
'''
import sys


# def B26529(x:int):
#     if x<=1:
#         return 1
#     else:
#         return B26529(x-1) + B26529(x-2)

def B26529(x:int):
    if x<=1:
        return 1
    else:
        dp = [0]*(x+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, x+1): dp[i] = dp[i-1]+dp[i-2]
        return dp[x]



if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for _ in range(n):
        sys.stdout.write(str(B26529(int(sys.stdin.readline())))+'\n')
