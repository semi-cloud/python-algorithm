# 조건을 만족하는 사람 중 코딩테스트 점수를 X점 이상 받은 사람은 몇명인가?
# 2. X 점수 이상 => 이중 포문이 아니라 이분 탐색 사용해서 내 위로 몇명이 존재하는지 체크하기
# O(N^2)가 되지 않으려면 쿼리가 주어졌을 때 => 바로 쿼리에 해당하는 사람이 누구인지 찾아야하므로(ex) "query" : [점수1, 점수 2..], ..])
# 맵으로 모든 검색 조건들에 대해 사람을 뽑아서 점수를 기록해두고, 쿼리문의 점수보다 높은 개수만 찾아주면 끝(이분 탐색)
# a b c d e 150 : {[0번 사람, 점수], [1번 사람, 점수] .. }  # 사람 수가 50,000

from collections import defaultdict
from bisect import bisect_left

all_queries = defaultdict(list)
def solution(info, query):
    res = []
    for i in range(len(info)):  # 50,000
        get_queries(0, info[i].split(" "), "")

    # 정렬 로직 밖으로 빼기
    for v in all_queries.values():
        v.sort()

    for i in range(len(query)):  # 100,000
        temp = query[i].split(" ")
        score, q = int(temp[-1]), " ".join(temp[:-1])  # 쿼리 부분과 점수 부분 분리

        score_list = all_queries[q]  # 해당 쿼리에 맞는 점수 리스트 가져오기
        res.append(len(score_list) - bisect_left(score_list, score))  # 이분 탐색(O(logN)) 으로 위치 찾고 해당 점수보다 이상인 사람 개수 찾기
    return res

def get_queries(depth, arr, string):
    if depth == 4:
        all_queries[string[:len(string)-5]].append(int(arr[-1]))
        return

    get_queries(depth + 1, arr, string + arr[depth] + " and ")   # 1. 해당 위치에서 문자를 사용하는 경우
    get_queries(depth + 1, arr, string + '-' + " and ")    # 2. 해당 위치에서 '-'를 사용하는 경우

print(solution(["java backend junior pizza 150",
                "python frontend senior chicken 210",
                "python frontend senior chicken 150",
                "cpp backend senior pizza 260",
                "java backend junior chicken 80",
                "python backend senior chicken 50"],
               ["java and backend and junior and pizza 100",
                "python and frontend and senior and chicken 200",
                "cpp and - and senior and pizza 250",
                "- and backend and senior and - 150",
                "- and - and - and chicken 100",
                "- and - and - and - 150"]
               ))

# 시간 초과 코드
def solution(info, query):
    dic = defaultdict(list)
    scores = defaultdict(list)
    res = []

    for i in range(len(info)):
        a, b, c, d, e = info[i].split(" ")
        dic[a].append(i + 1)  # 어떤 사람하고 연결이 되어 있는지 저장
        dic[b].append(i + 1)
        dic[c].append(i + 1)
        dic[d].append(i + 1)
        scores[int(e)].append(i + 1)

    for i in range(len(query)):  # 100000
        conds = []
        lis = query[i].replace("and", "").split("  ")
        d, e = "", 0
        for i in range(len(lis)):  # 검색에 사용될 조건만 뽑기
            if i == 3:
                d, e = lis[i].split(" ")
                e = int(e)
                if d != "-": conds.append(d)
                continue

            if lis[i] != "-": conds.append(lis[i])

        if len(conds) > 0:
            both = set(dic[conds[0]])
            for i in range(1, len(conds)):  # 모든 조건에 공통으로 들어있는 지원자 찾기
                both = both & set(dic[conds[i]])
        else:
            both = set([i + 1 for i in range(len(info))])  # 조건이 없는 경우 모든 사람이 대상이 됌

        cnt = 0
        for people in both:  # 교집합인 애들 점수 체크
            for key in scores.keys():  # x 점 이상인 값 리스트에 해당 지원자가 들어있으면 결과에 추가
                if e <= key and people in scores[key]:
                    cnt += 1
        res.append(cnt)
    return res

# 잘못된 조합 코드
# def get_queries(depth, idx, arr):    # 순열 생성: # [java, backend, junior, pizza, 150]
#     if depth > 4: return
#
#     string = ""
#     for i in range(len(arr)-2):
#         string += arr[i]
#         string += " and "
#     string += arr[len(arr)-2]   # 마지막 점수 추가
#     all_queries[string].append(int(arr[-1]))  # 결국 해당 점수 이상인 것만 고르면 되니까 사람 정보 말고 점수만 추가
#
#     for i in range(idx, 4):
#         prev = arr[i]
#         arr[i] = '-'
#         get_queries(depth + 1, idx + 1, arr)
#         arr[i] = prev
