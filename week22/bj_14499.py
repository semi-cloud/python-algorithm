# 주사위가 이동했을 때 마다 상단에 쓰여 있는 값을 구하는 프로그램
# 이동 = 해당 명령어 방향으로 굴리면서 한칸 이동하는 것
# 인덱스를 주사위의 각 자리(면)으로 고정시킨 후, 주사위를 굴리면서 변하는 숫자는 값에 넣으면서 해결

N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))  # 주사위 이동 명령어
dice = [0 for _ in range(7)]         # 주사위 6면
dx = [0, 0, -1, 1]   # 동 서 북 남
dy = [1, -1, 0, 0]


def roll(dir):      # 각 방향으로 주사위 굴려서 변하는 규칙
    if dir == 1:   # 동
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif dir == 2:   # 서
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif dir == 3:  # 북
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    else:          # 남
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]


for c in command:
    nx = x + dx[c-1]    # 주사위 이동 칸
    ny = y + dy[c-1]

    if not 0 <= nx < N or not 0 <= ny < M:   # 바깥 이동은 명령어 무시
        continue

    x, y = nx, ny          # 주사위를 던지고 맵에서 벗어난다면 이동 전 자리 유지
    roll(c)                # 주사위 굴리기
    if arr[x][y]:          # 칸에 쓰여 있는 수가 0이 아닌 경우 칸 => 주사위 바닥면
        dice[6] = arr[x][y]
        arr[x][y] = 0
    else:                  # 칸에 쓰여 있는 수가 0인 경우 주사위 바닥면 => 칸
        arr[x][y] = dice[6]
    print(dice[1])         # 상단 숫자 출력