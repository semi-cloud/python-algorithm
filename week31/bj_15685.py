# 배열 자체를 90도 돌리는 방법 => 중심점이 정해져 있기 때문에 어렵다
# 회전 시키는게 아니라 스택에 새롭게 생기는 선분들의 좌표를 추가(선을 하나씩 다시 추가)
# 선이 추가 되는 방향에는 규칙이 존재 : 이전 선들의 정보는 기억 하고 있으므로 방향만 규칙에 따라서 바꿔서 그대로 추가
# 다음 세대는 스택 탑에서부터 거꾸로 꺼내가면서 만들고, 이전 세대의 방향 + 1
# 이전 세대 => 다음 세대 : 위 => 왼 / 왼 => 아 / 오 => 위 / 아래 => 오

def make_dragon(x, y, d, k):
    arr[x][y] = 1  # 시작점 체크
    path = list()  # 스택에 각 선분의 방향 넣기
    path.append(d)

    for _ in range(k):  # 각 세대 마다 스택을 거꾸로 탐색하면서 스택에 새로운 선분들을 추가
        st = path[:]
        while st:
            new_dir = (st.pop() + 1) % 4
            path.append(new_dir)

    for p in path:
        nx, ny = x + dx[p], y + dy[p]   # 선분 끝 점 계산해서 배열에 표시
        arr[nx][ny] = 1
        x, y = nx, ny

n = int(input())
dragons = [list(map(int, input().split())) for _ in range(n)]
res = 0
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]  # 오, 상, 좌, 하
N = 102  # 101 : 인덱스 에러

# 1. 주어진 드래곤 커브 정보를 맵에 1로 표현
arr = [[0 for _ in range(N)] for _ in range(N)]  # 최대 100 * 100 크기의 격자판
for y, x, d, g in dragons:
    make_dragon(x, y, d, g)  # 좌표 변환

# 2. 전체 맵을 다 돌면서 시작 지점 기준 2 X 2 정사각형이 모두 1로 되어 있는지 체크
for i in range(N):
    for j in range(N):
        if i < 0 or i >= N or j < 0 or j >= N:
            continue
        if arr[i][j] == 1 and arr[i+1][j] == 1 and arr[i][j+1] == 1 and arr[i+1][j+1] == 1:
            res += 1
print(res)


