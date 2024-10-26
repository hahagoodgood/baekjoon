'''
    url : https://www.acmicpc.net/problem/18111
    1. 가장 낮은 좌표의 층을 매울수 있나?
        1.1. Y: 가장 낮은 층의 갯수와 가장 높은 층의 갯수를 찾아 비용 검색
            1.1.2 가장 낮은 층의 비용이 저렴 : 메우기
            1.1.3 가장 높은 층의 비용이 저렴 : 제거
        1.2. N: 가장 높은 층을 제거
'''
# 좌표 찾기
def find_layer(land : list, mod : str):
    # 최소값
    if mod == "lowest" :
        min_layer = land[0][0]

        for i in land:
            for j in i:
                if min_layer > j:
                    min_layer = j
        return min_layer

    elif mod == "highest" :
        max_layer = land[0][0]
        for i in land:
            for j in i:
                if max_layer < j:
                    max_layer = j
        return max_layer

# 해당 층의 블록 수
def count_block(land : list, layer : int) :
    cnt_blc = 0
    for i in land:
        for j in i:
            if layer == j:
                cnt_blc += 1
    return cnt_blc

# B로 메울 수 있나?
def is_able_to_fill(land : list, B : int):
    min_layer = find_layer(land, "lowest")

    cnt_low = count_block(land, min_layer)

    #메울수 있는지 여부
    if cnt_low <= B:
        return True
    else :
        return False

# B로 메우기
def fill_land(land : list, B : int) :
    lowest_layer = find_layer(land, "lowest")
    cnt_layer = count_block(land, lowest_layer)

    B -= cnt_layer

    for i in range(len(land)) :
        for j in range(len(land[i])) :
            if lowest_layer == land[i][j]:
                land[i][j] = lowest_layer + 1

    return B

# 메우기 계산하기
def get_time(land : list, mod : str):
    if mod == "fill" :
        layer = find_layer(land, "lowest")
        cnt_layer = count_block(land, layer)
        return cnt_layer
    elif mod == "remove" :
        layer = find_layer(land, "highest")
        cnt_layer = count_block(land, layer)
        return cnt_layer * 2

# 제거하기
def remove(land : list, B : int):
    #높은층 탐색
    layer = find_layer(land, "highest")

    #최고층 제거
    for i in range(len(land)):
        for j in range(len(land[i])):
            if layer == land[i][j]:
                land[i][j] -= 1
                B += 1
    return B

# 평평한가
def is_filled(land : list) :
    layer = land[0][0]
    for i in land:
        for j in i:
            if layer != j:
                return False
    return True

'''
N: 세로 크기
M: 가로 크기
B: 블록의 갯수
'''
N, M, B = map(int, input().split())
# 각 칸의 땅의 높이 2차원 list
land = []
for i in range(N):
    land.append(list(map(int, input().split())))

# 평탄화 작업 시간
filling_time = 0

# 평평할 때까지 while
while not is_filled(land):
    # 제거 시 시간 비용 계산
    remove_time = get_time(land, "remove")

    # 인벤토리의 블록으로 최저층을 메울 수 있는지
    if is_able_to_fill(land, B):
        # 메울때 시간 비용 계산
        fill_time = get_time(land, "fill")
        # 메울때 드는 비용이 더 작거나 같을 때
        if fill_time <= remove_time :
            filling_time += fill_time
            B = fill_land(land, B)
        #제거 비용이 저렴할 때
        else :
            filling_time += remove_time
            B = remove(land, B)
    # 인벤토리의 블록으로 메울 수 없을 때
    else :
        filling_time += remove_time
        B = remove(land, B)

print(filling_time, land[0][0])
