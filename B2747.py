# sys: Module for rapid standard input/output
# 표준 입출력을 빠르게 하기 위한 모듈
import sys

# n: 피보나치 수열의 크기 변수
def main(n:int):
    # A DP table to stare the Nth Fibonacci number
    # n번째 피보나치 수를 저장할 dp 테이블
    dp = [0]*(n+1)
    # If n is bigger than 0 Calculate the Fibonacci sequence
    # n이 0보다 클 경우 피보나치 계산 수행
    if n > 0:
        # Definition of Fibonacci: F(1) is 1.
        # 피보나치의 정의: F(1)은 1이다.
        dp[1] = 1

        # Calculating the Fibonacci sequence using a "for" loop
        # 반복문으로 피보나치 수열을 계산
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
    # Output the Fibonacci sequence once calculation is complete.
    # 계산이 완료된 피보나치 수열을 출력
    return sys.stdout.write(str(dp[n]))

#When the Python file is executed dicectly, the code below runs.
# 파이썬 파일이 직접 실행될 때 아래의 코드가 실행된다.
if __name__ == '__main__':
    # Read one line from standard input and convert it to an interger using the int function.
    # Place the input String converted to an integer into the main function.
    # 표준 입력으로 한줄을 읽어 int 함수를 사용하여 정수로 변환한다.
    # 정수로 변환된 입력문을 main 함수에 넣는다.
    main(int(sys.stdin.readline()))