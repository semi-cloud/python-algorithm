# 로봇 이동 경로가 단순할 확률 구하기 = 모든 위치가 한번만 방문하는 경로
# 각 방향의 확률 = 25 25 25 25 : E W S N => 개수로 변환해서 N개 순열 생성 => 그 중에 단순한 경로만 뽑아내기
# 답 : 방문했던 곳을 다시 방문하지 않으면서 N번 이동 가능한 확률 => 중복이 없는 경로의 확률들을 모두 더하면 됌 => 한 경로의 확률을 구할 때는 그냥 곱해주면 됌

d = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # 동 서 남 북
# 방문 해제가 필요하므로 DFS 스택으로 하면 X
def bt(x, y, p, cnt):  # 경로 배열을 받음, 애초에 확률을 계산 하면서 탐색
    global ans
    if cnt == N:
        ans += p
        return

    for i in range(4):   # 방향 순열 생성
        nx, ny = x + d[i][0], y + d[i][1]
        if nx < 0 or nx > 30 or ny < 0 or ny > 30: continue

        if not visit[nx][ny]:
            visit[nx][ny] = True
            bt(nx, ny, p * percents[i], cnt + 1)
            visit[nx][ny] = False

N, *lis = map(int, input().split())
visit = [[False for _ in range(31)] for _ in range(31)]  # N : 최대 15
percents = []
ans = 0

for i in range(4):
    percents.append(lis[i] * 0.01)  # 확률 구하기(25 -> 0.25)

visit[15][15] = True
bt(15, 15, 1, 0)
print(ans)
# print(float(sub) / float(total))
