# inputs = [0, 10, 20, 15, 25, 10, 20]
# index = 0
'''
# 재귀함수를 사용하면 중복 계산이 되기에 비효율 적이다.
def step(cnt_con, stairs : list, index):
    #마지막 계단일때
    if len(stairs) - index <= 1:
        return stairs[index]
    # 마지막 바로 앞 계단 일때
    if len(stairs) - index <= 2:
        return stairs[index] + step(cnt_con+1, stairs, index+1)
    # 마지막에서 두번째 일때
    if len(stairs) - index <= 3:
        return stairs[index] + step(cnt_con = 0, stairs = stairs, index = index+2)
    if cnt_con >= 1 :
        return stairs[index] + step(cnt_con = 0, stairs = stairs, index = index+2)

    #함수 현제 위치에서 함수 2개를 호출 시킨다 2중 더 높은 수를 채택한다
    one_step = stairs[index] + step(cnt_con+ 1, stairs, index+1)
    two_step = stairs[index] + step(cnt_con = 0, stairs = stairs, index = index+2)
    return one_step if one_step > two_step else two_step

n = int(input())
inputs = [0]
for i in range(n):
    inputs.append(int(input()))

print(step(-1, inputs, 0))
'''
n = int(input())
inputs = [0]
for i in range(n):
    inputs.append(int(input()))

if n == 1:
    print(inputs[1])
else :
    # 각 계단에서 얻을 수 있는 최고 점수를 기록한다.
    dp = [0]*(n+1)
    dp[1] = inputs[1]
    dp[2] = inputs[1]+inputs[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-2], dp[i-3] + inputs[i-1]) + inputs[i]

    print(dp[n])