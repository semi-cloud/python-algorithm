from heapq import heappush, heappop

N = int(input())
heap = []

for _ in range(N):  # 1500
    temp = list(map(int, input().split()))
    for i in range(N):   # 1500
        if len(heap) < N:     # 힙의 길이가 N보다 작다면 힙에 추가
            heappush(heap, temp[i])
        else:                 # 힙의 길이가 N보다 크다면 힙에서 가장 작은 수보다 큰 경우만 힙에 추가
            if heap[0] < temp[i]:    # 가장 큰 N개의 수만 힙에 유지
                heappop(heap)         # 루트 원소인 가장 작은 원소 팝
                heappush(heap, temp[i])  # 새로운 원소 추가

print(heap[0])

