# 지도가 주어졌을 때, 지나갈 수 있는 길의 개수를 구하기

# 2. 높이가 같으면 지나감, 같지 않다면 경사로를 놓을 수 있는지 탐색
# 2-1. 인접한 높은 곳과 차이 1
# 2-2. 같은 숫자가 L개 이상 연속 되어 있는가
# 3. 갈 수 있다면 경사로 방문 체크 따로 필요

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

# 가로 방향 길 체크
visit = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):  # 하나의 길
    can_go = True
    for j in range(N - 1):
        if abs(arr[i][j + 1] - arr[i][j]) > 1:  # 높이가 1 차이 보다 많이 난다면 경사로를 놓을 수 없으면 그 길은 갈 수 X
            can_go = False
            break

        if arr[i][j] == arr[i][j + 1]: continue  # 높이가 같으면 패스

        if arr[i][j] < arr[i][j + 1]:  # 올라가는 경사로(왼쪽에 놓을 수 있는지 체크)
            temp = arr[i][j]
            for idx in range(L):
                if j - idx < 0 or arr[i][j - idx] != temp or visit[i][j - idx]:  # 경사로가 이미 놓아져 있는 경우
                    visit[i] = [False for _ in range(N)]  # 해당 행에서 앞에서 두었던 경사로 까지 모두 초기화
                    can_go = False  # 갈 수 없는 길이라 판명
                    break
            else:
                for idx in range(L):  # 경사로 놓기
                    visit[i][j - idx] = True

        elif arr[i][j] > arr[i][j + 1]:  # 내려가는 경사로(오른쪽에 놓을 수 있는 체크)
            temp = arr[i][j + 1]
            for idx in range(1, L + 1):
                if j + idx >= N or arr[i][j + idx] != temp or visit[i][j + idx]:  # 경사로가 이미 놓아져 있는 경우
                    visit[i] = [False for _ in range(N)]
                    can_go = False
                    break
            else:
                for idx in range(1, L+1):  # 경사로 놓기
                    visit[i][j + idx] = True
    if can_go:
        ans += 1  # 갈 수 있는 길 판명

# 세로 방향 길 체크
visit = [[False for _ in range(N)] for _ in range(N)]
for j in range(N):  # 하나의 길
    can_go = True
    for i in range(N - 1):
        if abs(arr[i + 1][j] - arr[i][j]) > 1:  # 높이가 1 차이 보다 많이 난다면 경사로를 놓을 수 없으면 그 길은 갈 수 X
            can_go = False
            break

        if arr[i][j] == arr[i + 1][j]: continue  # 높이가 같으면 패스

        if arr[i][j] < arr[i + 1][j]:  # 올라가는 경사로(왼쪽에 놓을 수 있는지 체크)
            temp = arr[i][j]
            for idx in range(L):
                if i - idx < 0 or arr[i - idx][j] != temp or visit[i - idx][j]:  # 경사로가 이미 놓아져 있는 경우
                    visit[j] = [False for _ in range(N)]   # 해당 열에서 앞에서 두었던 경사로 까지 모두 초기화
                    can_go = False  # 갈 수 없는 길이라 판명
                    break
            else:
                for idx in range(L):  # 경사로 놓기
                    visit[i - idx][j] = True

        elif arr[i][j] > arr[i + 1][j]:  # 내려가는 경사로(오른쪽에 놓을 수 있는 체크)
            temp = arr[i + 1][j]
            for idx in range(1, L + 1):
                if i + idx >= N or arr[i + idx][j] != temp or visit[i + idx][j]:  # 경사로가 이미 놓아져 있는 경우
                    visit[j] = [False for _ in range(N)]
                    can_go = False  # 갈 수 없는 길이라 판명
                    break
            else:
                for idx in range(1, L + 1):  # 경사로 놓기
                    visit[i + idx][j] = True
    if can_go:
        ans += 1  # 갈 수 있는 길 판명
print(ans)

