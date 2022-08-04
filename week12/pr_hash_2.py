from collections import defaultdict

def solution(participant, completion):
    d1 = defaultdict(int)
    d2 = defaultdict(int)

    for p in participant:          # 참여자 명단
        d1[p] += 1

    for c in completion:           # 완주자 명단
        d2[c] += 1

    for k, v in d1.items():
        if k not in d2.keys() or v > d2[k]:       # 완주자 명단에 없거나 나온 횟수가 더 적을 경우
            return k

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))