# import sys
# input = sys.stdin.readline

def cover(bordlist):
    #폴리오미노를 배치하는 함수
    return 0

def is_able(bord):
    #bordlist의 요소를 순차적으로 탐색하여 가능여부를 찾는 함수
    for item in bord:
        if item % 2 == 1:
            return -1

def greedy(bord):
    is_able(bord)
    return 0

data = list(input())
bord = []
cntX = 0
cntDote = 0

for item in data:
    if item == '.':
        if cntDote >= 0 :
            
            bord.append(cntX)
            cntX = 0
            cntDote -= 1
        else :
             cntDote -= 1
        continue
    else :
        if cntDote < 0 :
            bord.append(cntDote)
            cntDote = 0
            cntX += 1
        else :
            cntX += 1

if cntX > 0 :
    bord.append(cntX)
    cntX = 0
if cntDote < 0:
    bord.append(cntDote)
    cntDote = 0

print(bord)

answer = greedy(bord)

# answer = greedy(bord)
# print(answer)
