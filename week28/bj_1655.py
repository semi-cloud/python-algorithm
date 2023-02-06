# 매 수가 추가될 때마다 중간값 찾기
# 매 수가 입력될 때마다 정렬이 일어나는 것은 비 효율적(N * NlogN(퀵소트), 최악의 경우 N * N^2 => 시간 초과)
# 힙은 무조건 최대/최소값 밖에 꺼낼 수 없기 때문에 힙에 넣는 조건 및 정렬 방식을 바꾸거나 최대/최소 힙 두개 사용

# 0. 일단 들어오는 거는 최대 힙에 삽입
# 1. 두 힙의 크기는 항상 최대 힙이 최소 힙보다 같거나(1 2 3 / 4 5 6), 하나 더 많아야함(1 2 4 / 7 10)
# 2. 최대 힙의 탑은 최소 힙의 탑보다 작거나 같아야 함
# 2번 규칙에 어긋 난다면 최대 힙의 탑을 최소 힙으로 이전, 3번 규칙에 어긋 난다면 서로의 탑을 체인지 => 항상 최대 힙의 탑에는 중간 값이 존재하게 됨

import sys
from heapq import heappush, heappop

N = int(input())
min_q, max_q = [], []

for i in range(N):  # N * LogN
    num = int(sys.stdin.readline())
    heappush(max_q, (-num, num))      # 일단 최대 힙에 추가

    if len(max_q) - len(min_q) > 1 or len(max_q) - len(min_q) < 0:  # 1. 두 힙의 크기는 같거나, 최대 힙이 하나 더 많아야함(중간값이 최대 힙의 탑)
        temp_max = heappop(max_q)     # 최대 힙의 탑을 빼서 민 힙에 추가하여 비율 맞추기
        heappush(min_q, temp_max[1])

    if min_q and max_q[0][1] > min_q[0]:  # 힙에서 원소 빼내지 않고 최대/최솟값 찾는 방법 max_q[-1] (X)
        a, b = heappop(max_q)[1], heappop(min_q)
        if a > b:              # 2. 만약 최대 힙의 탑이 최소 힙의 탑보다 크다면(1 2 [10] : 최대힙 / [4] 5 : 최소힙 => [10]과 [4] 교환)
            heappush(max_q, (-b, b))   # 두 힙의 탑을 서로 교환해서 더 작은 숫자가 최대 힙으로 가도록 조정
            heappush(min_q, a)
    print(max_q[0][1])        # 위 두가지 규칙이 지켜진다면, 최대 힙의 탑이 중간값으로 설정 됌 / min()은 시간 복잡도 O(N)이므로 시간 초과

