from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
house, chicken = [], []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append([i, j])      # 집 위치 저장
        if arr[i][j] == 2:
            chicken.append([i, j])    # 치킨집 위치 저장

result = float('inf')
for c in combinations(chicken, M):    # M개의 치킨집 선텍
    total = 0                         # 도시의 치킨 거리
    for loc in house:
        temp = float('inf')           # 집 으로 부터 선택한 M개의 모든 치킨 집 중 최단 거리(치킨 거리)
        for j in range(M):
            temp = min(temp, abs(loc[0] - c[j][0]) + abs(loc[1] - c[j][1]))     # 거리 구하기
        total += temp
    result = min(result, total)   # 모든 치킨집 조합에 대해 가장 최단 거리 구하기

print(result)









