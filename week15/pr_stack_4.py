# 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 출력
from collections import deque


def solution(priorities, location):
    q = deque([(p, i) for i, p in enumerate(priorities)])   # p : 중요도, i : 위치(인덱스)
    cnt = 1          # 인쇄 되는 순서

    while q:
        node, idx = q.popleft()
        for num, _ in q:
            if node < num:   # 더 큰 수가 있다면 맨 끝에 다시 추가
                q.append((node, idx))
                break
        else:                # 더 큰 수가 없다면 프린트
            if idx == location:
                return cnt
            cnt += 1


print(solution([1, 1, 9, 1, 1, 1], 0))