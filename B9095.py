'''
---

#question
No.9095
Integer 4 can be expressed as a sum of 1s, 2s, and 3s in seven different ways as follows:

1+1+1+1,
1+1+2,
1+2+1,
2+1+1,
2+2,
1+3, and
3+1.
Write a program that determines the number of ways in which a given integer can be expressed as a sum of 1s, 2s, and 3s.
You may assume that the integer is positive and less than 11.

##input
The input consists of T test cases. The number of test cases (T ) is given in the first line of the input file. Each test case consists of an integer written in a single line.

##output
Print exactly one line for each test case. The line should contain an integer representing the number of ways.
'''
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
    '''
    Given the number of 3s, the number of 2s, and the number of 1s,
    it is equivalent to first finding the number of ways to place the 2s between the 3s,
    and then finding the number of ways to place the 1s between the arrangements of 3s and 2s.
    '''
    '''
    3의 갯수 2의 갯수 1의 갯수가 주어졌을 때
    3 사이의 2을 넣는 경우의 수를 구한 후
    3과 2의 배열 사이의 1을 넣는 경우의 수를 구하는 것과 같다.
    '''
    result = 0
    # Finding the number of threes in number n
    # 숫자n에서 3의 갯수 구하기
    for three_idx in range(n//3+1):
        # Number of twos in number n
        # 숫자n에서 2의 갯수
        for two_idx in range((n-three_idx*3)//2+1):
            cnt = 0
            # The number of ways to place twos between threes, (n3+1) H n2
            # 3 사이의 2을 넣는 경우의 수, (n3+1) H n2
            cnt = math.factorial(three_idx+two_idx)//(math.factorial(two_idx)*math.factorial(three_idx))
            # The number of positions where 1 should be placed
            # 1이 들어가야 할 자리의 개수
            num_one = three_idx+two_idx+1
            # Number of ones in number n
            # 숫자n에서 1의 갯수
            one_idx = n-3*three_idx-2*two_idx
            # The number of ways to insert a 1 between the arrays of 3 and 2
            # 3과 2의 배열 사이의 1을 넣는 경우의 수 num_one H one_idx
            cnt *= math.factorial(num_one+one_idx-1)//(math.factorial(one_idx)*math.factorial(num_one-1))
            result += cnt

    return result

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for _ in range(n):
        num = int(sys.stdin.readline())
        sys.stdout.write(str(B9095(num))+'\n')