# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return
import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)   # 최소 힙으로 생성

    while scoville[0] < K:    # 첫번째 원소가 K 보다 크다면 반복문 종료
        num = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)  # 스코빌 지수 계산 후 힙에 푸시
        heapq.heappush(scoville, num)
        cnt += 1

        if len(scoville) == 1 and scoville[0] < K:    # 마지막의 최종 계산 결과가 K보다 작다면 -1
            return -1
    return cnt

print(solution([1, 2, 3, 9, 10, 12], 7))
