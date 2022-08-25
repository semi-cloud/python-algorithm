# 명함을 회전 시켜서 모든 명함을 수납할 수 있는 가장 작은 지갑의 크기 찾기

def solution1(sizes):        # 풀이 1
    # 각 사이즈 마다 큰 수와 작은 수를 각각 배열에 담고, 큰거 중에 가장 큰거 * 작은거 중에 가장 큰거
    return max([max(x) for x in sizes]) * max([min(x) for x in sizes])


def solution2(sizes):         # 풀이 2
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:           # 한쪽 으로 큰거와 작은 것을 몰고 최댓값 계산
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col

print(solution1([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))



