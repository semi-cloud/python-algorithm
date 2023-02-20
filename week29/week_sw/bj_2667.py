def dfs(a, b):
    cnt = 0
    st = [(a, b)]
    while st:
        x, y = st.pop()
        cnt += 1  # 인접한 집이 없고 하나만 있는 경우라면 카운팅이 안되므로 반복문 바깥에서 해주기

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1:  # 아직 방문하지 않았다면
                st.append((nx, ny))
                arr[nx][ny] = 0
    return cnt     # 단지에 속하는 집의 수 반환

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
ans, total_cnt = 0, []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:  # 아직 방문하지 않은 곳만 단지 탐색 수행
            arr[i][j] = 0
            total_cnt.append(dfs(i, j))  # 한 DFS 탐색이 끝났다는 것은 한 단지의 탐색 완료를 의미
            ans += 1   # 단지 개수 증가
print(ans)
[print(a) for a in sorted(total_cnt)]

