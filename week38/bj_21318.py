# i > i+1 => 실수를 함, 실수를 하는 곡 개수 구하기
# 매 질문 마다 검사 => O(N) * O(M) = 최악 100,000,000,00

import sys
input = sys.stdin.readline

N = int(input())  # 100,000
arr = list(map(int, input().split(" ")))
M = int(input())  # 100,000
quests = [list(map(int, input().split(" "))) for _ in range(M)]
sum = [0 for _ in range(N)]

# 특정 구간에 감소하는 수열 개수를 누적 저장해두면, 바로 구할 수 있음
for i in range(1, N):
    if arr[i-1] > arr[i]:  # 수열이 감소한다면
        sum[i] = sum[i-1] + 1
    else:
        sum[i] = sum[i-1]

for i, j in quests:
    print(sum[j-1] - sum[i-1])
