import sys

a, b, c = map(int, sys.stdin.readline().split())
sys.stdout.write(f"{(a+b)%c}\n{((a%c)+(b%c))%c}\n{(a*b)%c}\n{((a%c)*(b%c))%c}")