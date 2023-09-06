# 특정 층에서 최대 P개 전구를 반전시켜서 얻을 수 있는 경우의 수

N, K, P, X = map(int, input().split(" ")) # 층수, 자리수, 최대 반전 가능한 개수, 현재 층
nums = [
    [1, 1, 1, 1, 1, 1, 0],  # 0 -9 숫자를 표현하는 배열
    [0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1]
]

def find_switch_count(a, b):  # a에서 b로 바꾸려면 총 몇개의 전구 반전이 필요하느냐
    switch = 0
    for i in range(7):
        if a[i] != b[i]:
            switch += 1
    return switch

# 자리수 별로 따로 경우의 수 구하는게 아니라, 총 자리수 모두 합쳐셔 반전 횟수를 구하기
res = 0
for num in range(1, N+1):   # 모든 숫자를 탐색하면서 가능한지 체크
    if num == X:        # 자기 자신은 제외
        continue

    cnt = 0
    target, origin = str(num), str(X)
    target = "0" * (K-len(target)) + target
    origin = "0" * (K-len(origin)) + origin

    for i in range(K):      # 각 자리수 별로 체크
        cnt += find_switch_count(nums[int(target[i])], nums[int(origin[i])])

    if cnt <= int(P):   # 반전시킬 수 있는 개수보다 작거나 같고 N범위 안에 잇으면 OK
        res += 1
print(res)

# res = 1
# for i in range(int(K)):
#     idx = int(X[i])
#
#     possible = 0
#     for num in range(10):   # 모든 숫자를 탐색하면서 가능한지 체크
#         if num == idx:   # 자기 자신은 제외
#             continue
#
#         cnt = find_switch_count(nums[idx], nums[num])
#         if cnt <= int(P) and num <= int(N[i]):    # 반전시킬 수 있는 개수보다 작거나 같고 N범위 안에 잇으면 OK
#             print(num)
#             possible += 1
#
#     res *= possible
#     print()
# print(res - 1)  # 0 0 이 되는 경우의 수 제외
