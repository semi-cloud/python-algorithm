# 최소 몇 단계의 과정을 거쳐 begin 을 target 으로 변환할 수 있는지 구하기

from collections import deque

def check_word(a, b):
    temp = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            temp += 1
        if temp >= len(a)-1:  # 한 단어만 차이 나는 경우
            return True

def solution(begin, target, words):
    q = deque()
    visited = [False] * len(words)
    q.append((begin, 0))    # 시작 단어, 깊이

    while q:
        w, d = q.popleft()
        if w == target:      # 타켓 문자열 변환한 경우
            return d

        for i, word in enumerate(words):    # 한 단어 차이 나는 것들 먼저 큐에 추가 후 방문 처리
            if not visited[i] and check_word(w, word):
                visited[i] = True
                q.append((word, d + 1))
    return 0     # 변환 불가능 경우

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))