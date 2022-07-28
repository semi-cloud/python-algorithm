def solution(answers):
    d = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(d)                 # 맞힌 문제 수 저장

    for idx, num in enumerate(answers):
        for i, v in enumerate(d):
            if num == v[idx % len(v)]:    # 각 패턴 수만큼 반복 검사
                s[i] += 1                 # 일치하면 맞힌 문제 수 증가

    return [i + 1 for i, n in enumerate(s) if n == max(s)]     # 높은 점수 오름차순으로 출력


answer_list = [1, 3, 2, 4, 2]
print(solution(answer_list))