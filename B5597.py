#1
""" tesk=set([int(input()) for _ in range(5)])
for i in range(30):
    if i+1 not in tesk:
        print(i+1) """

#2
""" tesk=list(map(int,range(1,31)))
for _ in range(28):
    tesk.remove(int(input())) 
print(*tesk) """

#3
""" import sys
tesk = [i for i in range(1,31)]
for _ in range(28):
    tesk.remove(int(sys.stdin.readline()))
print(*tesk) """

#4
""" import sys
tesk = set(list(range(1,31)))
for _ in range(28):
    tesk -= set([int(sys.stdin.readline())])
print(*tesk) """

#5
""" print(*{*map(int,open(0))}^{*range(1,31)}) """

#6
tesk = [1]*31
for _ in range(28): tesk[int(input())]=0
print(*[x for x in range(1,31)if tesk[x]])
#tesk[x]가 0이 아닌 것만 출력