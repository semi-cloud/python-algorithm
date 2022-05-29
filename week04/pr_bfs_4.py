# 주어진 항공권을 모두 이용하여 여행경로 짜기, 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로 출력
from collections import defaultdict

n = int(input())
tickets = [list(input().split()) for _ in range(n)]

def dfs():
    result = []
    routes = defaultdict(list)

    for ticket in tickets:
        routes[ticket[0]].append(ticket[1])       # 출발-도착 정보들을 딕셔너리에 추가

    for key in routes.keys():
        routes[key].sort(reverse=True)            # 알파벳 빠른 순으로 스택의 탑에 가게 정렬

    st = ["ICN"]
    while st:
        x = st[-1]

        if not routes[x]:             # 도착지가 존재하지 않으면(끝났으면) 스택에서 꺼내서 결과값에 추가
            result.append(st.pop())
        else:
            st.append(routes[x].pop())     # 마지막 원소(알파벳 빠른 순)꺼내서 스택에 추가
    result.reverse()
    return result

print(dfs())




