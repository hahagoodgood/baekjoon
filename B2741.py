'''
#qustion
B2741
Given a natural number N, write a program that outputs one per line from 1 to N.

---
##input
The first line is given a natural number N that is less than or equal to 100,000.

---
##output
The first line to the Nth line are printed in order.
'''
import sys


def b2475(N:int):
    for i in range(1,N+1):
        sys.stdout.write(str(i) + '\n')

if __name__ == '__main__':
    b2475(int(sys.stdin.readline()))