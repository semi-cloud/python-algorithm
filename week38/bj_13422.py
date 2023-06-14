# 붙잡히지 않고 털 수 있는 연속된 집 고르는 방법 개수 구하기
# 조합(완전 탐색) 불가능, O(N) 슬라이딩 윈도우 활용

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split(" "))  # 집(100,000), 홈칠 연속된 집 개수(100,000), 방범 장치 동작 하는 금액
    moneys = list(map(int, input().split(" ")))

    i, j = 0, M-1
    cur_money = 0
    res = 0
    for k in range(M):
        cur_money += moneys[k]

    if N == M:  # 전체 집 개수와 뽑으려는 집 개수가 같은 경우 중복이 생김
        if cur_money < K:
            res = 1
    else:
        while i < N:
            if cur_money < K:
                res += 1

            cur_money -= moneys[i]
            i += 1

            j = (j + 1) % N
            cur_money += moneys[j]
    print(res)
