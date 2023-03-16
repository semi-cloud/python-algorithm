# m번의 합체를 모두 끝낸 뒤, 만들 수 있는 가장 작은 점수 구하기

from heapq import heappush, heappop, heapify

n, m = map(int, input().split())
card = list(map(int, input().split()))
heapify(card)

for i in range(m):  # 가장 작은 두 수를 골라서 덮어 씌우기(그리디)
    a = heappop(card)
    b = heappop(card)
    heappush(card, a + b)
    heappush(card, a + b)

print(sum(card))