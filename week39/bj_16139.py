# 해당 범위 내에 특정 알파벳이 몇 번 나타나는지 구하기

import sys
input = sys.stdin.readline

s = input()
m = len(s)
dp = [[0 for _ in range(26)] for _ in range(m+1)]

for i in range(1, m + 1):   # 각 알파벳 별로 누적합 채우기
    for j in range(26):  # 각 문자열 인덱스 마다 26개(알파벳 별로) 누적합 배열 존재
        idx = ord(s[i-1]) - 97
        if idx == j:     # 알파벳에 해당하는 자리 찾기
            dp[i][j] = dp[i-1][j] + 1
        else:
            dp[i][j] = dp[i-1][j]

n = int(input())
for i in range(n):  # 2000
    alpha, l, r = input().split(" ")
    alpha, l, r = ord(alpha) - 97, int(l), int(r)
    print(dp[r+1][alpha] - dp[l][alpha])  # 해당 구간의 알파벳 개수

# 시간 초과 : 딕셔너리 사용
# from collections import defaultdict
#
# s = input()
# n = int(input())
# d = defaultdict(list)
#
# for i in range(len(s)):  # 2000
#     d[s[i]].append(i)
#
# for i in range(n):  # 2000
#     res = 0
#     alpha, l, s = input().split(" ")
#     l, s = int(l), int(s)
#
#     for idx in d[alpha]:  # 2000
#         if l <= idx <= s:
#             res += 1
#     print(res)

