# 인접한 공간을 그냥 넘어갈 수는 없고, 길을 건너지 않고 우회해서 갈 수 있다면 OK

# 1. 모든 소들을 2개의 쌍으로 묶음
# 2. 각 소들이 길로 연결되서 갈 수 있는지 체크, 갈 수 있다면 +1
# 3. 각 소들이 인접한데 길이 없는 경우는 대상에서 제외

from itertools import combinations
import sys

input = sys.stdin.readline

dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]  # 하 상 좌 우
def dfs(a, b):     # 길로 연결 해서 도달할 수 있는지 체크
    st = [(a[0], a[1])]   # 소가 있는 위치
    visited = [[False for _ in range(N+1)] for _ in range(N+1)]
    visited[a[0]][a[1]] = True

    while st:
        x, y = st.pop()

        if x == b[0] and y == b[1]:  # 길을 사용하지 않고도 만날 수 있는 경우
            return True

        for i in range(4):
            if road[x][y][i]: continue    # 이어져 있는 길이 있다면 건너지 X

            nx, ny = x + dx[i], y + dy[i]
            if nx <= 0 or nx > N or ny <= 0 or ny > N: continue

            if not visited[nx][ny]:
                visited[nx][ny] = True
                st.append((nx, ny))

    return False

N, K, R = map(int, input().split(" "))
road = [[[False for _ in range(4)] for _ in range(N+1)] for _ in range(N+1)]  # 동서남북 방향에 길이 존재
for _ in range(R):
    x1, y1, x2, y2 = map(int, input().split(" "))
    if x1 + 1 == x2 and y1 == y2:  # 아래
        road[x1][y1][0] = True
        road[x2][y2][1] = True
    elif x1 - 1 == x2 and y1 == y2:  # 위
        road[x1][y1][1] = True
        road[x2][y2][0] = True
    elif x1 == x2 and y1 + 1 == y2:  # 오
        road[x1][y1][3] = True
        road[x2][y2][2] = True
    else:   # 왼
        road[x1][y1][2] = True
        road[x2][y2][3] = True

cows = [list(map(int, input().split(" "))) for _ in range(K)]
res = 0

for cow1, cow2 in list(combinations(cows, 2)):  # 이중 포문으로 하면 빨라짐
    if not dfs(cow1, cow2):  # 반드시 길로만 이동할 수 있는 경우
        res += 1

print(res)


# 이중 포문이 더 속도 느림
# for i in range(K):
#     for j in range(i, K):
#         if not dfs(cows[i], cows[j]):  # 반드시 길로만 이동할 수 있는 경우
#             res += 1

# 이렇게 저장 해주면 틀림
# for _ in range(R):
#     x1, y1, x2, y2 = map(int, input().split(" "))
#     road[x1][y1].append([x2, y2])
#     road[x2][y2].append([x1, y1])
