# 크기가 양수인 부분 수열 중에서, 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하기
from collections import defaultdict

def right_seq(mid, sum):
    if mid == n:
        result[sum] += 1   # 합의 경우의 수 저장
        return

    right_seq(mid + 1, sum + arr[mid])
    right_seq(mid + 1, sum)


def left_seq(st, sum):
    global cnt
    if st == n // 2:
        cnt += result[s - sum]
        return

    left_seq(st + 1, sum + arr[st])
    left_seq(st + 1, sum)

n, s = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
result = defaultdict(int)
cnt = 0

right_seq(n // 2, 0)  # 절반씩 수행
left_seq(0, 0)

if s == 0:      # 공집합인 경우
    cnt -= 1
print(cnt)
