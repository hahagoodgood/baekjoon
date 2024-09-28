# a = int(input())
# [print(' '*i,'*'*(a-i)) for i in range(a)]

# 2 ////////////////////////
# for i in range(a):
#     str = ' '*i + '*'*(a-i)
#     print(str)

for i in range(a:=int(input())):print(' '*i+'*'*(a-i))
# print(print(' '*i, '*'*(a-i)))으로 하면 ' ' 와 '*'사이에 공백이 생긴다.