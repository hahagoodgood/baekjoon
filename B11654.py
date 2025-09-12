'''
#qustion
b11654
Write a program that outputs the value of the ASCII code of the given letter,
given one of the lowercase letters, uppercase letters, and digits 0-9.

---
##input
One of the lowercase letters, uppercase letters, and digits 0-9 is given in the first line.

---
##output
Outputs the ASCII code value of the given letter as input
'''
import sys
sys.stdout.write(str(ord(sys.stdin.readline()[0])))