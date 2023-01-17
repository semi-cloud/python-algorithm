# K년 후 살아있는 나무 개수 구하기

from collections import deque
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
trees = [[deque() for _ in range(N)] for _ in range(N)]
for i in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

map = [[5 for _ in range(N)] for _ in range(N)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

while K > 0:
    # 봄 : 양분 먹고 업데이트
    for i in range(N):
        for j in range(N):
            for k in range(len(trees[i][j])):
                age = trees[i][j][k]
                if map[i][j] >= age:     # 땅에 양분이 충분한 경우 먹기
                    map[i][j] -= age       # 먹은 만큼 양분 업데이트
                    trees[i][j][k] += 1    # 나이 증가  [0, 1, 2]
                else:            # 땅에 양분이 충분 하지 않은 경우 죽은 나무 처리
                    for _ in range(k, len(trees[i][j])):   # 죽어야 하는 나무 이후의 나무 까지 다 제거(어짜피 나이가 많아서..죽음)
                        map[i][j] += trees[i][j].pop() // 2
                    break        # 큐의 길이가 변동 되므로 멈춰야 인덱스 발생 X

    # 가을 : 나무 번식
    for i in range(N):
        for j in range(N):
            for age in trees[i][j]:
                if age % 5 == 0:  # 나무 나이가 5의 배수
                    for k in range(8):  # 인접한 8개의 칸에 나이가 1인 나무 생성
                        nx = i + dx[k]
                        ny = j + dy[k]

                        if 0 <= nx < N and 0 <= ny < N:
                            trees[nx][ny].appendleft(1)   # 정렬할 필요 없도록 나이 1 나무는 왼쪽에 추가
    # 겨울 : 로봇이 양분 추가
    for x in range(N):
        for y in range(N):
            map[x][y] += arr[x][y]
    K -= 1  # 해가 지나감

alive = 0
for i in range(N):
    for j in range(N):
        alive += len(trees[i][j])
print(alive)
