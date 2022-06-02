m, n, k = map(int, input().split())
visit = [[False] * n for _ in range(m)]
result = []
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())    # N, M
    for i in range(y1, y2):
        for j in range(x1, x2):
            visit[i][j] = True

def dfs(a, b):
    st = [(a, b)]
    visit[a][b] = True
    area = 0

    while st:
        x, y = st.pop()
        area += 1

        for dx, dy in d:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if not visit[nx][ny]:
                st.append((nx, ny))
                visit[nx][ny] = True

    result.append(area)

count = 0
for i in range(m):     # 5
    for j in range(n):    # 7
        if not visit[i][j]:
            dfs(i, j)
            count += 1

result.sort()
print(count)
print(" ".join(map(str, result)))






