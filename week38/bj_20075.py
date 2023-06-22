import sys
input = sys.stdin.readline

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]  # 왼, 아, 오, 위(반시계 방향 이동)
def move():
    x, y = N // 2, N // 2
    k, d = 1, 0   # 같은 방향 커지는 정도

    while True:
        if x == 0 and y == 0: break

        for _ in range(2):
            for _ in range(k):
                x, y = x + dx[d], y + dy[d]  # 반시계 방향으로 토네이도 이동
                spread(x, y, d)
            d = (d + 1) % 4

        # 맨 위쪽 줄 이동
        if k == N-1:
            for _ in range(k):
                x, y = x + dx[d], y + dy[d]
                spread(x, y, d)
        k += 1

def spread(a, b, dir):  # 모래 분배(이미 있다면 기존에서 더해짐)
    global out_sand
    spin_spread = spins[dir]
    total = arr[a][b]
    left_sand = total
    arr[a][b] = 0     # y 자리에 존재하던 모래 제거

    x, y = a-2, b-2   # 시작 위치 기준 배열의 첫번째 원소부터 탐색
    for i in range(x, x + 5):
        for j in range(y, y + 5):
            amount = int(total * spin_spread[i - x][j - y])

            if spin_spread[i-x][j-y] > 0:
                if i < 0 or i >= N or j < 0 or j >= N:  # 범위를 넘어간다면 결과에 추가
                    out_sand += amount
                else:                         # 아니라면 기존 배열에 반영
                    arr[i][j] += amount
                left_sand -= amount          # 분배된 만큼 총 모래 양에서 제거

    na, nb = a + dx[dir], b + dy[dir]        # a 자리에는 이동하지 않은 남은 양 저장
    if na < 0 or na >= N or nb < 0 or nb >= N:
        out_sand += left_sand
    else:
        arr[na][nb] += left_sand

def rotate(lis):
    new_lis = list(reversed(list(zip(*lis))))
    return new_lis

N = int(input())
arr = [list(map(int, input().split(" "))) for _ in range(N)]
out_sand = 0
left = [[0, 0, 0.02, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0.05, 0, 0, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0, 0, 0.02, 0, 0]]
down = rotate(left)
right = rotate(down)
up = rotate(right)
spins = [left, down, right, up]
move()
print(out_sand)


