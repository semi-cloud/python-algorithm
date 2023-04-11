# 모든 종류 보석 적어도 1개 이상 포함 가장 짧은 구간 구매
# DP 문제 X => 정확한 구간을 구하는게 아니라 구간의 "길이"를 구해야함
# 일단 최소 갯수 이상일 때 까지 j를 증가시키고, 탐색하면서 딕셔너리에 나온 횟수를 체크
# 나온 횟수가 2 이상이면 해당 문자는 불 필요하게 중복이니 i 증가시키기

from collections import defaultdict


def solution(gems):
    d = defaultdict(int)  # 각 문자마다 나온 횟수 저장
    total = len(set(gems))
    answer = []

    i, j = 0, 0
    cnt, flag = 0, False
    for i in range(len(gems)):
        while cnt != total and j < len(gems):  # 모든 보석을 구매할 때 까지 j 증가시키기
            if d[gems[j]] == 0:  # 서로 다른 값이 나온다면 cnt 증가
                cnt += 1
            d[gems[j]] += 1  # 나온 개수 카운팅
            j += 1
            flag = True

        if flag: j -= 1  # 위에 while 문을 안 거치면 j-=1 하면 안됌

        if cnt == total:
            if d[gems[i]] > 1:  # 2개 이상 나온 경우 해당 범위에서는 하나만 존재해도 되니까 제거 가능하므로 제거
                d[gems[i]] -= 1  # 제거한 값 갱신
            else:
                # 1개인 경우 더 이상 줄이지 못함, 결과에 추가
                answer.append((i + 1, j + 1, (j + 1) - (i + 1)))
                d[gems[i]] -= 1
                cnt = cnt - 1  # 다음 결과값으로 넘어가므로 cnt - 1
                j += 1
            flag = False

    res = []
    arr = sorted(answer, key=lambda x: x[2])
    min = arr[0][2]
    for a in answer:  # 최소 구간 길이 찾기(그냥 제때 갱신해주면 될듯)
        if a[2] == min:
            res.append((a[0], a[1]))
    return sorted(res, key=lambda x: x[0])[0]