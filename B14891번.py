
#https://www.acmicpc.net/problem/14891

a = [] #톱니 리스트
scds = [] # 회전 리스트

##############################################################

# 회전 방향에 따라 회전하는 함수
def turn(x : list, drt):
    temp = 0
    if drt < 0 :
        temp = x[0]
        for i in range(len(x)-1):
            x[i] = x[i+1]
        x[7] = temp
    else :
        temp = x[7]
        for i in range(len(x)-1):
            x[7-i] = x[7-i-1]
        x[0] = temp

################################################################3

# 입력 리스트
# 톱니 입력
for _ in range(4):
    x = list(input())
    a.append(x)

#회전 횟수 입력
n = int(input())

#스케줄 입력
for i in range(n):
   scd = list(map(int, input().split()))
   scds.append(scd)


import copy
# 스케줄 순차 실행
for scd in scds:
    ta = copy.deepcopy(a)
    turn(a[scd[0]-1], scd[1])

    #스케줄에 있는 톱니와 반대되는 방양으로 회전
    drc = scd[1] * (-1)

    #왼쪽 톱니 회전
    for i in range(scd[0]-2,-1,-1):
        #현재 톱니의 2번째 이빨이 이전 이전 톱니의 6번째 이빨과 극이 다른지 비교
        if ta[i][2] != ta[i+1][6]:
            #회전
            turn(a[i], drc)
            #방향 변경
            drc *= -1
        else:
            break

    #44
    drc = scd[1] * (-1)
    # 오른쪽 톱니 회전
    for i in range(scd[0],4):
        # 현재 톱니의 2번째 이빨이 이전 이전 톱니의 6번째 이빨과 극이 다른지 비교
        if ta[i-1][2] != ta[i][6]:
            turn(a[i], drc)
            drc *= -1
        else:
            break
#점수
score = 0

# 점수 채점
for idx, whl in enumerate(a):
    if whl[0] == '1':
        score += 2**idx

print(score)
