# 1-N 중복 없이 오름차순으로 M개 고른 수열 찾기(조합)
#       1[T F F F]            2[T T F F]             3 [T T T F]             4[T T T T]      // depth = 0
# 1(x) 2(o) 3(o) 4(o)   1(x) 2(x) 3(o) 4(o)     1(x) 2(x) 3(x) 4(o)    1(x) 2(x) 3(x) 4(x)   // depth = 1
# T T F F / T T T F / T T T T

path = []
def dfs(depth, visit):
    if depth == M:
        print(" ".join(map(str, path)))
        return

    for i in range(N):
        n = i+1
        if not visit[n]:
            visit[n] = True      # 중복이 없어야 하므로 순열과 달리 방문 여부를 다시 거짓으로 만들지 X
            path.append(n)
            dfs(depth + 1, visit[:])
            path.pop()

N, M = map(int, input().split())
visited = [False for _ in range(N+1)]   # 노드 방문 여부 체크
dfs(0, visited)

