# CCTV의 방향을 적절히 정해서, 사각 지대의 최소 크기를 구하는 프로그램
import copy

def spread(x, y, direct, tmp):
    for d in direct:          # 방향이 여러개일 경우
        nx = x
        ny = y
        while True:
            nx += dx[d]        # 해당 방향 으로 한칸씩 이동
            ny += dy[d]
            print(direct, nx, ny)
            if 0 <= nx < N and 0 <= ny < M and tmp[nx][ny] != 6:    # 벽이 아닌 경우
                if tmp[nx][ny] == 0:        # CCTV를 만나면 무시하고 탐색 진행, CCTV가 아니면 감시
                    tmp[nx][ny] = '#'
            else:             # 벽을 만나면 바로 해당 방향 탐색 종료
                break


def dfs(arr, cnt):     # cnt : 감시할 수 있는 영역
    global result

    tmp = copy.deepcopy(arr)
    if cnt == len(cctv_info):   # 한 방향에 대해서 모든 CCTV를 돌았으면, 최솟값 결과 저장=> 재귀 끝난 후 돌아오면 복사 배열 다시 초기화
        area = 0
        for i in range(N):
            for j in range(M):
                if tmp[i][j] == 0:   # 사각 지대
                    area += 1
        result = min(result, area)
        return

    n, x, y = cctv_info[cnt]
    for dir in direction[n]:       # 한 방향 마다 재귀로 모든 CCTV 를 탐색
        spread(x, y, dir, tmp)
        dfs(tmp, cnt + 1)
        tmp = copy.deepcopy(arr)     # 배열 초기화


N, M = map(int, input().split())
cctv_info, arr = [], []
result = int(1e9)
dx = [1, -1, 0, 0]   # 동 서 남 북
dy = [0, 0, 1, -1]

direction = [    # 회전 시 바라 보는 방향을 미리 저장
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 2], [2, 1], [1, 3], [3, 0]],
    [[3, 0, 2], [1, 3, 0], [0, 2, 1], [2, 1, 3]],
    [[0, 1, 2, 3]],
]

for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(M):
        if 1 <= arr[i][j] < 6:
            cctv_info.append((arr[i][j], i, j))       # CCTV 위치 정보와 값 저장

dfs(arr, 0)
print(result)





