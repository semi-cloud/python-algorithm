from collections import deque


def solution(q, func):
    temp, flag = 0, False
    if len(q) < func.count('D'):   # 배열이 비어 있는데 D를 사용한 경우
        return "error"

    for c in func:
        if c == 'R':
            temp += 1      # R값 카운트
            flag = False if flag else True    # R이 있음을 표시
        else:
            if flag:       # 앞에서 R이 있는 경우, 뒤에서 원소 제거
                q.pop()
            else:
                q.popleft()      # 앞에서 R이 없으면 첫번째 원소 제거

    if temp % 2 != 0:            # R의 개수가 홀수개 이면 마지막 한번만 뒤집기
        q.reverse()
    return "[" + ",".join(q) + "]"


T = int(input())
for _ in range(T):
    p = input()              # 수행할 함수
    p = p.replace('RR', '')  # RR 제거(원 상태는 계산 X)
    n = int(input())         # 배열에 들어 있는 원소 개수
    queue = deque(input()[1:-1].split(','))
    if n == 0:
        queue = []
    print(solution(queue, p))


