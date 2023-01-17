# 최소 필요한 배추 흰지렁이 마리 수 구하기

def dfs(a, b):
    st.append((a, b))

    while st:
        x, y = st.pop()
        arr[x][y] = 0     # 방문 처리 미리 해줘야함

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                # arr[x][y] = 0       여기서 방문 처리 하면 덩어리의 마지막 원소가 주위에 0밖에 없기 때문에 조건을 통과하지 못함
                st.append((nx, ny))


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0 for _ in range(M)] for _ in range(N)]
    st = []
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    result = 0

    for i in range(K):
        a, b = map(int, input().split())
        arr[b][a] = 1

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:   # 배추가 심어져 있는 곳이면 수행 탐색
                dfs(i, j)        # 깊이 탐색 하면서 인접한 곳들(덩어리)은 미리 0 처리 해주기
                result += 1

    print(result)

