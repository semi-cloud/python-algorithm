from collections import deque
import sys
input = sys.stdin.readline

def bfs(a, b):
    global sheep, wolf
    s, w = 0, 0
    q = deque([(a, b)])
    visit[a][b] = True

    while q:
        x, y = q.popleft()

        if arr[x][y] == 'o': s += 1   # arr[nx][ny]가 아니고 여기서 검사 필요
        elif arr[x][y] == 'v': w += 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C or arr[nx][ny] == '#' or visit[nx][ny]:
                continue
            visit[nx][ny] = True
            q.append((nx, ny))

    if s <= w: sheep -= s  # 늑대 개수 보다 양 개수가 적으면 해당 영 역안에 있는 양 모두 먹음
    else: wolf -= w      # 아니라면 늑대를 쫓아냄

R, C = map(int, input().split(" "))
sheep, wolf = 0, 0
arr = ['' for _ in range(R)]
for i in range(R):
    temp = input()
    for t in temp:
        if t == 'v': wolf += 1
        elif t == 'o': sheep += 1
    arr[i] = temp

dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
visit = [[False for _ in range(C)] for _ in range(R)]

for i in range(R):
    for j in range(C):
        if not visit[i][j] and arr[i][j] != '#':
            bfs(i, j)

print(sheep, wolf)
