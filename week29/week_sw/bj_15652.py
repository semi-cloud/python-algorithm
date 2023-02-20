# 1-N까지 자연수 중에 비 내림차순으로 M개를 고른 수열, 같은 수를 여러번 골라도 됌
#          1                   2                    3                       4
# 1(o) 2(o) 3(o) 4(o)  1(x) 2(o) 3(o) 4(o)  1(x) 2(x) 3(o) 4(o)    1(x) 2(x) 3(x) 4(o)

path = []
def dfs(depth):
    if depth == M:
        print(" ".join(map(str, path)))
        return

    for i in range(N):
        if path and path[-1] <= i+1 or depth == 0:      # 이전 경로의 마지막 노드보다 같거나 크다면 탐색 가능
            path.append(i+1)
            dfs(depth + 1)
            path.pop()

N, M = map(int, input().split())
dfs(0)


