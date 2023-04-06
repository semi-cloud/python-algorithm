# 총 K번 회전시킨 이후에 네 톱니바퀴의 점수의 합을 출력
# 1. 모든 톱니바퀴는 초기 상태에서 회전 하기 전에 값으로 맞닿아 있는 부분이 같은지 안 같은지 판단 해야함(배열에 저장)
# 2. 회전한 배열에 인접해 있는 거를 탐색, 앞에서 구한 값이 다르면 회전 아니면 그냥 냅둠

from collections import deque

def rotate_gear(temp, d, N):
    res = [0 for _ in range(N)]
    if d == -1:  # 반 시계 방향
        for i, a in enumerate(temp):
            res[(i - 1 + N) % N] = a
    else:
        for i, a in enumerate(temp):
            res[(i + 1) % N] = a
    return res

def check_match():
    for i in range(3):
        if arr[i][2] == arr[i+1][6]:
            is_rotate[i] = False

arr = [list(map(int, input())) for _ in range(4)]
k = int(input())  # 회전 횟수
rotate = [list(map(int, input().split())) for _ in range(k)]

for i, dir in rotate:  # 100
    visit = [False for _ in range(4)]
    is_rotate = [True for _ in range(3)]
    i -= 1
    q = deque([])
    q.append((i, dir))

    check_match()
    while q:      # 돌린 톱니바퀴를 큐에 추가 해서 연쇄 작용
        idx, d = q.popleft()  # 톱니바퀴 종류와 회전 방향 검사
        if not visit[idx] and idx == i:
            visit[idx] = True
            arr[i] = rotate_gear(arr[idx], d, 8)  # 현재 톱니바퀴는 나중에 돌림(인접한 톱니에 영향을 주면 X)

        if idx - 1 > -1:
            if not visit[idx - 1]:
                visit[idx - 1] = True
                if is_rotate[idx - 1]:  # 회전이 필요한 톱니바퀴만 탐색에 추가
                    arr[idx - 1] = rotate_gear(arr[idx - 1], -d, 8)
                    q.append((idx - 1, -d))

        if idx + 1 < 4:
            if not visit[idx + 1]:
                visit[idx + 1] = True
                if is_rotate[idx]:
                    arr[idx + 1] = rotate_gear(arr[idx + 1], -d, 8)
                    q.append((idx + 1, -d))

total = 0
for i, a in enumerate(arr):
    if a[0] == 1: total += 2**i  # 12시 방향 S 극이면 1점
print(total)