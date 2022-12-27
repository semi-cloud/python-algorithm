def update():
    for i in range(R):
        for j in range(C):
            if arr[i][j][0] == 0 or arr[i][j][0] == -1:  # 미세먼지일 경우에만 확산
                continue
            arr[i][j][1] = arr[i][j][0] // 5   # 확산 1회가 끝난 후, 새로 확산 시작 전에 업데이트


def dust_spread():
    for x in range(R):
        for y in range(C):
            if arr[x][y][0] == 0 or arr[x][y][0] == -1:  # 미세먼지일 경우에만 확산
                continue

            cnt = 0
            for d in range(4):   # 네 방향으로 확산
                nx = x + dx[d]
                ny = y + dy[d]

                if 0 > nx or R <= nx or 0 > ny or C <= ny or arr[nx][ny][0] == -1:  # 공기 청정기가 있거나 칸이 없는 경우는 확산 불가능
                    continue

                arr[nx][ny][0] += arr[x][y][1]    # 인접한 곳에 확산된 값을 더해주기
                cnt += 1         # 총 몇 개의 방향으로 확산되었는지 체크
            arr[x][y][0] -= cnt * arr[x][y][1]   # 확산된 만큼 원래 미세먼지 농도에서 빼주기

def air_clean():
    temp = [a[:] for a in arr]

    x1, y1 = air[0][0], air[0][1] + 1    # 공기 청정기 다음 위치 부터 시작
    x2, y2 = air[1][0], air[1][1] + 1
    arr[x1][y1], arr[x2][y2] = [0, 0], [0, 0]
    up_dir, down_dir = 1, 1      # 시작 방향은 오른쪽

    while True:
        nx = x1 + dx[up_dir]
        ny = y1 + dy[up_dir]

        if nx == air[0][0] and ny == air[0][1]:  # 다음 구역이 공기 청정기라면 미세먼지 제거
            break

        if nx < 0 or nx >= R or ny < 0 or ny >= C:  # 배열을 벗어난다면 방향 바꾸기(반시계 방향)
            up_dir = (up_dir + 3) % 4
            continue

        arr[nx][ny] = temp[x1][y1]   # 한칸씩 미세먼지 이동
        x1, y1 = nx, ny   # 현재 위치 이동

    while True:
        nx = x2 + dx[down_dir]
        ny = y2 + dy[down_dir]

        if nx == air[1][0] and ny == air[1][1]:  # 한바퀴를 돌아서 공기청정기까지 왔다면
            break

        if nx < 0 or nx >= R or ny < 0 or ny >= C:  # 범위를 벗어난다면 방향 전환(시계 방향)
            down_dir = (down_dir + 1) % 4
            continue

        arr[nx][ny] = temp[x2][y2]   # 한칸씩 미세먼지 이동
        x2, y2 = nx, ny   # 현재 위치 이동

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]   # 한 방향으로 정렬(위 오 아 왼)
R, C, T = map(int, input().split())
arr = [[[0 for _ in range(2)] for _ in range(C)] for _ in range(R)]  # 삼중 배열로 선언
air = []    # 공기 청정기 위치 정보
for i in range(R):
    lis = list(map(int, input().split()))
    for j in range(C):
        if lis[j] == -1:
            air.append((i, j))
            arr[i][j][0] = lis[j]
        else:
            arr[i][j][0], arr[i][j][1] = lis[j], lis[j] // 5

for _ in range(T):  # 1000  * (2500 * 4 = 10000) = 10000000
    dust_spread()
    air_clean()
    update()

total_dust = 0
for i in range(R):
    for j in range(C):
        if arr[i][j][0] > 0:
            total_dust += arr[i][j][0]
print(total_dust)

# print(sum(sum([[arr[i][j][0] for j in range(C) if arr[i][j][0] > 0] for i in range(R)], [])))