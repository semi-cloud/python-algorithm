# 모든 파티에 참가 했을때, 거짓말쟁이로 알려지지 않으면서 과장된 이야기를 할 수 있는 파티 개수의 최댓값
# 분리 집합(서로소 집합)은 DFS와 같은 그래프 탐색의 반복이 효율성이 떨어짐으로 인해 나온 대안

# 1. 진실을 아는 사람과 같은 파티에 있는 사람들이 참여하는 다른 파티에서도 거짓말 불가능 = 같은 그룹으로 묶기
# 2. 파티장들에서 겹친 자들이 진실을 아는 자에 속하지 않는다면 거짓말을 할 수 있음
# ex) 진실을 알고 있는 사람 : 50번 가정
# 2 3
# 2 4
# 5 6
# ...
# 48 49
# 49 50
# => 집합이 두개로 나눠짐 : 2 - 3 - 4(거짓말 가능 집합) / 50 - 49.. - 5 (진실만 가능 집합)

import sys

# 일반 부모 배열 : [1, 1, 2, 3, 5, 5]
# 경로 압축 부모 배열 : [1, 1, 1, 1, 5, 5]
def find_parent(x):       # x의 부모 찾아서 반환 3
    if parent[x] == x:    # x가 루트까지 도달 했다면 그대로 반환
        return x

    parent[x] = find_parent(parent[x])  # find 연산 실행시 마다 각 노드의 부모 노드를 루트로 만들어주기(경로 압축)
    return parent[x]   # 루트 노드를 차례대로 반환

def union(a, b):
    pa = find_parent(a)
    pb = find_parent(b)

    if pb < pa:           # 두 그래프 하나로 합치기(부모를 공통화)
        parent[pa] = pb   # parent[a] = pb (X)
    else:
        parent[pb] = pa

N, M = map(int, input().split())
T, *truth = list(map(int, sys.stdin.readline().split()))    # list 가변 unpacking
parent = [i for i in range(N+1)]     # 부모 배열

# 진실을 아는 자의 루트 노드는 0으로 지정(가장 작은 수)
for i in range(T):
    parent[truth[i]] = 0

parties = [[] for _ in range(M)]     # 각 파티 마다의 참석자
for i in range(M):
    p, *temp = list(map(int, sys.stdin.readline().split()))
    for j in range(len(temp)):
        parties[i].append(temp[j])  # 파티 참석자들 정보 저장
        if p == 1:  # 참석자가 한명인 경우
            continue

        if j != 0:
            union(temp[0], temp[j])     # union 통해 연결 여부 확인(따로 인접 노드 그래프가 필요 X)

if T == 0:    # 진실을 아는 자가 없다면
    print(M)  # 모든 파티에서 거짓말 가능
else:
    ans = 0
    for i, party in enumerate(parties):  # 모든 파티를 돌면서
        for p in party:    # 부모가 0 이라면(진실을 아는 자와 연결되어 있다면) 거짓말을 하지 못함
            # 서로 다른 그룹의 새로운 연결 정보가 생겼을 때, 두 그룹을 합친 후 모든 노드의 루트 노트 갱신 해야함
            # b + a라 할 때, a 집합의 루트 노드를 합칠 b 집합의 루트 노드 값으로 바꾼다면
            # b 집합에 있던 원소의 찐 부모 노드를 찾기 위해 find 연산을 다시 해줌으로써 a 집합의 루트 노드 값이 나올 수 있음
            if find_parent(parent[p]) == 0:  # parent[p] == 0 (X)
                break
        else:
            ans += 1
    print(ans)

