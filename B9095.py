'''
---
#문제 9095번
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

---
##입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.

---
##출력:
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.
'''
import sys
import math
def B9095(n:int):
    cnt = 0
    for three_idx in range(n//3+1):
        for two_idx in range((n-three_idx*3)//2+1):
            cnt += 1
    dp = [0]*cnt
    cnt2 = 0
    # 해당 숫자에서 3의 갯수 구하기
    for three_idx in range(n//3+1):
        for two_idx in range((n-three_idx*3)//2+1):
            cnt2 += 1
            # 3 사이에 2가 있을 자리를 순서없이 고르는 경우의 수 (n3+1)Hn2
            result = math.factorial(three_idx+two_idx)//(math.factorial(two_idx)*math.factorial(three_idx))
            # 3과 2의 배열에서 1이 있을 자리를 순서없이 고르는 경우의수
            # 1이 들어가야할 자리
            sit_one = three_idx+two_idx+1
            # 1의 갯수
            num_one = n-3*three_idx-2*two_idx
            result *= math.factorial(sit_one+num_one-1)//(math.factorial(num_one)*math.factorial(sit_one-1))
            dp[cnt2-1] = result

    return sum(dp)

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for _ in range(n):
        num = int(sys.stdin.readline())
        sys.stdout.write(str(B9095(num))+'\n')