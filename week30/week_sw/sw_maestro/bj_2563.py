# 2번 유사 문제
# 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이 구하기 => 겹치는 영역 또는 선분 찾기
# 방법 1 : 겹치는 영역을 전체 영역에서 제거
# 방법 2 : 그냥 1로 칠해진 영역만 구하면 전체 색종이 넓이가 나옴

n = int(input())
arr = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):   # 색종이 영역들은 1 더해주기 => 겹치는 부분은 2가 됌
            arr[i][j] = 1
            # arr[i][j] += 1

ans = 0
for a in arr:
    ans += sum(a)

# overlap = 0
# for i in range(100):
#     for j in range(100):
#         if arr[i][j] == 2:
#             overlap += 1

print(ans)





