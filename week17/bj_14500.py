# 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램
import sys
input = sys.stdin.readline

def dfs(x, y, depth, sum):  # 1
    global result

    if depth == 4:
        result = max(result, sum)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if depth == 2:
                visited[nx][ny] = True
                dfs(x, y, depth + 1, sum + arr[nx][ny])       # 'ㅏ', 'ㅓ', 'ㅗ', 'ㅜ' 모양의 블럭 생성
                visited[nx][ny] = False
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, sum + arr[nx][ny])
            visited[nx][ny] = False


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
result = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, arr[i][j])
        visited[i][j] = False
print(result)



