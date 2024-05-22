# """ 
# N = 축제진행 시간
# M = 파티에 초대된 욱제의 친구
# K = 파티에 초대된 영선이의 친구
# T = 최소 파티 인원
# *g = 오기입 저장
#  """

# N, M, K, T, *g= map(int,input().split())
# #Msch=[[3, 12], [5, 10], [7, 8]] 욱제 친구들의 [입장시간, 퇴장시간]
# Msch=[list(map(int,input().split()))for _ in range(M)]

# """ 
# Wf=파티 참석중인 욱제 친구
# Yfin = 파티 참석중인 영선 친구
# Yfout = 파티 참석 중이 않인 영선 친구
# Wf=욱제가 참석 가능한 시간
# """
# wf = 0
# yfIn = 0
# yfOut = K
# wPTime = 0

# for cTime in range(N):
#     wf= 0
#     for wFSch in Msch:
#         # Msch에서 각 친구들의 입장시간과 퇴장시간을 현재시간과 비교하여 
#         # 현재 참석하고 있는 욱제의 친구들을 구한는 코드
#         if wFSch[0]<=cTime+1 and wFSch[1]>cTime+1:
#             wf+=1

#     # 욱제와 영선이의 친구들을 제외한 파티인원이 T보다 클때
#     if wf>=T :
#         yfIn = 0
#         wPTime += 1
#     #  작을때
#     else:
#         if wf + yfIn >= T:
#             wPTime += 1
#         else :
#             #파티에 필요한 영선이의 친구
#             needF = T-(wf+yfIn)
            
#             # 들어오지 않은 영선이의 친구가 들어온 필요한 친구보다 클 때
#             if yfOut - needF >= 0:
#                 yfIn += needF
#                 yfOut -= needF
#                 wPTime += 1
#     print("\n현재시간:",cTime+1)
#     print("욱제친구:",wf)
#     print("영선친구:",yfIn)
#     print("파티원:",wf+yfIn,"\n")
    
# print(wPTime)

#N, M, K, T= map(int,input().split())
#N, M, K, T, *a= map(int,open(0).read().split())
#Msch=[[3, 12], [5, 10], [7, 8]] 욱제 친구들의 [입장시간, 퇴장시간]
# Msch=[list(map(int,input().split()))for _ in range(M)]
#N, M, K, T= map(int,input().split())
#N, M, K, T, *a = map(int,input().split())
#N, M, K, T, *a= map(int,open(0).read().split())
#Msch=[[3, 12], [5, 10], [7, 8]] 욱제 친구들의 [입장시간, 퇴장시간]
#Msch=[list(a[2*x:2*x+2])for x in range(M)]

# """ 
# N = 축제진행 시간
# M = 파티에 초대된 욱제의 친구
# K = 파티에 초대된 영선이의 친구
# T = 최소 파티 인원
# *g = 오기입 저장
#  """

N, M, K, T= map(int,input().split())
#Msch=[[3, 12], [5, 10], [7, 8]] 욱제 친구들의 [입장시간, 퇴장시간]
Msch=[list(map(int,input().split()))for _ in range(M)]

""" 
Wf=파티 참석중인 욱제 친구
Yfin = 파티 참석중인 영선 친구
Yfout = 파티 참석 중이 않인 영선 친구
Wf = 욱제가 참석 가능한 시간
needPs = 각 시간마다 욱제가 참석하기 위해 필요한 사람
"""
wf = 0
yfOut = K
wPTime = 0
needPs =[]
#필요자원 리스트 구하기
for cTime in range(N):
    wf= 0
    for wFSch in Msch:
        # Msch에서 각 친구들의 입장시간과 퇴장시간을 현재시간과 비교하여 
        # 현재 참석하고 있는 욱제의 친구들을 구한는 코드
        if wFSch[0]<=cTime+1 and wFSch[1]>cTime+1:
            wf+=1
    if wf>=T :
        needPs.append(0)
        wPTime += 1
    #  영선의 친구가 필요할 때
    else:
        needPs.append(T-wf)
print(needPs)

#[가용시간/필요인원, 가용시간, 필요 인원]2차원 리스트 생성
idx = -1
for i in range(N):
    #[가용시간, 필요인원]2차원 리스트를 사용하기 위한 index

    #필요인원이 0이상일 때
    if needPs[i] > 0:
        #2차원 리스트 생성 여부
        if idx == -1:
            idx += 1
            needPsForm = [[0,1,needPs[i]]]
            # 이전 필요인원가 지금 필요인원이 같다 => 추가입장이 없다
            # => 가용시간 증가

        elif needPs[i-1] >= needPs[i] :
            needPsForm[idx][1] += 1

        #     #이전필요인원이 현재 필요인원보다 크다 => 추가입장 필요없다
        #     # => 가용시간 증가
        # elif needPs[i-1] > needPs[i]:
        #     needPsForm[idx][2] += 1

            # 추가적인 입장이 필요 => 우선순위 파악 필요
            # 2차원 리스트 추가 필요 
        elif needPs[i-1] == 0:
            needPsForm[idx][0] = needPsForm[idx][1] / needPsForm[idx][2]
            idx += 1
            needPsForm.append([0,1,needPs[i]])

            # 필요인원이 다르다=> 추가적인 입장이 필요 => 우선순위 파악 필요
            # 2차원 리스트 추가 필요 
        elif needPs[i-1] < needPs[i]:
            needPsForm[idx][0] = needPsForm[idx][1] / needPsForm[idx][2]
            idx += 1
            needPsForm.append([0,1,needPs[i]-needPs[i-1]])

needPsForm[idx][0] = needPsForm[idx][1] / needPsForm[idx][2]

print("[우선순위,가용시간,필요인원]:",needPsForm)
            
needPsForm.sort(reverse = True)
#여기에 needPsForm[i][2]가 내림차순 변환식 추가!!

print("정렬",needPsForm)


for form in needPsForm:
    if yfOut > 0:
        if form[2] <= yfOut :
            yfOut -= form[2]
            wPTime += form[1]
print("욱제의 최대 축재 참여시간",wPTime)

print(wPTime)

# #큰거 다음 작을거가 올때 문제가 있나?
# #needPsForm[i][2]가 내림차순이라 그런가?

# # 입력 받기
# n, m, k, t = map(int, input().split())

# # 파티 참석 여부를 저장할 리스트 초기화
# a = [0] * 301

# # 파티 참석 정보 입력 받기
# for _ in range(m):
#     a_, b_ = map(int, input().split())
#     # 주어진 시간 동안 파티 참석자 수를 세기
#     for i in range(a_, b_):
#         a[i] = min(t, a[i] + 1)

# # 파티 참석 정보를 기반으로 불연속적인 구간을 찾기
# v = []
# temp = a[1]
# _count = 1
# for i in range(2, n + 1):
#     if temp != a[i]:
#         v.append((_count, temp))
#         _count = 0
#         temp = a[i]
#     _count += 1
# v.append((_count, temp))

# # DP 배열 초기화
# dp = [[0] * 301 for _ in range(301)]

# # 최대 시간을 구하는 함수 정의
# def go(here, num, prev):
#     # 종료 조건: 파티의 끝까지 도달했을 때
#     if here == len(v):
#         return 0
#     # 이미 계산한 값이 있다면 반환
#     if dp[here][num] != 0:
#         return dp[here][num]

#     # 현재 파티에서 발생하는 비용 계산
#     cost = max(0, t - v[here][1])
#     real_cost = 0 if prev >= cost else cost

#     # 현재 파티에 참석하는 경우와 참석하지 않는 경우 중 최대 값을 구함
#     ret = dp[here][num]
#     if num - real_cost >= 0:
#         ret = max(go(here + 1, num - real_cost, cost) + v[here][0], go(here + 1, num, 0))
#     else:
#         ret = go(here + 1, num, 0)
    
#     # 계산된 값을 저장하고 반환
#     dp[here][num] = ret
#     return ret

# # 최대 시간 출력
# print(go(0, k, 0))
