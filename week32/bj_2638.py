# 입력으로 주어진 치즈가 모두 녹아 없어 지는데 걸리는 정확한 시간 구하기

def external_dfs(a, b):
    visit = [[False for _ in range(M)] for _ in range(N)]
    st = [(a, b)]
    visit[a][b] = True
    if arr[a][b] == 0: arr[a][b] = 2

    while st:
        x, y = st.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue

            if arr[nx][ny] == 0 and not visit[nx][ny]:
                st.append((nx, ny))
                arr[nx][ny] = 2   # 외부 공기 구별
                visit[nx][ny] = True


def cheese_dfs(a, b,  melt, visited):
    st = [(a, b)]
    visit[a][b] = True

    while st:
        x, y = st.pop()
        cnt = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue

            if arr[x][y] == 1 and arr[nx][ny] == 2:  # 공기는 방문 체크 X
                cnt += 1
                continue

            if arr[nx][ny] == 1 and not visited[nx][ny]:  # 다음 치즈 탐색
                st.append((nx, ny))
                visited[nx][ny] = True

        if cnt >= 2:
            melt.append((x, y))  # 2변 이상 공기와 접촉 한다면 녹아야 할 치즈로 체크

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
total, melt_cnt = 0, 0  # 녹은 치즈의 개수, 개수가 처음이랑 같다면 종료
time = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1: total += 1
external_dfs(0, 0)  # 외부와 내부 공간을 구분

# 2. 녹을 치즈 DFS 상하좌우 탐색
while melt_cnt != total:
    later_melt = []
    visit = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):  # 탐색과 제거를 같이 하면 약 1이 연결되어 있지 않고 떨어져 있으면 왼쪽 끝나고 2로 바뀌고 이게 같은 턴의 오른쪽 치즈까지 영향이 감
        for j in range(M):
            if arr[i][j] == 1 and not visit[i][j]:
                cheese_dfs(i, j, later_melt, visit)  # 처음 처리 능한 치즈 확인

    for x, y in later_melt:   # 녹인 치즈는 공기로 바꿔 주고 방문 표시
        melt_cnt += 1
        arr[x][y] = 2
        st = [(x, y)]

        while st:
            a, b = st.pop()
            for i in range(4):
                nx, ny = a + dx[i], b + dy[i]
                if arr[nx][ny] == 0:  # 구멍이 뚫린 경우 외부 공기 유입
                    arr[nx][ny] = 2
                    st.append((nx, ny))
    time += 1
print(time)


