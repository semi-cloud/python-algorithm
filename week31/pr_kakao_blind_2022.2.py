import math

def is_prime(n):  # 1,000
    if n == 1: return False

    for i in range(2, int(math.sqrt(n)) + 1):  # 제곱근 까지 확인
        if n % i == 0:  # 1과 자기 자신이 아닌 숫자로 나누어 떨어지는 경우 소수가 아님
            return False
    return True

def solution(n, k):  # 1,000,000 : O(N)
    ans = 0
    prime = list()
    while n > 0:
        prime.append(n % k)
        n //= k
    prime.reverse()

    temp = ""
    for p in prime:
        if p == 0:   # 0 을 만나기 전까지의 숫자가 소수인지 확인
            if temp and is_prime(int(temp)):
                ans += 1
            temp = ""  # 문자열 초기화
        else:
            temp += str(p)

    if len(temp) > 0 and is_prime(int(temp)):  # 남은 숫자 처리
        ans += 1
    return ans

print(solution(437674, 3))