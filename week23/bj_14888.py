def dfs(depth, num):   # 깊이, 계산값
    global add, sub, mul, div, arr, max_n, min_n

    if depth == N-1:
        # 트리의 한 줄에 대해서 연산이 끝난 경우(트리에 끝에 도달한 경우) 최대 최솟값 갱신
        max_n = max(max_n, num)
        min_n = min(min_n, num)
        return

    if add > 0:       # 모든 연산자에 대해 트리 형태 재귀적으로 생성
        add -= 1
        dfs(depth+1, num + arr[depth + 1])
        add += 1
    if sub > 0:
        sub -= 1
        dfs(depth + 1, num - arr[depth + 1])
        sub += 1
    if mul > 0:
        mul -= 1
        dfs(depth + 1, num * arr[depth + 1])
        mul += 1
    if div > 0:
        div -= 1
        res = num // arr[depth + 1]
        if num < 0 and arr[depth + 1] > 0:
            res = -(abs(num) // arr[depth + 1])
        dfs(depth + 1, res)
        div += 1


N = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split()) # 각 연산자의 개수

min_n, max_n = float("inf"), float("-inf")
dfs(0, arr[0])   # 첫번째 노드부터 시작
print(max_n)
print(min_n)