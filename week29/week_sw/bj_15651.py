# 1-N까지 자연수 중에 M개를 고른 수열, 같은 수를 여러번 골라도 됌(대신 수열 자체의 중복은 불가능)
#          1                   2                  3
#    1     2     3          1  2  3            1  2  3
# 1 2 3  1 2 3  1 2 3  1 2 3 1 2 3 1 2 3  1 2 3 1 2 3 1 2 3

path = []
def dfs(depth):
    if depth == M:
        print(" ".join(map(str, path)))
        return

    for i in range(N):
        path.append(i+1)
        dfs(depth + 1)
        path.pop()

N, M = map(int, input().split())
dfs(0)


