# N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 비교 횟수의 최소값 출력
# N이 100,000 + 제한 2초(4천만) : 완전 탐색은 불가능(N^2), 조합을 찾는 것도 불가능(2^n = n이 30만 되도 8자리수)
# 1. dp 방식으로는 O(N^3) 이므로 시간 초과
# 2. 우선순위 큐(그리디 방식)이용 : O(N*LogN)의 시간으로 구현

# 백준 99퍼에서 틀리는 경우 N의 경계값(1~100,000) 도 체크 해주기
import heapq, sys

N = int(input())
sizes = []
for i in range(N):    # sizes 배열을 따로 받고 heapq.heapify(sizes) 보다 시간이 빠름
    heapq.heappush(sizes, int(sys.stdin.readline()))
ans = 0

if N > 1:  # 숫자 묶음이 하나 밖에 없다면 합칠 수 없음

    # 매 카드를 섞을때 마다 가장 작은 값을 꺼내 와서 더해 줘야함
    while heapq:    # 모든 노드를 거치므로 O(N)
        # 가장 작은 값 두 개 꺼내서 더하고, 다시 힙에 푸시
        sums = heapq.heappop(sizes) + heapq.heappop(sizes)  # O(1)
        heapq.heappush(sizes, sums)    # O(logN)
        ans += sums

        if len(sizes) == 1:
            break

print(ans)

# 틀린 코드
# 반례 : 30 40 50 60 (답:360/내 코드:370)
# (30 + 40) + (50 + 60) 일때 가장 작음 : 카드 묶음이 작은 순서대로 더해 나가면 최솟값을 도출할 수 없음
# N = int(input())
# sizes = [int(input()) for _ in range(N)]
# sizes.sort()
#
# sums = {-1: 0}
# for idx in range(N):
#     sums[idx] = sums[idx - 1] + sizes[idx]
#
# ans = sizes[0] + sizes[1]
# for i in range(2, N):        # (10 + 20) + (10 + 20 + 30) + ... + (10 + ... N)
#     ans += sums[i]
#
# print(ans)




