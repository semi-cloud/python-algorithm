# 어떤 사이트의 친구 관계가 생긴 순서대로 주어졌을 때, 두 사람의 친구 네트워크에 몇 명이 있는지 구하기(친구 관계만으로 이동할 수 있는 사이)
# a b   : 2
# b c   : 3
# d e   : 2
# e b   : 5 (a b c e d)
# a f   : 6 (a b c e d f)
# f c   : 6 (a b c e d f)

from collections import defaultdict

def find_parent(x):
    if parent[x] == x:
        return x

    parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    a = find_parent(x)  # 제일 루트 노드의 카운팅 값을 반환(계속 갱신 필요)
    b = find_parent(y)
    if friend_cnt[a] == 0: friend_cnt[a] = 1  # 초기값 1로 설정
    if friend_cnt[b] == 0: friend_cnt[b] = 1

    if a < b:
        parent[b] = a
        friend_cnt[a] += friend_cnt[b]  # 다른 작은 집합의 개수를 큰 집합에 합치기
        return friend_cnt[a]      # 가장 루트 노드에 존재한 집합 내부 노드 개수 반환
    elif a > b:
        parent[a] = b
        friend_cnt[b] += friend_cnt[a]  # 다른 작은 집합의 개수를 큰 집합에 합치기
        return friend_cnt[b]
    else:   # 둘이 같은 부모일 경우
        return friend_cnt[a]

T = int(input())
for _ in range(T):
    parent = defaultdict(str)
    friend_cnt = defaultdict(int)
    F = int(input())    # 100,000
    for i in range(F):  # 매번 돌면서 이어진 친구 수 출력
        a, b = list(input().split())
        if parent[a] == '': parent[a] = a
        if parent[b] == '': parent[b] = b
        res = union(a, b)
        print(res)