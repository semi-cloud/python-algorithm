# 여러 회전 연산이 있을 때 순서에 따른 배열의 최소값 구하기

def move(copy, r, c, s):  # 시계 방향으로 한 칸씩 돌리는 함수(정사각형)
    lx, ly, rx, ry = r-s-1, c-s-1, r+s-1, c+s-1
    R = (rx - lx) + 1

    for i in range(R // 2):   # 껍질의 개수 만큼 회전 반복
        dir = 0       # 오른쪽 방향 부터 시작
        start_x, start_y, end_x, end_y = lx + i, ly + i, rx - i, ry - i
        x, y = start_x, start_y
        temp = copy[x][y]

        while dir < 4:   # 네 방향에 대해 수행
            nx, ny = x + dx[dir], y + dy[dir]

            if nx == start_x and ny == start_y:   # 시작점 바로 이전의 값을 저장한 temp 상태를 유지하기 위해 바로 종료
                break

            if start_x <= nx <= end_x and start_y <= ny <= end_y:  # 범위 내에 있다면 해당 방향으로 값 이동
                prev = copy[nx][ny]     # 다음 값 보존
                copy[nx][ny] = temp
                temp = prev
                x, y = nx, ny
            else:
                dir += 1   # 범위를 벗어나면 방향 시계 방향으로 회전
        copy[start_x][start_y] = temp           # 네바퀴 돌고 마지막 원소 첫번째 자리에 저장


def dfs(depth, copy):
    global ans
    if depth == K:       # 모든 회전을 완료하면
        for c in copy:   # 배열 A의 값 구하기
            ans = min(ans, sum(c))
        return

    for idx, spin in enumerate(spins):
        r, c, s = spin
        if not visit[idx]:
            visit[idx] = True
            temp_arr = [a[:] for a in copy]   # 기존 배열을 먼저 복사하고 회전 진행
            move(temp_arr, r, c, s)      # 시계방향으로 회전
            dfs(depth + 1, temp_arr)  # 배열의 복사본을 전달
            visit[idx] = False

import sys

N, M, K = map(int, input().split())    # 범위가 작으므로 완전 탐색
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
spins = [list(map(int, input().split())) for _ in range(K)]
visit = [False for _ in range(K)]   # 각 회전 종류의 방문 체크
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

ans = float("inf")
dfs(0, arr)
print(ans)
