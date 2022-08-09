# 개똥벌레가 파괴해야하는 장애물의 최솟값과 그러한 구간이 총 몇 개 있는지 출력
from collections import Counter

N, H = map(int, input().split())
x, y = [0 for _ in range(H+1)], [0 for _ in range(H+1)]    # x : 석순, y : 종유석

for i in range(N):          # h 높이의 석순과 종유석이 몇개 있는지 각각 배열에 저장
    num = int(input())
    if i % 2 == 0:
        x[num] += 1
    else:
        y[num] += 1

px, py = [0 for _ in range(H+1)], [0 for _ in range(H+1)]    # 누적합 구할 배열
px[H], py[1] = x[H], y[H]

for i in range(1, H):               # 경로별 석순과 종유석에 부딪히는 갯수 합하기
    px[H-i] = px[H-i+1] + x[H-i]    # 만나는 석순 개수
    py[i+1] = py[i] + y[H-i]        # 만나는 종유석 개수

temp = [0 for _ in range(H)]
for idx, (a, b) in enumerate(zip(px[1:], py[1:])):
    temp[idx] = a + b

d = Counter(temp)
result = list(sorted(d.keys()))[0]
print(result, d[result])







