from heapq import heappush, heappop

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
sx, sy = 0, 0
d = [(0, -1), (-1, 0), (0, 1), (1, 0)]       # 좌, 상, 우, 하

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            sx, sy = i, j
            arr[i][j] = 0               # 아기상어 위치 0으로 바꾸기(크기가 9인 상어로 인식 방지)

def bfs(a, b):
    size, move, eat, check = 2, 0, 0, False
    start, end = a, b       # 먹은 위치 정보 저장

    while True:              # 먹으면 먹은 위치 부터 다시 탐색 시작
        que = []
        visit = [[False] * n for _ in range(n)]     # 재방문 가능 하도록 매번 초기화
        heappush(que, (0, start, end))              # 거리와 함께 위치 정보 힙에 저장
        visit[start][end] = True
        check = False

        while que:
            cur, x, y = heappop(que)       # 1)가장 가까운 2)왼쪽 상단 부터 꺼내 오기

            if size > arr[x][y] != 0:       # 물고기를 먹을 수 있는 경우
                eat, arr[x][y] = eat + 1, 0     # 먹고 물고기 제거
                start, end = x, y                # 다시 시작할 위치 지정
                move += cur                     # 이동 시간 합
                check = True                    # 물고기 먹었음 을 표시
                break

            for dx, dy in d:
                nx, ny = x + dx, y + dy

                if nx < 0 or nx >= n or ny < 0 or ny >= n or visit[nx][ny]:    # 방문했거나 범위 넘어가는 경우
                    continue

                if size >= arr[nx][ny]:            # 같거나 작은 경우 에만 이동 가능
                    visit[nx][ny] = True
                    heappush(que, (cur + 1, nx, ny))     # 거리 가까운 순으로 넣기

        if not check:       # 다 돌고도 먹이를 먹은 적이 없음 => 그냥 탈출
            break

        if size == eat:      # 크기만큼 물고기를 먹었으면
            size += 1      # 크기 증가 시키기
            eat = 0        # 먹은 횟수 초기화
    print(move)

bfs(sx, sy)

