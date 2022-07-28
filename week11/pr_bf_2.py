import math
from itertools import permutations


def is_prime_number(x):          # 소수 판별 알고리즘
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    count = 0
    arr = []
    arr_set = set()
    for i in range(1, len(numbers) + 1):
        arr.extend(list(permutations(list(numbers), i)))    # 모든 경우의 수

    for i, num in enumerate(arr):                  # 중복 제거 위해 집합 형태로 변환
        num = int("".join(num))
        arr_set.add(num)

    for i, num in enumerate(arr_set):
        if num != 0 and num != 1 and is_prime_number(num):     # 소수가 맞다면 카운트 증가
            count += 1
    return count


number = "17"
solution(number)
