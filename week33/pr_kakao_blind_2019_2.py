# 후보키 : 모든 부분 집합을 구한 이후에 후보키가 될 수 있는 것을 판별
# 비트 마스킹 : 기존의 값을 이용하지 않고 비트로 바뀐 0과 1, 그리고 그 비트들의 위치만으로 값을 결정하는 방법

# 1 : 0 0 0 1 (0번 칼럼) / 2: 0 0 1 0 (1번 칼럼) / 3 : 0 0 1 1 (0 + 1 번 칼럼) ... / 16(1<<4) : 1 1 1 1 (0+1+2+3번 칼럼)
def solution(relation):
    N, M = len(relation[0]), len(relation)  # 열과 행

    key = []  # 후보키 목록
    for i in range(1, 1 << N):  # 비트마스킹 자체로 조합을 표현 가능
        # 1. 집합의 최소성 검사
        dup = False
        for k in key:
            if k & i == k:  # 같은 경우 이미 후보키가 포함되어 있고 나머지들은 제외 가능하므로 최소성 만족 X
                dup = True
                break
        if dup: continue

        # 2. 집합의 유일성 검사(set)
        temp = set()
        for j in range(M):  # 모든 행에 대해서 검사

            lis = ""      # 리스트로 하면 원소가 하나일 때랑 구분이 X
            for k in range(N):
                if not i & (1 << k): continue  # idx 번째 컬럼에 비트가 켜져 있는지(포함되어 있는지) 체크
                lis += relation[j][k]
            temp.add(lis)  # 집합 단위로 한번에 담아서 증복이 없는지 비교 해야함(각 칼럼 마다 중복 체크 X)

        if len(temp) == M:  # 중복이 없는 경우 해당 집합을 후보키에 추가
            key.append(i)
    return len(key)
