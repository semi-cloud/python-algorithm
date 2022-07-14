# 서로 다른 옷의 조합의 수를 return
from collections import defaultdict

def solution(clothes):
    d = defaultdict(list)
    for clothe, type in clothes:
        d[type].append(clothe)

    count = 1
    for val in d.values():
        count = count * (len(val) + 1)       # 각각의 경우의 수 구한 후 곱하기
    return count - 1                         # 최소 1개는 입으므로 모두 0인 경우 제외

data = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(data))