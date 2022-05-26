# 비의 양에 따라 달라 지는 물에 잠기지 않는 안전 영역의 최대 개수 구하기

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_height = max(map(max, arr))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(a, b, height):
    st = [(a, b)]
    while st:
        x, y = st.pop()

        for i in range(4):     # 상하좌우 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if not visit[nx][ny] and height < arr[x][y]:    # 방문하지 않았고 잠기지 않는 지역
                visit[nx][ny] = True
                st.append((nx, ny))


count, result = 0, 0
for h in range(max_height):
    visit = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visit[i][j] and h < arr[i][j]:     # 잠기지 않는 지역 기준으로 탐색 수행
                dfs(i, j, h)
                count += 1            # 탐색이 종료되면 카운트 증가

    result = max(result, count)       # 여러 경우 중 최댓값
    count = 0

print(result)
