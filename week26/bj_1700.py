# 전기용퓸 사용 순서 기반으로 플래그를 빼는 최소의 횟수 구하기
# 페이지 교체 알고리즘 중 OPT(앞으로 가장 오랫동안 사용하지 않을 페이지를 교체)

import sys

N, K = map(int, input().split())
goods = list(map(int, sys.stdin.readline().split()))  # 전기용품 사용 순서
consent = [0 for _ in range(N)]    # 플러그에 꼽혀있는 전기용품 목록

def find_used_later(idx):
    temp, good = 0, goods[idx:]
    for c in consent:
        if c in good:  # 모두 나중에 사용이 된다면 그 중 늦게 사용되는 것을 택하기
            temp = max(temp, good.index(c))
        else:       # 나중에 사용이 되지 않는다면 바로 해당 위치에 콘센트 빼기
            return c
    return good[temp]

def is_empty_space():
    for i in range(N):
        if consent[i] == 0:
            return i  # 빈 공간이 있는 경우 해당 위치를 반환
    return -1   # 빈 공간이 없는 경우 -1 반환

for i in range(N):
    if goods[i] not in consent:
        consent[i] = goods[i]

# 후에 사용 가능성이 있다면 해당 전기용품 플래그 부터 우선으로 빼지 않는 것이 최적의 답
ans = 0
for i in range(N, K):
    if goods[i] in consent:  # 전기 용품이 이미 코드에 꼽혀져 있는 경우 패스
        continue

    j = is_empty_space()
    if j > 0:       # 플러그에 빈 공간이 있다면 바로 꼽기
        consent[j] = goods[i]
    else:
        # 플러그에 빈 공간이 없고 새롭게 코드를 꽂아야 하는 전기 용품이라면
        later = find_used_later(i)   # 현재 코드에 꽃혀있는 N개의 용품 중에 누가 제일 나중에 사용 되는지 체크
        consent.remove(later)
        consent.append(goods[i])   # 해당 제품을 빼고 새로 꼽기
        ans += 1     # 뽑는 횟수 증가
print(ans)

