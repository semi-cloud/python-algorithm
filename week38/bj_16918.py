def set_bomb(cur_time):  # 1초가 더 지나면 폭탄이 없는 모든 칸에 폭탄 설치
    for i in range(R):
        for j in range(C):
            if arr[i][j] == -1:
                arr[i][j] = cur_time + 3

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
def explode_bomb(cur_time):  # 1초가 더 지나면 폭탄이 폭발 하면서 상하좌우 연쇄 폭발
    bomb_list = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] == -1 or arr[i][j] > cur_time: continue
            bomb_list.append((i, j))

    for x, y in bomb_list:
        arr[x][y] = -1
        for k in range(4):  # 폭발 시간이 된 폭탄만 검사
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or nx >= R or ny < 0 or ny >= C: continue
            arr[nx][ny] = -1       # 제거할 인접한 폭탄 리스트 저장(기존에 존재하던 폭탄은 유지 해야 하므로 바로 제거 X)

import sys
input = sys.stdin.readline

R, C, N = map(int, input().split(" "))  # N초
temp = [input() for _ in range(R)]
time = 0
arr = [[time + 3 if temp[i][j] == 'O' else -1 for j in range(C)] for i in range(R)]

time += 1   # 1초 동안 아무것도 안함
while True:     # 폭탄은 설치 후 3초 뒤에 폭발
    time += 1
    if time % 2 == 0:  # 짝수 시간에는 무조건 다 0으로 채워짐
        set_bomb(time)
    else:            # 홀수 시간에는 폭탄 터트리기(규칙 존재)
        explode_bomb(time)
    if time == N: break

for i in range(R):
    for j in range(C):
        if arr[i][j] == -1:
            print(".", end="")
        else:
            print("O", end="")
    print()