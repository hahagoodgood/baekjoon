from collections import deque


def portal_game(N, portals):
    # 그래프 초기화
    graph = [[] for _ in range(N)]
    for a, b in portals:
        graph[a].append(b)

    # BFS 초기화
    queue = deque([0])
    distances = [-1] * N
    distances[0] = 0

    # BFS 수행
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    # 결과 반환
    return distances[N - 1]


# 예시 입력
N = 5
portals = [(0, 1), (1, 2), (2, 3), (3, 4)]

# 함수 호출 및 결과 출력
result = portal_game(N, portals)
print(result)  # 출력: 4