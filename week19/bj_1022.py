r1, c1, r2, c2 = map(int, input().split())  # 왼쪽 위, 오른쪽 아래 칸(총 가로 세로 길이)
N, M = (r2 - r1 + 1), (c2 - c1 + 1)
arr = [[0 for _ in range(M)] for _ in range(N)]
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
total = N * M

x, y = 0, 0
direct, cnt, d, length = 0, 1, 1, 0
while total > 0:              # 출력 배열의 원소 개수
    for i in range(2):        # 2회씩 반복
        for j in range(d):    #
            if r1 <= x <= r2 and c1 <= y <= c2:   # 출력 하고자 하는 범위 내에 있다면
                arr[x - r1][y - c1] = cnt
                total -= 1
                length = max(length, len(str(cnt)))
            x += dx[direct]
            y += dy[direct]
            cnt += 1
        direct = (direct + 1) % 4    # 방향 전환
    d += 1

for i in range(N):
    for j in range(M):
        print(str(arr[i][j]).rjust(length), end=' ')   # 문자를 공백을 삽입해 오른쪽 정렬
    print()





