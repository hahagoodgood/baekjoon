""" 
N = 축제진행 시간
M = 파티에 초대된 욱제의 친구
K = 파티에 초대된 영선이의 친구
T = 최소 파티 인원
 """
n, m, k, t = map(int, input().split())

# 파티 참석 여부를 저장할 리스트 초기화
a = [0] * (n+1)

# 파티 참석 정보 입력 받기
# a: 욱제 친구의 입장시간
# b: 욱제 친구 퇴장 시간
for _ in range(m):
    start, end = map(int, input().split())
    # 주어진 시간 동안 파티 참석자 수를 세기
    for i in range(start, end):
        #min(t, a[i] + 1)는 t와 a[i]+1 중 더 작은 값을 넣는다.
        a[i] = min(t, a[i] + 1)
print(a)

# 파티 참석 정보를 기반으로 불연속적인 구간을 찾기
# v는 2차원 배열 [한번 입장 후 입장하지 않는 횟수, 사람]
# temp = 입장한 사람의 숫자
# count = 시간 횟수를 측정하기 위한 변수
v = []
temp = a[1]
count = 1
for i in range(2, n + 1):
    if temp != a[i]:
        v.append((count, temp))
        count = 0
        temp = a[i]
    count += 1
v.append((count, temp))
print("v=",v)
# DP 배열 초기화
# 동적 계획법: 큰 문제를 작은 부분 문제로 나누어 해결하는 방법
# 메모이제이션: 이전에 계산한 값을 저장해두고 동일한 계산이 필요할 때 이를 재활용하여 중복 계산을 피하는 기법
# here: 현재 파티시간의 인덱스를 나타냅니다. 처음 호출 시 here는 0부터 시작하며, 재귀 호출을 통해 다음 파티로 이동하면서 증가합니다.
# num: 남은 영희의 친구의 수를 나타냅니다.
# prev: 이전 파티까지의 비용 중 가장 큰 값을 나타냅니다.
# dp: 동적 계획법에서 중복 계산을 피하기 위해 사용되는 메모이제이션 배열입니다.
dp = [[0] * (k+1) for _ in range(len(v))]


# 최대 시간을 구하는 함수 정의
def go(here, num, prev):
    # 종료 조건: 

    if here == len(v):
        return 0
    
    # 이미 계산한 값이 있다면 반환
    # 중복 계산 회피
    if dp[here][num] != 0:
        return dp[here][num]

    # 현재 파티에서 발생하는 비용 계산
    cost = max(0, t - v[here][1])
    # 이전 비용이 현제 비용과 같거나 크다면 real_cost = 0
    # 그렇지 않으면 real_cost = cost
    real_cost = 0 if prev >= cost else cost

    # 현재 파티에 참석하는 경우와 참석하지 않는 경우 중 최대 값을 구함
    # 최대 값 갱신 
    # ret = dp[here][num]
    # 남아있는 영선의 친구의 수가 요구 비용보다 클때
    # 해당 시점에 비용을 지불 할 때와 지불하지 않았을 때를 계산하여 최대 값을 도출
    if num - real_cost >= 0:
        ret = max(go(here + 1, num - real_cost, cost) + v[here][0], go(here + 1, num, 0))
    else:
        ret = go(here + 1, num, 0)
    
    # 계산된 값을 저장하고 반환
    dp[here][num] = ret
    print("here:", here,"num:",num,"ret:",ret)
    print(dp)
    return ret

# 최대 시간 출력
print(go(0, k, 0))
