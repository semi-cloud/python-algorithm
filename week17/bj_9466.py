# 어느 프로젝트 팀에도 속하지 않는 학생들의 수를 계산

import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x):
    global count
    visited[x] = True
    traced.append(x)       # 탐색 경로 저장

    next = arr[x]         # 다음에 방문할 정점
    if visited[next]:      # 다음에 방문할 정점이 끝났는지 체크
        if next in traced:   # 다음에 방문할 정점이 탐색 경로에 존재하는 경우에 싸이클이 발생(팀이 구성)
            count += len(traced[traced.index(next):])
    else:
        dfs(next)           # 방문하지 않았다면 탐색 진행


T = int(input())
for _ in range(T):
    n = int(sys.stdin.readline())
    arr = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [False] * (n+1)
    count = 0

    for idx in range(1, n+1):
        if not visited[idx]:         # 이미 팀이 결성 되었다면 검사 X
            traced = []              # 탐색 경로 정보를 담을 스택
            dfs(idx)
    print(n - count)
