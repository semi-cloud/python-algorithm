# 사다리에 가로선을 추가했을때, i번 세로선의 결과가 i번이 나오기 위해 추가해야 하는 가로선 개수의 최솟값

def find_result():             # 각 행이 i번째에 도착하는지 확인
    for i in range(1, N+1):     # 세로 줄 개수
        cur_x = i
        for j in range(1, H+1):    # 가로 줄 개수
            if visited[j][cur_x-1]:     # 왼쪽에 사다리가 있는 경우
                cur_x -= 1              # 왼쪽 칸으로 이동
            elif visited[j][cur_x]:     # 오른쪽에 사다리가 있는 경우
                cur_x += 1              # 오른쪽 칸으로 이동
        if cur_x != i:
            return False
    return True


def dfs(cnt, x, y):
    global answer
    if answer <= cnt:      # 이미 최소값보다 더 많은 사다리를 만든 경우 검사 필요 X
        return

    if find_result():      # i번째가 i번으로 도달하는 경우
        answer = min(answer, cnt)     # 추가 사다리 개수 최소로 갱신
        return

    if cnt == 3:
        return

    # 가로줄을 백트래킹 방식으로 추가
    for i in range(x, H+1):       # 가로줄
        k = y if i == x else 1       # 행이 변경 되기 전에는 순서대로 세로줄 탐색
        for j in range(k, N):         # 세로줄
            if not visited[i][j]:      # 가로줄을 만들 수 있으면
                visited[i][j] = True      # 가로줄 생성
                dfs(cnt + 1, i, j + 2)      # j+2 : 가로줄 연속 불가능
                visited[i][j] = False      # 다시 visited 배열 돌려놓기


N, M, H = map(int, input().split())
visited = [[False] * (N+1) for _ in range(H+1)]       # 사다리가 있는 곳 표시
answer = 4

for _ in range(M):
    a, b = map(int, input().split())
    visited[a][b] = True

dfs(0, 1, 1)
print(answer if answer <= 3 else -1)
