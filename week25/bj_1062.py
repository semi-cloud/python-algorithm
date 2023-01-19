# 어떤 K개의 글자를 가르쳐야 학생들이 읽을 수 있는 단어의 개수가 최대가 되는지 구하기
# 공통되지 않는 글자를 하나씩 추가해 가면서 K개가 됐을때 제일 많은 단어를 읽을 수 있는지 체크

def read_word():
    read = 0
    for word in words:
        for i in range(4, len(word) - 4):  # 시간을 줄이기 위해 anta, tica를 제외한 가운데 부분만 탐색
            if not visited[ord(word[i]) - 97]:   # path 배열에서 in 연산자를 통해 확인하는 거는 시간이 오래 걸림
                break
        else:        # 모든 글자를 읽을 수 있는 경우 증가(break 걸리지 않았을 때)
            read += 1
    return read

ans = 0
def bt(depth, start):
    global ans, cnt

    if depth == cnt:
        ans = max(ans, read_word())  # 읽을 수 있는 단어의 최댓값 찾기
        return

    for i in range(start, len(alphabet)):   # 모든 알파벳이 아니라 N개의 단어 내에 존재하는 알파벳에 대해서만 탐색
        idx = ord(alphabet[i]) - 97
        if not visited[idx]:           # 방문하지 않았다면(이미 가르치기로 한 글자가 아니라면) 탐색에 추가
            visited[idx] = True
            bt(depth + 1, i)       # start :
            visited[idx] = False

        # 아래의 코드는 DEF 중복이 되는 BDFE, BEDF, BEFD 등의 경우까지 다 봐주게 됌
        # path.append(letter)
        # bt(depth + 1)
        # path.pop()

import sys

N, K = map(int, input().split())
words = [sys.stdin.readline().strip() for _ in range(N)]
alphabet = []     # set은 시간을 엄청 잡아 먹음
visited = [False for _ in range(26)]   # 기본으로 필요한 단어는 True 표시
for c in ['a', 'n', 't', 'c', 'i']:
    visited[ord(c) - 97] = True

for word in words:  # 50
    for w in word:  # 15
        if not visited[ord(w) - 97] and w not in alphabet:  # 기본으로 필요한 단어 제외 글자들 구하기
            alphabet.append(w)

if K < 5:    # 최소로 공통인 글자의 개수보다 가르칠 수 있는 글자 수가 작다면 0 반환
    print(0)
elif K == 26:   # 모든 글자를 가르칠 수 있는 경우
    print(N)
elif len(alphabet) < K - 5:    # 배울 수 있는 단어 보다 모르는 단어가 적은 경우
    print(N)  # 모든 단어를 배울 수 있음
else:
    cnt = K - 5      # 공통 글자 제외 추가로 배울 수 있는 글자 개수
    bt(0, 0)            # 나머지 글자에 대해서 백트래킹
    print(ans)

# 시간 초과 코드
# def read_word():
#     read = 0
#     for word in words:
#         for i in range(4, len(word) - 4):  # 시간을 줄이기 위해 anta, tica를 제외한 가운데 부분만 탐색
#             if word[i] not in path:
#                 break
#         else:        # 모든 글자를 읽을 수 있는 경우 증가(break 걸리지 않았을 때)
#             read += 1
#     return read
#
# ans = 0
# path = ['a', 'n', 't', 'i', 'c']
# def bt(depth, start):
#     global ans, cnt
#
#     if depth == cnt:
#         ans = max(ans, read_word())  # 읽을 수 있는 단어의 최댓값 찾기
#         return
#
#     for i in range(start, len(alphabet)):   # 모든 알파벳이 아니라 N개의 단어 내에 존재하는 알파벳에 대해서만 탐색
#         # for letter in alphabet:       # 모든 알파벳이 아니라 N개의 단어 내에 존재하는 알파벳에 대해서만 탐색
#         idx = ord(alphabet[i]) - 97
#         if not visited[idx]:          # 방문하지 않았다면(이미 가르치기로 한 글자가 아니라면) 탐색에 추가
#             visited[idx] = True
#             path.append(alphabet[i])
#             bt(depth + 1, i)
#             path.pop()
#             visited[idx] = False   # 이 부분을 안해준 다면 B가 포함되는 경우들만 검사하고 B가 포함되지 않는 케이스들은 검사하지 X
# 예시)
# B
# DD
# DD
# ZZ
# ZZ
# K = 2일때 B, D, Z / [B, D] : 3개 [B,Z] : 3개 [D,Z] : 4개(근데 이 부분을 앞에서 검사해서 방문 배열이 True 상태이니 검사하지 못하게됌)
