# N개의 수를 적은 후 M으로 나누었을 때, 나머지가 모두 같게 되는 M을 모두 찾기( M은 1보다 커야 함)
from math import gcd
from math import sqrt

N = int(input())
arr = [int(input()) for _ in range(N)]
temp, result = [], set()           # 약수들의 중복을 방지하기 위해 집합 선언(2 X 2)
arr.sort()

for i in range(1, N):
    temp.append(arr[i] - arr[i-1])   # (A - B), (B - C) 수 저장

prev = temp[0]
for i in range(1, len(temp)):        # 최대 공약수 구하기
    prev = gcd(prev, temp[i])
result.add(prev)

for i in range(2, int(sqrt(prev))+1):    # 제곱근까지 탐색하여 탐색 시간을 반으로 줄이기
    if prev % i == 0:
        result.add(i)
        result.add(prev // i)            # 제곱근 이후 약수도 같이 추가

print(" ".join(list(map(str, sorted(result)))))














