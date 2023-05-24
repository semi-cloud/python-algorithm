# 가스관 - 빵집 연결하는 파이프라인 최대 개수 구하기
# 내가 어느 방향으로 다음 파이프를 연결하느냐에 따라 최대 개수가 결정됌 => DFS + DP 인줄 알았지만 그리디였음
# 최대값이 나오게 하려면 = 파이프라인 설치 순서에 따라 달라짐 -> 파이프라인 경로를 최대한 위쪽으로 올려놔야 밑에서 갈 길이 트임

def dfs(a, b, visited):
    global res
    st = [[a, b]]
    visited[a][b] = True

    while st:
        x, y = st.pop()
        if y == C-1:  # 끝에 다다를 경우 한 파이프라인 경로 완성
            res += 1
            break

        for i in range(3):  # 다음 이동 가능한 세 방향 탐색
            nx, ny = x + dx[i], y + dy[i]
            if 0 > nx or nx >= R or 0 > ny or ny >= C or arr[nx][ny] == 'x': continue

            if not visited[nx][ny]:
                visited[nx][ny] = True
                st.append([nx, ny])

    while st:     # 경로가 이미 완성 되었으므로 남아 있던 경로들 방문 해제
        x, y = st.pop()
        visit[x][y] = False  # 세 방향 탐색할 때 스택에 방문 처리 하고 넣어두었던 것들 방문 제거 필요

R, C = map(int, input().split(" "))  # 10000, 500 => 5000000
arr = [list(input()) for _ in range(R)]
dx, dy = [1, 0, -1], [1, 1, 1]  # 오른쪽 대각선 아래, 오른쪽, 오른쪽 대각선 위 순서(스택으로 탐색 하므로 반대)
visit = [[False for _ in range(C)] for _ in range(R)]
res = 0

for i in range(R):
    dfs(i, 0, visit)
print(res)








