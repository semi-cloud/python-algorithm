# 도시의 모든 두 집 쌍에 대해 왕래 가능하면서 절약할 수 있는 최대 액수(끌 수 있는 가로등 개수)
# 제거할 길의 비용이 최대가 되어야 하므로 최소 스패닝 트리
# 1. 간선 오름차순 정렬
# 2. 하나씩 더해가면서 사이클을 발생시키지 않는다면 신장

def find_parent(x):
    if x == parent[x]:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

while True:
    m, n = map(int, input().split())  # 200000 O(ElogV)
    if m == 0 and n == 0:
        break

    edge = []
    parent = [i for i in range(m)]  # 길 정보
    ans, total = 0, 0

    for i in range(n):
        x, y, z = map(int, input().split())
        edge.append((z, x, y))
        total += z

    minimum = 0
    edge.sort()  # 1.간선 비용 순 오름차순 정렬
    for z, x, y in edge:
        if find_parent(x) != find_parent(y):  # 사이클 발생 여부 체크
            union_parent(x, y)  # 발생하지 않는다면 스패닝 트리 추가
            minimum += z
    print(total - minimum)
