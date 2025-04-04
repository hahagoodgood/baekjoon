from collections import deque
import sys

def portal_game(N, C, portal_info):
    # 각 위치에 존재하는 포탈 정보 저장
    portals = [[] for _ in range(N)]
    visited = [float('inf')] * N



    for T, A, B in portal_info:
        portals[A].append((B, T))  # T == 0이면 레드포탈, T == 1이면 블루포탈

    dq = deque()
    dq.appendleft((0, 0))  # 시작 위치 0에서 시간 0
    visited[0] = 0

    while dq:
        now_x, now_t = dq.popleft()

        # 포탈 이동
        for next_x, portal_type in portals[now_x]:
            next_t = now_t
            if visited[next_x] > next_t:
                visited[next_x] = next_t
                # if portal_type == 0:
                #     dq.appendleft((next_x, next_t))
                # else:
                #     dq.append((next_x, next_t))
                #     if now_x + 1 < N and visited[now_x + 1] > now_t + 1:
                #         visited[now_x + 1] = now_t + 1
                #         dq.append((now_x + 1, now_t + 1))

                dq.appendleft((next_x, next_t))
            if portal_type == 1 and now_x + 1 < N and visited[now_x + 1] > now_t + 1:
                visited[now_x + 1] = now_t + 1
                dq.append((now_x + 1, now_t + 1))

        # 일반 이동 (x+1로 1초 후 이동)
        if len(portals[now_x]) == 0:
            if now_x + 1 < N and visited[now_x + 1] > now_t + 1:
                visited[now_x + 1] = now_t + 1
                dq.append((now_x + 1, now_t + 1))

    if visited[N-1] < float('inf'):
        # print(visited)
        return visited[N-1]

    # print(visited)
    return -1  # 도달할 수 없는 경우

# 입력 예시 처리

input = sys.stdin.readline
N, C = map(int, input().split())
portal_info = [tuple(map(int, input().split())) for _ in range(C)]
print(portal_game(N, C, portal_info))




# from collections import deque
# import sys
#
# def portal_game(N, C, portal_info):
#     # 각 위치에 존재하는 포탈 정보 저장
#     portals = [None] * N
#     visited = [float('inf')] * N
#
#     for T, A, B in portal_info:
#         portals[A] = (B, T)  # T == 0이면 레드포탈, T == 1이면 블루포탈
#
#     dq = deque()
#     dq.appendleft((0, 0))  # 시작 위치 0에서 시간 0
#     visited[0] = 0
#
#     while dq:
#         now_x, now_t = dq.popleft()
#
#         # 포탈 이동
#         if portals[now_x] :
#             next_x, portal_type = portals[now_x]
#
#             if visited[next_x] > now_t:
#                 visited[next_x] = now_t
#                 dq.appendleft((next_x, now_t))
#
#             if portal_type == 1 and now_x + 1 < N and visited[now_x + 1] > now_t + 1:
#                 visited[now_x + 1] = now_t + 1
#                 dq.append((now_x + 1, now_t + 1))
#
#         # 일반 이동 (x+1로 1초 후 이동)
#         else :
#             if now_x + 1 < N and visited[now_x + 1] > now_t + 1:
#                 visited[now_x + 1] = now_t + 1
#                 dq.append((now_x + 1, now_t + 1))
#     print(visited)
#     return visited[N-1] if visited[N-1] < float('inf') else -1
#
#     # print(visited)
#     # return -1  # 도달할 수 없는 경우
#
# # 입력 예시 처리
#
# input = sys.stdin.readline
# N, C = map(int, input().split())
# portal_info = [tuple(map(int, input().split())) for _ in range(C)]
# print(portal_game(N, C, portal_info))

"""
코드 작성 중 논리오류로 실행 안 되는 코드 때문에 애먹었던 코드이다.
    블루 포트 사용시 방문한 지점보다 비용이 많이 들게 되면 이동하지 않는 조건문이 있었는데
    해당 조건문에서 블루포트를 사용하지 않고 다음 지점으로 이동하는 부분까지 포함되어
    탐색하지 않은 직점을 탐색 못하게 되어 논리 오류가 발생하였다.
    이를 해결하기 위해 블루 포트를 사용하고 되었을때 비용이 더 발생하는 것을 판단하는 조건문에서
    밖으로 제외하여 다음 지점으로 이동이 가능하도록 하였고
    이에 문제가 해결되었다.
위의 코드는 문제있던 코드를 수정한 것이고 아래있는 AI가 추천한 코드이다.
"""
'''
in English:
This was a piece of code that caused a lot of trouble due to a logical error
    that prevented it from it from running properly.
    There was a condition that prevented movement 
        when using the Blue Port if the cost was higher 
        than visiting the next point normally.
    However, this condition also mistakenly included the case of moving to the next point without using the Blue Port,
    which caused unexplored points to remain unvisited, leading to a logical error.
    To fix this, I moved the cost check for using the Blue Port outside of the condition,
    so that moving to the next point would still be possible even without using the Blue Port.
    This resolved the issue.
The code above is the corrected version, and the one below is the one recommended by the AI.
'''

