import sys
from collections import defaultdict

def solution(enroll, referral, seller, amount):  # 10,000
    sys.setrecursionlimit(10 ** 6)
    N = len(enroll)
    people = defaultdict(int)
    people['center'] = 0  # 루트 노드 표시

    graph = [0 for _ in range(N + 1)]  # 부모 정보 노드
    for idx, e in enumerate(enroll):
        people[e] = idx + 1

    for idx, r in enumerate(referral):
        if r == "-":  # 부모가 센터인 경우
            graph[idx + 1] = 0  # 자식 -> 부모 방향으로 탐색
        else:
            graph[idx + 1] = people[r]

    def dfs(i, money):
        if i == 0:  # 센터인 경우 끝
            return

        total_money = money  # 부모는 이거 필요 없음
        give = int(total_money * 0.1)
        parent = graph[i]
        if give >= 1:   # 1원 이상인 경우에만 전달(부모 노드로 계속 전달)
            ans[i] += total_money - give
            dfs(parent, give)
        else:
            ans[i] += total_money

    M = len(seller)
    ans = [0 for _ in range(N + 1)]
    for i in range(M):
        dfs(people[seller[i]], amount[i] * 100)
    return ans[1:]  # 센터 제외 하고 출력
