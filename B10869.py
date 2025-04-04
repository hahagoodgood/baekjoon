import sys

#1
A, B = map(int, sys.stdin.readline().split())
sys.stdout.write(f"{A+B}\n{A-B}\n{A*B}\n{A//B}\n{A%B}")

#2
A, B = map(int, input().split())
print(f"{A+B}\n{A-B}\n{A*B}\n{A//B}\n{A%B}")