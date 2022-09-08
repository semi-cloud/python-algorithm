from collections import defaultdict


def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    d = defaultdict(set)           # 중복 제거를 위해 집합 사용
    for info in report:
        a, b = info.split(" ")     # a : 신고한 사람 b : 신고 당한 사람
        d[b].add(a)

    for key, v in d.items():
        if len(v) >= k:            # 정지된 ID 라면 신고한 사람들 에게 메일 발송
            for value in v:
                answer[id_list.index(value)] += 1
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"],
             ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))