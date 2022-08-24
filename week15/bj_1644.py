# 자연수가 주어졌을 때, 이 자연수를 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 구하기
import math

def find_prime_number():         # N보다 작거나 같은 모든 소수를 찾기
    primes = []
    for i in range(2, int(math.sqrt(N)) + 1):
        if arr[i]:
            j = 2
            while i * j <= N:       # 배수들 제거
                arr[i * j] = False
                j += 1

    for i in range(2, N+1):
        if arr[i]:
            primes.append(i)
    return primes


N = int(input())
arr = [True for i in range(N+1)]
p = find_prime_number()

right, cnt, temp = 0, 0, 0
for left in range(len(p)):                    # N까지의 소수들만 존재하는 배열
    while temp < N and right < len(p):        # 타겟 수보다 커지기 전까지 오른쪽 포인터 이동
        temp += p[right]                  # 구간합 구하기
        right += 1                        # 오른쪽 포인터 이동

    if temp == N:          # 타겟 수와 같다면 경우의 수 증가 시키기
        cnt += 1
    temp -= p[left]        # 시작 원소인 p[left]를 빼준 합에서 다시 시작

print(cnt)