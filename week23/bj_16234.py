# 각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지 구하는 프로그램

import copy

from collections import defaultdict

def dfs(a, b, num):
    cnt, people = 0, 0       # 연합 내부의 나라 개수, 인구 개수
    st = [(a, b)]
    visited[a][b] = num

    while st:
        x, y = st.pop()
        cnt += 1
        people += arr[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 > nx or nx >= N or 0 > ny or ny >= N:
                continue

            if visited[nx][ny] == 0 and L <= abs(arr[nx][ny] - arr[x][y]) <= R:   # 국경이 열릴 수 있는 경우
                visited[nx][ny] = num    # 연합 집합에 추가된 노드만 방문 처리
                st.append((nx, ny))
    return cnt, people


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
union = defaultdict(int)
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
day = 0
flag = False

while True:
    # 1. 인구 이동
    temp = copy.deepcopy(arr)   # 반복 시작 할때의 인구 상태를 저장해놓고, 끝에서 변했는지 체크
    visited = [[0 for _ in range(N)] for _ in range(N)]    # 방문 처리 및 연합 구분 배열(방문 > 0)
    num = 1             # 각 연합을 구분하기 위한 숫자

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:   # 이미 연합이 생성된 노드는 검사 하지 않음
                cnt, people = dfs(i, j, num)
                if cnt > 0 and people > 0:        # 연합이 생성된 경우 총 인구 수 / 나라 개수 값을 연합 마다 저장
                    union[num] = people // cnt
                num += 1

    # 2. 다시 돌면서 연합 마다 숫자 갱신
    for i in range(N):
        for j in range(N):
            arr[i][j] = union[visited[i][j]]

    if temp == arr:  # 인구 이동이 더이상 발생 하지 않는다면 종료
        break
    day += 1
print(day)


