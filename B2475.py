'''
#qustion
B2475
KOI Electronics, a computer manufacturer,
assigns a unique six-digit number to each computer it manufactures.
The first five digits of a unique number are given one of the numbers 00000 to 999999 and the sixth digit includes a verification number.
The verification number is the sum of the five numbers in the first five digits of a unique number divided by 10.

For example, if the first five digits of a unique number are 04256,
1 is the remainder of the sum of the numbers squared by 0+16+4+25+36 = 81 divided by 10.

---
##input
In the first line the first five digits of a unique number are given one by one with a blank space between them.

---
##output
Output the verification number on the first line.
'''
import sys


def b2475(N:list):
    result = 0
    for i in N:
        result += i*i
    return result %10

if __name__ == '__main__':
    sys.stdout.write(str(b2475(list(map(int, sys.stdin.readline().split())))))