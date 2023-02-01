# 매 분마다 물과 고슴도치가 함께 이동 하려면 큐에 둘다 추가 해야함
# 고슴도치 경로만 큐에 추가 하면 매 분마다 물을 따로 확장 시켜야 하는데 매 분을 나눠서 체크 불가능
def bfs(a, b):
    water = [a[:] for a in arr]  # 물 확장용 배열
    q = deque()
    [[q.append((1, i, j)) for j in range(C) if water[i][j] == '*'] for i in range(R)]  # 큐에 물들의 시작 위치를 추가
    q.append((0, a, b))  # 큐에 고슴도치 시작 위치 추가

    while q:
        sort, x, y = q.popleft()

        if sort == 0:   # 1. 고슴도치 위치인 경우
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] != 'X' and water[nx][ny] != '*' and not visit[nx][ny]:
                    if arr[nx][ny] == 'D':  # 다음 갈 곳이 소굴이라면 최단 거리 체크하고 종료
                        return arr[x][y] + 1

                    visit[nx][ny] = True
                    q.append((sort, nx, ny))
                    arr[nx][ny] = arr[x][y] + 1

        if sort == 1:   # 2. 물 위치인 경우
            # 방문 체크를 하지 않으면 안전하게 굴로 이동할 수 없는 경우 함수 종료가 안되어 무한루프 발생
            # 고슴도치 이동 방문 배열과 같이 쓰면 고슴도치가 이동하고 지난 곳에 물을 확장할 수 없는 문제 발생
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] != 'X' and arr[nx][ny] != 'D' and not visit_water[nx][ny]:
                    visit_water[nx][ny] = True
                    q.append((sort, nx, ny))
                    water[nx][ny] = '*'
    else:
        return "KAKTUS"  # 큐를 다 돌았는데도 굴을 만나지 못한 경우

from collections import deque

R, C = map(int, input().split())  # 50(그래프 완전 탐색)
arr = [['' for _ in range(C)] for _ in range(R)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
visit = [[False] * C for _ in range(R)]
visit_water = [[False] * C for _ in range(R)]

cur_x, cur_y = 0, 0
for i in range(R):
    temp = input()
    for j in range(C):
        arr[i][j] = temp[j]
        if temp[j] == 'S':
            cur_x, cur_y = i, j   # 고슴도치 위치

arr[cur_x][cur_y] = 0
print(bfs(cur_x, cur_y))
