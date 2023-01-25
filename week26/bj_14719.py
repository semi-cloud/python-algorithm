# 고이는 빗물의 총량을 구하기
# 기존 풀이 : 직접 2차원 배열에 벽을 세우고, 빈 공간을 만나면 그 다음 벽을 만나기 전까지 물을 채우는 방식으로 진행

H, W = map(int, input().split())
blocks = list(map(int, input().split()))  # 각 위치의 블록이 쌓인 높이

ans = 0
for i in range(1, W-1):   # 첫번째 칸과 마지막 칸 제외 세로 방향으로 탐색(물이 고일 수 없음)
    cur = blocks[i]
    left = max(blocks[:i])   # 왼쪽 방향으로 가장 큰 블럭 높이
    right = max(blocks[i+1:])  # 오른쪽 방향으로 가장 큰 블럭 높이

    if cur < left and cur < right:   # 현재 위치의 블럭 보다 양쪽에 있는 가장 큰 블럭의 높이가 높아야 빗물이 고임
        ans += min(left, right) - cur     # 빗물이 고이는 양 : 양 옆 둘중에 작은 높이 - 현재 블럭의 높이

print(ans)