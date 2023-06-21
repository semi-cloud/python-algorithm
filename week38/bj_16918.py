def set_bomb(cur_time):  # 1초가 더 지나면 폭탄이 없는 모든 칸에 폭탄 설치
    for i in range(R):
        for j in range(C):
            if arr[i][j][0] == '.':
                arr[i][j] = ['O', cur_time + 3]

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
def explode_bomb(cur_time):  # 1초가 더 지나면 폭탄이 폭발 하면서 상하좌우 연쇄 폭발
    bomb_list = []
    for i in range(R):
        for j in range(C):
            if arr[i][j][0] == '.' or arr[i][j][1] != cur_time: continue

            arr[i][j] = ['.', 0]
            for k in range(4):   # 폭발 시간이 된 폭탄만 검사
                nx, ny = i + dx[k], j + dy[k]
                if nx < 0 or nx >= R or ny < 0 or ny >= C: continue
                bomb_list.append([nx, ny])  # 제거할 인접한 폭탄 리스트 저장(기존에 존재하던 폭탄은 유지 해야 하므로 바로 제거 X)

    for x, y in bomb_list:
        arr[x][y] = ['.', 0]

import sys
input = sys.stdin.readline

R, C, N = map(int, input().split(" "))  # N초
arr = [[list() for _ in range(C)] for _ in range(R)]
time = 0

for i in range(R):
    temp = input()
    for j in range(C):
        if temp[j] == 'O':
            arr[i][j] = [temp[j], time + 3]  # [폭탄 여부(원소), 폭발 예정 시간]
        else:
            arr[i][j] = [temp[j], 0]

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
        print(arr[i][j][0], end="")
    print()