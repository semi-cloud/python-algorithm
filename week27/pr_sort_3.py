# H-index : 논문 N편 중, h번 이상 인용된 논문이 h편 이상이고, 나머지 논문들이 h편 이하로 인용되는 최대값

from bisect import bisect

def solution(citations):
    citations.sort()

    ans, cur = 0, 0
    for idx in range(len(citations) + 1):   # idx = H-index 가능 범위(최대값은 논문 개수)
        if idx not in citations:
            cur = bisect(citations, idx)    # 존재하는 수가 아니라면 들어갈 위치 구하기
        else:
            cur = citations.index(idx)     # 존재하는 수라면 위치 구하기

        if len(citations) - cur >= idx:    # h번 이상으로 인용된 논문이 h개 이상, 나머지 논문이 h편 이하
            ans = max(ans, idx)
    return ans

print(solution([3, 4, 5, 11, 15, 16, 17, 18, 19, 20]))
print(solution([10, 10, 10, 10, 10]))
