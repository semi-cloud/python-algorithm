# S층에서 G층으로 가기 위해 눌러야 하는 버튼의 수의 최솟값
# 먼저 G층에 도달한 최단 경로를 구해야 하므로 DFS 가 아닌 넓이 우선 탐색 이용
# BFS, DFS 는 무조건 방문 처리 필요에 주의

from collections import deque

def bfs(start, cnt):
    visited = [False for _ in range(f+1)]  # 이미 간 층은 다시 갈 방문할 필요가 없음(중요)
    q = deque([(start, cnt)])
    while q:
        v, c = q.popleft()
        if 0 >= v or v > f or visited[v]:  # 갈 수 있는 층을 벗어났거나 이미 방문했던 층이라면
            continue

        if v == g:  # 스타트 링크에 도달했다면
            return c

        visited[v] = True
        q.append((v + u, c + 1))
        q.append((v - d, c + 1))
    return "use the stairs"       # 엘리베이터를 이용해서 G층에 갈 수 없는 경우

f, s, g, u, d = map(int, input().split())  # 1000000  s : 강호 위치 g : 스타트 링크 위치
print(bfs(s, 0))   # 강호 위치에서 출발
