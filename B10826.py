'''
#qustion
b10826
The Fibonacci numbers begin with 0 and 1.
The 0th Fibonacci number is 0, and the 1st Fibonacci number is 1.
Then from the 2nd it is the sum of the previous two Fibonacci numbers.

Using this equation, Fn = Fn-1 + Fn-2 (n ≥ 2).

If you write the Fibonacci number until n=17, it is as follows.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

Write a program to find the nth Fibonacci number, given n.

---
##input
The first line is given by n. N is a natural number less than or equal to 10,000, or 0.

---
##output
Output the nth Fibonacci number on the first line.
'''
import sys


def b10826(n:int):
    dp = [0]*(2 if n < 2 else n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):dp[i] = dp[i-1]+dp[i-2]
    return dp[n]

if __name__ == '__main__':
    sys.stdout.write(str(b10826(int(sys.stdin.readline()))))
