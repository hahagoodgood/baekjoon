# square = []
# for i in range(10):
#     row = list(map(int,input().split()))
#     square.append(row)

# # print(square)

# #5X5,4X4, 3X3, 2X2, 1X1을 차례대로 검사

# papers = []
# #붙일 색종이의 배열[시작X, 시작 Y, 끝X, 끝 Y] 

# #개수 초과 플래그
# cntOver = 0

# for idxOfChek in range(5,0,-1):
#     paperCnt = 0
#     for idxOfRow in range(10):
#         for idxOfClm in range(10):
#             duple = 0
#             #이미 종이를 붙인 곳임을 나타내는 플래그
#             if square[idxOfRow][idxOfClm] == 1:
#                 #1을 만났을때 검사
#                 #해당 영역이 papers의 영역 안에 있는지 검사
#                 # for sRow, sClm, eRow, eClm in papers:
#                 #     if sRow <= idxOfRow and idxOfRow <= eRow:
#                 #         if sClm <= idxOfClm and idxOfClm <= eClm:
#                 #             duple = -1
#                 #             break
#                 if duple == 0:
#                     #중복이 아닐때
#                     paper = 0
#                     for i in range(idxOfChek):
#                         if idxOfRow + i < 10 and idxOfClm + idxOfChek - 1 < 10:
#                             if square[idxOfRow+i][idxOfClm:idxOfClm + idxOfChek] == [1] * idxOfChek:
#                                 paper += 1
#                     if paper == idxOfChek:
#                         for i in range(idxOfChek):
#                             if idxOfRow+i < 10 and idxOfClm + idxOfChek - 1 < 10:
#                                 if square[idxOfRow+i][idxOfClm:idxOfClm + idxOfChek] == [1] * idxOfChek:
#                                     square[idxOfRow+i][idxOfClm:idxOfClm + idxOfChek] = [0] * idxOfChek
#                         papers.append([idxOfRow, idxOfClm, idxOfRow + idxOfChek - 1, idxOfClm + idxOfChek - 1])
#                         paperCnt += 1
#                         if paperCnt > 5:
#                             cntOver = -1
#                         # print("papers.append", idxOfRow, idxOfClm, idxOfRow + idxOfChek - 1, idxOfClm + idxOfChek - 1)
#                         # print(square)
#                 else :
#                     continue

# # print("papers:", papers)
# if cntOver == 0:
#     print(len(papers))
# else :
#     print(-1)


def is_valid(x, y, size, paper):
    # 색종이가 종이를 벗어나거나 이미 사용한 색종이라면 유효하지 않음
    if x + size > 10 or y + size > 10 or used_paper[size] == 5:
        return False
    else:
        # 색종이가 덮인 부분에 다른 색종이가 이미 있으면 유효하지 않음
        for i in range(x, x + size):
            for j in range(y, y + size):
                if paper[i][j] == 0 or visited[i][j]:
                    #paper가 0인 경우는 색종이의 범위를 벗어남
                    #visited가 1인 경우는 해당 영역이 이미 붙혀져 있다.
                    return False
    return True

def cover(x, y, size, value):
    # 색종이로ㄴ 덮은 부분을 표시하고 색종이 사용 개수를 증가시킴
    for i in range(x, x + size):
        for j in range(y, y + size):
            visited[i][j] = value

def find_next():
    # 다음 덮어야 할 위치 찾기
    for i in range(10):
        for j in range(10):
            if paper[i][j] == 1 and not visited[i][j]:
                return (i, j)
    return (-1, -1)

def dfs(cnt):
    global answer

    # 현재까지 사용한 색종이의 개수가 answer보다 크다면 중단
    if cnt >= answer:
        return

    x, y = find_next()

    # 모든 부분이 덮혔다면 answer 갱신
    if x == -1 and y == -1:
        answer = min(answer, cnt)
        return
    else :
        # 색종이를 붙일 수 있는 가장 큰 크기부터 시작
        for size in range(5, 0, -1):
            if is_valid(x, y, size, paper):
                cover(x, y, size, 1)
                used_paper[size] += 1
                dfs(cnt + 1)
                used_paper[size] -= 1
                cover(x, y, size, 0)
# 입력
paper = [list(map(int, input().split())) for _ in range(10)]
visited = [[0] * 10 for _ in range(10)] #색종이를 붙였다는 것을 알려주기 위한 2차원 배열
used_paper = [0] * 6  # 각 크기의 색종이 사용 개수
answer = float('inf') #무한대를 의미한다. 

# 탐색 시작
dfs(0)

# 정답 출력
if answer == float('inf'):
    print(-1)
else:
    print(answer)




