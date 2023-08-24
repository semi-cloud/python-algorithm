# 중복이 없는 연속 부분 수열 개수 구하기
# 같은 연속된 배열에만 중복이 없으면 됌 => 투 포인터 활용
# [i - j] 까지 중복 없는 부분 수열 개수 = (j-i) + 1
# ex) 1 2 3 1
# [0] : 19
# [0-1] : 2, 12       (추가)
# [0-2] : 3, 23, 123  (추가)
# [1-3] : 1, 31, 231  (추가)

from collections import defaultdict
N = int(input())  # 100,000
arr = list(map(int, input().split(" ")))
dic = defaultdict(int)
res = 0

i, j = 0, 0
dic[arr[i]] = 1

while i < N and j < N:
    while j < N and dic[arr[j]] <= 1:   # 중복이 발생하기 전까지 증가시키기
        res += (j - i) + 1              # j 증가 시마다 부분 수열 개수 누적
        j += 1                          # 선 증가 후 반영해야 조건문에서 중복 감지 가능
        if j >= N: break
        dic[arr[j]] += 1

    dic[arr[i]] -= 1      # 중복이 발생했으므로 중복 없을 때까지 앞 인덱스 증가
    i += 1

print(res)
